import os, sys
from layout import SITE
import pages_main as M, pages_products as P
OUT = sys.argv[1]
pages = {
 "index.html": M.home, "about.html": M.about, "industries.html": M.industries, "gallery.html": M.gallery,
 "contact.html": M.contact, "warranty.html": M.warranty, "404.html": M.not_found, "thank-you.html": M.thank_you,
 "chemical-handling-systems.html": P.acid, "frp-tanks.html": P.tanks, "fume-extraction.html": P.scrubbers,
 "pipe-fittings.html": P.pipes, "corrosion-proof-linings.html": P.linings, "steel-fabrications.html": P.fabrication,
 "technical.html": P.technical,
}
for name, fn in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(fn())
    print("wrote", name)
urls = [p for p in pages if p not in ("404.html", "thank-you.html")]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        pr = "1.0" if u == "index.html" else "0.8"
        f.write(f"  <url><loc>{loc}</loc><lastmod>2026-11-15</lastmod><priority>{pr}</priority></url>\n")
    f.write("</urlset>\n")
print("wrote sitemap.xml")
