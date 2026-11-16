"""Shared layout pieces for generating the Laybond static site."""

SITE = "https://laybond.co.in"
PHONE1 = "+91 94431 69842"
PHONE1_RAW = "+919443169842"
PHONE2 = "+91 98400 32218"
PHONE2_RAW = "+919840032218"
EMAIL1 = "sales@laybond.co.in"
EMAIL2 = "laybond@gmail.com"
WA = "https://wa.me/919443169842?text=Hello%20Laybond%2C%20I%20would%20like%20a%20quote%20for%20"
ADDRESS_HTML = "14-B, SIPCOT Industrial Complex,<br>Pudukkottai – 622 002,<br>Tamil Nadu, India"

I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>',
 "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>',
 "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>',
 "left": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
 "right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 0 1 2.2 12C2.2 6.6 6.6 2.2 12 2.2c2.6 0 5.1 1 6.9 2.9a9.7 9.7 0 0 1 2.9 6.9c0 5.4-4.4 9.8-9.8 9.8zm8.4-18.2A11.8 11.8 0 0 0 12 0C5.5 0 .2 5.3.2 11.9c0 2.1.5 4.1 1.6 5.9L.1 24l6.3-1.7c1.7.9 3.7 1.4 5.7 1.4 6.5 0 11.9-5.3 11.9-11.9 0-3.2-1.2-6.2-3.5-8.4z"/></svg>',
 # Product icons
 "acid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21.5h11.6a2 2 0 0 0 1.7-3L14 9V3"/><path d="M7 15h10"/></svg>',
 "tank": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="7" ry="2.5"/><path d="M5 5v13c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V5"/><path d="M5 11.5c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5"/></svg>',
 "scrub": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 22V8h8v14M10 8V2h4v6M5 22h14"/><path d="M15 4c1.5-1 3-1 4 0M17 6.5c1.2-.8 2.4-.8 3.5 0"/></svg>',
 "pipe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8h9a3 3 0 0 1 3 3v11M2 14h5a1 1 0 0 1 1 1v7"/><path d="M2 6v10M12 22h8M14 22v-2M8 22v-2"/></svg>',
 "lining": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M3 9h4M17 15h4"/></svg>',
 "fab": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z"/></svg>',
 # Feature icons
 "feather": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 12.2A6 6 0 0 0 11.8 3.8L5 10.6V19h8.4z"/><path d="M16 8L2 22M17.5 15H9"/></svg>',
 "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.7l5.7 5.6a8 8 0 1 1-11.3 0z"/><path d="M8 14a4 4 0 0 0 4 4"/></svg>',
 "temp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z"/></svg>',
 "rupee": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12M6 8h12M6 13l8.5 8M6 13h3a5 5 0 0 0 0-10"/></svg>',
 "ruler": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.3 8.7L8.7 21.3a1 1 0 0 1-1.4 0l-4.6-4.6a1 1 0 0 1 0-1.4L15.3 2.7a1 1 0 0 1 1.4 0l4.6 4.6a1 1 0 0 1 0 1.4z"/><path d="M7.5 10.5l2 2M10.5 7.5l2 2M13.5 4.5l2 2M4.5 13.5l2 2"/></svg>',
 "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z"/></svg>',
 # Industry icons
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9z"/></svg>',
 "factory": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20V9l6 4V9l6 4V4h4l2 16zM2 20h20"/></svg>',
 "cup": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h14l-2 18H7zM5.5 8h13"/></svg>',
 "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17H3v-5l2-5h14l2 5v5h-2M5 12h14"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/></svg>',
 "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v7l-5 9a1.5 1.5 0 0 0 1.3 2h11.4a1.5 1.5 0 0 0 1.3-2l-5-9V3"/></svg>',
 "pill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 20.5l10-10a4.9 4.9 0 0 0-7-7l-10 10a4.9 4.9 0 0 0 7 7zM8.5 8.5l7 7"/></svg>',
 "thread": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="3" width="12" height="18" rx="2"/><path d="M6 8l12 3M6 12l12 3M6 16l12 3"/></svg>',
 "oil": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v6M8 22l4-14 4 14M6 22h12M9.5 15h5"/></svg>',
 "leather": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4c3 1 5 1 8 0s5-1 8 0c-1 3-1 5 0 8s1 5 0 8c-3-1-5-1-8 0s-5 1-8 0c1-3 1-5 0-8s-1-5 0-8z"/></svg>',
 "metal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18l3-8h12l3 8zM7 10l2-5h6l2 5"/></svg>',
 "water": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2-2 4-2 6 0s4 2 6 0 4-2 6 0M2 18c2-2 4-2 6 0s4 2 6 0 4-2 6 0M12 2l3 4a3 3 0 1 1-6 0z"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10zM2 21c0-3 1.9-5.4 5.2-6"/></svg>',
 "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.5 13L17 22l-5-3-5 3 1.5-9"/></svg>',
}

