import glob, json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, "assets", "img")
SITE_URL = "https://www.ebc.live"

_cache = {}
def img(basename):
    """Return assets/img/<largest-file-matching-basename> path."""
    if basename in _cache:
        return _cache[basename]
    pattern = os.path.join(IMG_DIR, glob.escape(basename) + "_*")
    candidates = glob.glob(pattern)
    if not candidates:
        raise FileNotFoundError(basename)
    best = max(candidates, key=os.path.getsize)
    rel = "assets/img/" + os.path.basename(best)
    _cache[basename] = rel
    return rel


NAV_ITEMS = [
    ("about-us.html", "Studio"),
    ("equipment.html", "Equipment"),
    ("index.html#services", "Services"),
    ("gallery.html", "Gallery"),
    ("testimonials.html", "Testimonials"),
    ("contact.html", "Contact"),
]


def nav(active):
    links = "\n".join(
        f'<a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f"""
<header class="site-header">
  <nav class="nav">
    <a href="index.html" class="nav-logo"><img src="{img('Empire_Logo_1')}" alt="The Empire Studio"></a>
    <input type="checkbox" id="nav-toggle-input" class="nav-toggle-input">
    <div class="nav-links">
      {links}
    </div>
    <div class="nav-right">
      <a href="contact.html" class="btn btn-primary btn-sm">Book Now</a>
      <label for="nav-toggle-input" class="nav-toggle" aria-label="Menu">
        <span></span><span></span><span></span>
      </label>
    </div>
  </nav>
</header>
"""


FOOTER = f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <img class="footer-logo" src="{img('Empire_Logo_1')}" alt="The Empire Studio">
        <p>153 sqm of acoustically treated live room in a converted East London church. Recording, scoring, podcasts &amp; live sessions.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <a href="about-us.html">About</a>
        <a href="equipment.html">Studio &amp; Gear</a>
        <a href="gallery.html">Gallery</a>
      </div>
      <div class="footer-col">
        <h4>Visit</h4>
        <a href="testimonials.html">Testimonials</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Follow</h4>
        <a href="http://instagram.com/theempirestudiolondon">Instagram</a>
        <a href="contact.html">Enquire</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; The Empire Broadcasting Corporation Ltd - 82a, James Carter Road, Mildenhall, Bury
      St. Edmunds, England, IP28 7DE. Registered in England &amp; Wales. Company Number 12730620.
      VAT Number GB 362904885</span>
      <span>The Sound of Perfection</span>
    </div>
  </div>
</footer>
"""


def page(active, title, description, body, keywords="", og_image=None, extra_class=""):
    canonical = f"{SITE_URL}/" if active == "index.html" else f"{SITE_URL}/{active}"
    full_title = f"{title} — The Empire Studio"
    og_img_url = f"{SITE_URL}/{og_image or img('GAL_7')}"

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "The Empire Broadcasting Corporation",
        "alternateName": "The Empire Studio",
        "image": og_img_url,
        "url": f"{SITE_URL}/",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "33 Wadeson Street",
            "addressLocality": "London",
            "postalCode": "E2 9DR",
            "addressCountry": "GB",
        },
        "sameAs": ["http://instagram.com/theempirestudiolondon"],
        "description": "Recording studio in East London with a professional live room, "
                        "control room and equipment for music, film and podcasts.",
    }, indent=2)

    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow">
<meta name="author" content="The Empire Broadcasting Corporation">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{img('Empire_Logo_1')}">
<link rel="stylesheet" href="assets/css/refresh.css">

<meta property="og:type" content="website">
<meta property="og:site_name" content="The Empire Studio">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img_url}">
<meta property="og:locale" content="en_GB">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_img_url}">

<script type="application/ld+json">
{ld_json}
</script>
</head>
<body class="{extra_class}">
{nav(active)}
{body}
{FOOTER}
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


LIGHTBOX_HTML = """
<div class="lightbox" id="lightbox">
  <button class="lightbox-close" aria-label="Close">&times;</button>
  <button class="lightbox-prev" aria-label="Previous image">&#8592;</button>
  <img class="lightbox-img" src="" alt="">
  <button class="lightbox-next" aria-label="Next image">&#8594;</button>
</div>
"""


def carousel(inner_html, track_class):
    return f"""
<div class="carousel">
  <button class="carousel-arrow prev" aria-label="Scroll left">&#8592;</button>
  <div class="{track_class} h-scroll">
    {inner_html}
  </div>
  <button class="carousel-arrow next" aria-label="Scroll right">&#8594;</button>
</div>
"""


def marquee(items):
    seq = "".join(f'{it}<span>〰</span>' for it in items)
    return f"""
<div class="marquee"><div class="marquee-track">{seq}{seq}</div></div>
"""


def write(name, html):
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {name} ({len(html)} bytes)")
