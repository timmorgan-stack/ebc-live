import glob, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(ROOT, "assets", "img")

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
        <a href="news.html">Journal</a>
      </div>
      <div class="footer-col">
        <h4>Visit</h4>
        <a href="testimonials.html">Testimonials</a>
        <a href="events.html">Events</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Follow</h4>
        <a href="http://instagram.com/theempirestudiolondon">Instagram</a>
        <a href="contact.html">Enquire</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; The Empire Broadcasting Corporation — East London</span>
      <span>The Sound of Perfection</span>
    </div>
  </div>
</footer>
"""


def page(active, title, description, body, extra_class=""):
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — The Empire Studio</title>
<meta name="description" content="{description}">
<link rel="icon" href="{img('Empire_Logo_1')}">
<link rel="stylesheet" href="assets/css/refresh.css">
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