PRODUCTS = [
  # slug, title, short, icon, image name
  ("chemical-handling-systems.html", "Acid Handling Systems", "Complete chemical storage & dosing systems, 1–300 m³", "acid", "acid-handling"),
  ("frp-tanks.html", "Tanks & Vessels", "FRP storage tanks for corrosive & caustic chemicals", "tank", "frp-tanks"),
  ("fume-extraction.html", "Scrubbing Systems", "Fume scrubbers, ducts, stacks & exhaust systems", "scrub", "scrubbers"),
  ("pipe-fittings.html", "Pipe & Fittings", "FRP pipe 25–1500 mm with a full fittings range", "pipe", "pipe-fittings"),
  ("corrosion-proof-linings.html", "Corrosion-Proof Linings", "FRP linings for steel & concrete structures", "lining", "linings"),
  ("steel-fabrications.html", "Fabrication & Others", "MS / SS tanks, agitators, motor guards & structures", "fab", "fabrication"),
]
PRODUCT_SLUGS = [p[0] for p in PRODUCTS]


def media(src, label, cls="", alt=None, eager=False):
    alt = label if alt is None else alt
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<div class="media {cls}" data-label="{label}"><img src="{src}" alt="{alt}" {loading} decoding="async" onerror="this.remove()"></div>'


def head(title, desc, path, og_image="assets/images/hero/home-hero.jpg"):
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1565c0">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Laybond Pipings &amp; Equipments">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/images/logo/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/images/logo/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Laybond Pipings & Equipments","alternateName":"Laybond","url":"{SITE}/","logo":"{SITE}/assets/images/logo/Laybond2.png","foundingDate":"1994","slogan":"Mission Against Corrosion","email":"{EMAIL1}","telephone":"{PHONE1_RAW}","address":{{"@type":"PostalAddress","streetAddress":"14-B, SIPCOT Industrial Complex","addressLocality":"Pudukkottai","postalCode":"622002","addressRegion":"Tamil Nadu","addressCountry":"IN"}},"contactPoint":[{{"@type":"ContactPoint","telephone":"{PHONE1_RAW}","contactType":"sales","areaServed":"IN"}},{{"@type":"ContactPoint","telephone":"{PHONE2_RAW}","contactType":"sales","areaServed":"IN"}}]}}
</script>
</head>
"""


def header(path, solid=False):
    def cur(p):
        return ' aria-current="page"' if path == p else ""
    in_products = path in PRODUCT_SLUGS
    mega = "".join(
        f'<a href="{s}"{cur(s)}><span class="mega-icon">{I[ic]}</span><span><strong>{t}</strong><span>{d}</span></span></a>'
        for s, t, d, ic, _ in PRODUCTS)
    page_cls = "page-" + path.replace(".html", "")
    return f"""<body class="{page_cls}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header{' is-solid' if solid else ''}">
  <div class="container header-inner">
    <a class="logo" href="index.html" aria-label="Laybond – home"><img src="assets/images/logo/laybond-logo-color@2x.png" alt="Laybond Composite Engineering" width="240" height="62"></a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <a href="index.html"{cur('index.html')}>Home</a>
      <a href="about.html"{cur('about.html')}>About</a>
      <div class="nav-drop{' is-current' if in_products else ''}">
        <button type="button" aria-expanded="false" aria-haspopup="true">Products {I['chev']}</button>
        <div class="mega">{mega}</div>
      </div>
      <a href="industries.html"{cur('industries.html')}>Industries</a>
      <a href="technical.html"{cur('technical.html')}>Technical</a>
      <a href="gallery.html"{cur('gallery.html')}>Gallery</a>
      <a href="contact.html"{cur('contact.html')}>Contact</a>
      <div class="mobile-cta">
        <a class="btn btn--primary" href="contact.html">Request a Quote {I['arrow']}</a>
        <a class="btn btn--ghost" href="tel:{PHONE1_RAW}">{I['phone']} {PHONE1}</a>
      </div>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{PHONE1_RAW}">{I['phone']} {PHONE1}</a>
      <a class="btn btn--primary" href="contact.html">Get a Quote</a>
      <button class="menu-toggle" type="button" aria-label="Menu" aria-controls="site-nav" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">
"""


def cta(title="Have a corrosion challenge?", text="Tell us the chemical, concentration, temperature and volume. Our engineers will recommend the right FRP or dual-laminate solution and send you a detailed quote.", product=None):
    href = "contact.html" + (f"?product={product}" if product else "")
    return f"""<section class="section section--tight">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--primary" href="{href}">Request a Quote {I['arrow']}</a>
        <a class="btn btn--ghost" href="{WA}your%20requirement" target="_blank" rel="noopener">{I['wa']} WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""


