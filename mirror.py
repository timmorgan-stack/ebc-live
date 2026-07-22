import os
import re
import sys
import hashlib
from urllib.parse import urljoin, urlparse, unquote

import requests
from bs4 import BeautifulSoup

BASE = "https://www.ebc.live"
OUT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(OUT, "assets")

PAGES = [
    ("/", "index.html"),
    ("/about-us", "about-us.html"),
    ("/equipment", "equipment.html"),
    ("/testimonials", "testimonials.html"),
    ("/gallery", "gallery.html"),
    ("/news", "news.html"),
    ("/contact", "contact.html"),
    ("/events", "events.html"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

session = requests.Session()
session.headers.update(HEADERS)

asset_cache = {}  # remote_url -> local relative path (e.g. assets/css/xxxx.css)


def asset_subdir(url):
    path = urlparse(url).path.lower()
    if path.endswith((".css",)):
        return "css"
    if path.endswith((".js",)):
        return "js"
    if path.endswith((".woff", ".woff2", ".ttf", ".otf", ".eot")):
        return "fonts"
    if path.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".avif")):
        return "img"
    return "other"


def local_filename(url):
    parsed = urlparse(url)
    base = os.path.basename(parsed.path) or "file"
    base = unquote(base)
    # strip query-derived uniqueness into hash suffix to avoid collisions/format params
    h = hashlib.md5((url).encode("utf-8")).hexdigest()[:8]
    name, ext = os.path.splitext(base)
    if not ext:
        ext = ""
    safe_name = re.sub(r"[^a-zA-Z0-9_\-.]", "_", name)[:80]
    return f"{safe_name}_{h}{ext}"


def download_asset(url):
    if url in asset_cache:
        return asset_cache[url]
    if url.startswith("data:") or url.startswith("blob:"):
        return url
    try:
        resp = session.get(url, timeout=20)
        resp.raise_for_status()
    except Exception as e:
        print(f"  ! failed to download {url}: {e}")
        return url

    subdir = asset_subdir(url)
    fname = local_filename(url)
    local_path = os.path.join(ASSETS, subdir, fname)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(resp.content)

    rel = f"assets/{subdir}/{fname}"
    asset_cache[url] = rel
    print(f"  + {url} -> {rel} ({len(resp.content)} bytes)")
    return rel


def process_srcset(value, page_url):
    parts = []
    for chunk in value.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        bits = chunk.split()
        url = bits[0]
        descriptor = " ".join(bits[1:])
        abs_url = urljoin(page_url, url)
        local = download_asset(abs_url)
        parts.append(f"{local} {descriptor}".strip())
    return ", ".join(parts)


URL_IN_CSS_RE = re.compile(r"url\((['\"]?)([^'\")]+)\1\)")


def process_css_text(css_text, css_url):
    def repl(m):
        quote, url = m.group(1), m.group(2)
        if url.startswith("data:"):
            return m.group(0)
        abs_url = urljoin(css_url, url)
        local = download_asset(abs_url)
        return f"url({quote}{local}{quote})"
    return URL_IN_CSS_RE.sub(repl, css_text)


def fetch_page(path):
    url = urljoin(BASE, path)
    print(f"Fetching page {url}")
    resp = session.get(url, timeout=20)
    resp.raise_for_status()
    return resp.text, url


def process_page(html, page_url):
    soup = BeautifulSoup(html, "html.parser")

    # <link rel="stylesheet" href="...">
    for link in soup.find_all("link", href=True):
        rel = " ".join(link.get("rel", [])).lower()
        href = link["href"]
        if href.startswith(("data:", "mailto:", "#")):
            continue
        if "stylesheet" in rel or href.lower().endswith(".css") or "icon" in rel:
            abs_url = urljoin(page_url, href)
            local = download_asset(abs_url)
            link["href"] = local

    # <style> blocks with url(...)
    for style_tag in soup.find_all("style"):
        if style_tag.string:
            style_tag.string.replace_with(process_css_text(style_tag.string, page_url))

    # inline style="" attributes
    for tag in soup.find_all(style=True):
        tag["style"] = process_css_text(tag["style"], page_url)

    # <script src="...">
    for script in soup.find_all("script", src=True):
        src = script["src"]
        if src.startswith("data:"):
            continue
        abs_url = urljoin(page_url, src)
        # skip obvious third-party trackers we don't need to localize but still fine to fetch
        local = download_asset(abs_url)
        script["src"] = local

    # <img src / data-src / srcset>
    for img in soup.find_all("img"):
        for attr in ("src", "data-src", "data-image"):
            if img.get(attr):
                abs_url = urljoin(page_url, img[attr])
                img[attr] = download_asset(abs_url)
        if img.get("srcset"):
            img["srcset"] = process_srcset(img["srcset"], page_url)
        if img.get("data-srcset"):
            img["data-srcset"] = process_srcset(img["data-srcset"], page_url)

    # <source srcset> (picture/video)
    for source in soup.find_all("source"):
        if source.get("srcset"):
            source["srcset"] = process_srcset(source["srcset"], page_url)
        if source.get("src"):
            abs_url = urljoin(page_url, source["src"])
            source["src"] = download_asset(abs_url)

    # rewrite internal nav links to local .html files where we know them
    path_to_file = {p: f for p, f in PAGES}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        parsed = urlparse(href)
        if parsed.netloc and parsed.netloc not in ("www.ebc.live", "ebc.live"):
            continue  # external link, leave as-is
        p = parsed.path or "/"
        if p in path_to_file:
            a["href"] = path_to_file[p]
        elif p.rstrip("/") + "" in path_to_file:
            a["href"] = path_to_file[p.rstrip("/")]

    return str(soup)


def main():
    for path, fname in PAGES:
        try:
            html, page_url = fetch_page(path)
        except Exception as e:
            print(f"! failed to fetch {path}: {e}")
            continue
        processed = process_page(html, page_url)
        out_path = os.path.join(OUT, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(processed)
        print(f"Saved {out_path}\n")

    print(f"\nDone. Downloaded {len(asset_cache)} unique assets.")


if __name__ == "__main__":
    main()