def footer(extra_scripts=""):
    prod = "".join(f'<li><a href="{s}">{t}</a></li>' for s, t, *_ in PRODUCTS)
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/images/logo/Laybond2.png" alt="Laybond" width="240" height="62" loading="lazy">
        <p class="footer-tag">Mission Against <span>Corrosion</span></p>
        <p>FRP &amp; dual-laminate thermoplastic tanks, piping, scrubbers and linings, designed and built in Tamil Nadu since 1994.</p>
        <span class="iso-badge">{I['award']} ISO 9001 Certified</span>
      </div>
      <div>
        <h4>Products</h4>
        <ul>{prod}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="industries.html">Industries</a></li>
          <li><a href="technical.html">Technical &amp; Downloads</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="warranty.html">Warranty</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Head Office</h4>
        <ul class="footer-contact">
          <li>{I['pin']}<address>{ADDRESS_HTML}</address></li>
          <li>{I['phone']}<span><a href="tel:{PHONE1_RAW}">{PHONE1}</a><br><a href="tel:{PHONE2_RAW}">{PHONE2}</a></span></li>
          <li>{I['mail']}<span><a href="mailto:{EMAIL1}">{EMAIL1}</a><br><a href="mailto:{EMAIL2}">{EMAIL2}</a></span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Laybond Pipings &amp; Equipments. All rights reserved.</span>
      <span><a href="warranty.html">Warranty</a> · <a href="sitemap.xml">Sitemap</a></span>
    </div>
  </div>
</footer>
<div class="float-actions">
  <a class="float-btn float-btn--top" href="#main" aria-label="Back to top">{I['up']}</a>
  <a class="float-btn float-btn--call" href="tel:{PHONE1_RAW}" aria-label="Call Laybond">{I['phone']}</a>
  <a class="float-btn float-btn--wa" href="{WA}your%20requirement" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I['wa']}</a>
</div>
{extra_scripts}<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(title, lead, crumbs, img, label, eyebrow=None):
    crumb_html = '<li><a href="index.html">Home</a></li>' + "".join(
        (f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>') for t, h in crumbs)
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f"""<section class="page-hero">
  <div class="media hero-media" data-label="{label}"><img src="{img}" alt="" fetchpriority="high" onerror="this.remove()"></div>
  <div class="container">
    <ol class="breadcrumb">{crumb_html}</ol>
    {eb}
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


def product_strip(path):
    ac = ' aria-current="page"'
    links = "".join(f'<a href="{s}"{ac if s == path else ""}>{t}</a>' for s, t, *_ in PRODUCTS)
    return f'<div class="product-strip"><div class="container"><nav class="product-nav" aria-label="Products">{links}</nav></div></div>\n'


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def checks(items, cols=False):
    return f'<ul class="check-list{" check-list--2" if cols else ""}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


DUAL_LAMINATE = f"""<section class="section section--white">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Materials</span>
      <h2>Resin systems &amp; dual laminate</h2>
      <p class="lead">We build to customer specification using polyester, bisphenol and vinyl ester thermoset resins. Where FRP alone will not work, a dual-laminate construction usually will.</p>
    </div>
    <div class="split">
      <div class="reveal">
        <h3>What is dual laminate?</h3>
        <p>A hybrid construction: a strong fibreglass composite structure on the outside and a specialised thermoplastic liner on the inside. The liner is chosen to match the specific chemistry for maximum service life.</p>
        {checks(["Mechanical strength of an FRP composite exterior", "Corrosion-resistant thermoplastic interior for hazardous chemistry", "High-temperature and abrasion resistance", "Resists leaching agents and chemical attack", "Suitable for high-purity processes"])}
        <p class="mb-0"><strong>Liner options:</strong> PVC · CPVC · PP · HDPE and others, selected per chemical. See our <a href="technical.html#downloads">thermoplastic corrosion chart</a>.</p>
      </div>
      <div class="grid grid-2 reveal reveal-d1" style="grid-template-columns:1fr 1fr">
        {media("assets/images/products/dual-laminate.jpg", "Dual laminate section", "media--tall")}
        {media("assets/images/products/liner-options.jpg", "Liner options", "media--tall")}
      </div>
    </div>
  </div>
</section>
"""


def related(path):
    others = [p for p in PRODUCTS if p[0] != path][:3]
    cards = "".join(f"""<a class="card reveal reveal-d{i}" href="{s}">
        {media(f"assets/images/products/{img}.jpg", t)}
        <div class="card-body"><h3>{t}</h3><p>{d}</p><span class="card-link">Learn more {I['arrow']}</span></div>
      </a>""" for i, (s, t, d, ic, img) in enumerate(others))
    return f"""<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Explore more</span><h2>Related products</h2></div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
"""
