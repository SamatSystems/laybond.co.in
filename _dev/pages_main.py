from layout import *

INDUSTRIES = [
  ("bolt", "Power Stations", "DM plant acid/alkali storage, cooling-water treatment, scrubbers"),
  ("oil", "Refineries & Oil and Gas", "Chemical storage, underground fuel piping, linings"),
  ("cup", "Food & Beverage", "Food-grade tanks and silos, process piping (Coca-Cola supplier for 23+ years)"),
  ("car", "Automobile", "Pickling and plating lines, effluent treatment, fume extraction"),
  ("flask", "Petrochemical & Chemical", "Acid handling systems, process vessels, dual-laminate equipment"),
  ("pill", "Pharmaceutical", "High-purity dual-laminate tanks, solvent and acid storage"),
  ("thread", "Textiles", "Dye-house chemical tanks, bleach and caustic storage, ETP"),
  ("leather", "Leather & Tannery", "Chrome and acid tanks, effluent pits, corrosion-proof linings"),
  ("metal", "Metal Refining & Finishing", "Electroplating, pickling, acid fume scrubbers"),
  ("water", "Water & Wastewater", "Hypochlorite dosing, clarifier linings, raw-water and outfall piping"),
  ("factory", "Steel & Pulp/Paper", "Scrubbers for kilns and liquor recovery, storage tanks"),
  ("leaf", "Fertilizer Plants", "Acid gas scrubbers, ducting, corrosion-resistant storage"),
]


def home():
    path = "index.html"
    prod_cards = "".join(f"""<a class="card reveal reveal-d{i % 3}" href="{s}">
        {media(f"assets/images/products/{img}.jpg", t)}
        <div class="card-body"><h3>{t}</h3><p>{d}</p><span class="card-link">Explore {I['arrow']}</span></div>
      </a>""" for i, (s, t, d, ic, img) in enumerate(PRODUCTS))
    feats = [
      ("feather", "Light Weight", "As a composite, FRP offers a strength-to-weight ratio far higher than metals, so it is easier to transport, lift and install."),
      ("drop", "Corrosion Resistant", "Resin systems are formulated for the specific chemical, so FRP thrives in corrosive atmospheres where steel fails."),
      ("temp", "Temperature Resistant", "Suitable for hot or cold extremes and every kind of weather, indoors or outdoors."),
      ("rupee", "Economical", "High strength and corrosion resistance give an average service life of over 35 years with minimal upkeep."),
      ("ruler", "Design Freedom", "Any shape, size or finish, engineered to the relevant international standards."),
      ("wrench", "Easily Repaired", "Repairs, modifications and additional fittings can be carried out on site."),
    ]
    feat_html = "".join(f"""<div class="feature reveal reveal-d{i % 3}"><div class="feature-icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p></div>""" for i, (ic, t, d) in enumerate(feats))
    ind = "".join(f'<div class="industry reveal">{I[ic]}<span>{t}</span></div>' for ic, t, _ in INDUSTRIES[:8])
    marquee_items = ["FRP Tanks", "Acid Handling", "Fume Scrubbers", "FRP Piping", "Dual Laminate", "Tank Linings", "Agitators", "Motor Guards", "Ducting &amp; Stacks", "Steel Fabrication"]
    mq = "".join(f"<span>{x}</span>" for x in marquee_items * 2)
    html = head("Laybond | FRP Tanks, Piping, Scrubbers & Acid Handling Systems – Tamil Nadu",
                "Laybond Pipings & Equipments designs and builds FRP and dual-laminate thermoplastic tanks, acid handling systems, fume scrubbers, pipes and corrosion-proof linings. ISO 9001, since 1994.", path)
    html += header(path)
    html += f"""<section class="hero">
  <div class="media hero-media" data-label="">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/images/hero/home-hero.jpg">
      <source src="assets/videos/hero.mp4" type="video/mp4" onerror="this.parentNode.remove()">
    </video>
    <img src="assets/images/hero/home-hero.jpg" alt="" fetchpriority="high" style="z-index:-1" onerror="this.remove()">
  </div>
  <div class="container">
    <h1>Mission against <em>corrosion</em></h1>
    <p class="lead">The widest range of composite (FRP) and dual-laminate thermoplastic tanks, piping, scrubbers and process equipment. We handle it turnkey, from design and specification through fabrication, delivery and installation.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="contact.html">Request a Quote {I['arrow']}</a>
      <a class="btn btn--ghost" href="#products">Explore Products</a>
    </div>
    <ul class="hero-trust" aria-label="Credentials">
      <li>{I['award']}<span><strong>ISO 9001</strong> Certified</span></li>
      <li>{I['shield']}<span><strong>Since 1994</strong> 30+ years</span></li>
      <li>{I['pin']}<span><strong>SIPCOT</strong> Pudukkottai, TN</span></li>
    </ul>
    <div class="hero-stats">
      <div><strong>{30}+</strong><span>Years of FRP expertise</span></div>
      <div><strong>1–300<small style="font-size:.5em"> m³</small></strong><span>Tank capacity range</span></div>
      <div><strong>25–1500<small style="font-size:.5em"> mm</small></strong><span>FRP pipe diameters</span></div>
      <div><strong>35+</strong><span>Years average service life</span></div>
    </div>
  </div>
  <span class="scroll-cue">Scroll</span>
</section>

<section class="section section--white">
  <div class="container">
    <div class="split split--wide-left">
      <div class="reveal">
        <span class="eyebrow">Total composite engineering</span>
        <h2>Engineered to stand up to the world's most aggressive chemicals</h2>
      </div>
      <div class="reveal reveal-d1">
        <p class="lead">Laybond is a total composite engineering company. We design, fabricate and install FRP and dual-laminate equipment for power, refining, food &amp; beverage, pharma, textiles, tanneries, metal finishing and more.</p>
        <p>From a single dosing tank to a complete acid-handling and fume-scrubbing installation, we assist in every phase: design, specification, fabrication, delivery, installation and after-sales service.</p>
        <a class="card-link" href="about.html">Our story {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="products">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What we build</span>
      <h2>Products &amp; solutions</h2>
      <p class="lead">Expertise across acid dosing, handling, pumping and fume scrubbing, plus the tanks, piping and linings that hold it all together.</p>
    </div>
    <div class="grid grid-3">{prod_cards}</div>
  </div>
</section>

<section class="section section--dark" style="padding:36px 0">
  <div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}</div></div>
</section>

<section class="section section--darker">
  <div class="container">
    <div class="split" style="align-items:end;margin-bottom:clamp(36px,5vw,60px)">
      <div class="reveal">
        <span class="eyebrow">Why fibreglass?</span>
        <h2>Lighter than steel.<br>Outlasts it too.</h2>
      </div>
      <p class="lead reveal reveal-d1">Fibreglass is lightweight, economical, corrosion-resistant, flexible and extremely strong. In chemical service it consistently outperforms steel and aluminium.</p>
    </div>
    <div class="grid grid-3">{feat_html}</div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="img-stack reveal">
        {media("assets/images/about/factory-exterior.jpg", "Laybond factory – SIPCOT Pudukkottai", "media--tall")}
        {media("assets/images/about/workshop.jpg", "FRP workshop")}
        <div class="exp-badge"><strong>1994</strong><span>Established</span></div>
      </div>
      <div class="reveal reveal-d1">
        <span class="eyebrow">About Laybond</span>
        <h2>From one technician to a full-scale FRP works</h2>
        <p class="lead">Laybond began in 1994 in a rented shed in Ambattur, Chennai, with one FRP technician and a commitment to quality.</p>
        <p>Today we operate from an 8,000 sq ft manufacturing facility on more than an acre at SIPCOT Industrial Complex, Pudukkottai, allotted by the Government of Tamil Nadu. Our team of 50+ people serves industries across India, and we train local youth in FRP fabrication skills.</p>
        {checks(["ISO 9001 certified quality system", "Designed to BS 4994, ASTM D-3299 / D-4097 &amp; ASME RTP-1", "Factory-built tanks up to 50 m³; larger tanks built on site", "Installation, commissioning, maintenance &amp; emergency service"])}
        <a class="btn btn--dark" href="about.html">More about us {I['arrow']}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split" style="align-items:end;margin-bottom:clamp(36px,5vw,56px)">
      <div class="reveal"><span class="eyebrow">Industries we serve</span><h2>Trusted across process industries</h2></div>
      <p class="lead reveal reveal-d1">Coca-Cola has relied on Laybond FRP piping for over 23 years. Our equipment is also running at power stations, refineries and chemical plants across India.</p>
    </div>
    <div class="grid grid-4">{ind}</div>
    <p class="mt-2"><a class="card-link" href="industries.html">See all industries &amp; applications {I['arrow']}</a></p>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="split" style="align-items:end;margin-bottom:clamp(36px,5vw,56px)">
      <div class="reveal"><span class="eyebrow">Projects</span><h2>Recent work</h2></div>
      <div class="reveal reveal-d1" style="justify-self:start"><a class="btn btn--outline" href="gallery.html">View full gallery {I['arrow']}</a></div>
    </div>
    <div class="gallery-grid" id="gallery-grid" data-limit="6"></div>
  </div>
</section>
{lightbox()}
{cta()}
"""
    html += footer('<script src="assets/js/gallery-data.js"></script>\n')
    return html


def lightbox():
    return f"""<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Media viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close">{I['close']}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous">{I['left']}</button>
  <figure><div id="lb-stage"></div><figcaption id="lb-cap"></figcaption></figure>
  <button class="lb-btn lb-next" type="button" aria-label="Next">{I['right']}</button>
</div>"""


def about():
    path = "about.html"
    tl = [
      ("1992", "Where it started", "Victor, our founder and CEO, begins his career at an FRP tank manufacturer in Chennai."),
      ("1994", "Laybond is born", "Victor starts Laybond Pipings &amp; Equipments with a single FRP technician, building tanks in a rented shed in Ambattur Industrial Area, Chennai."),
      ("2003", "First dedicated facility", "We move to a new 3,200 sq ft facility in Ambattur SIDCO Industrial Estate, Chennai."),
      ("2009", "SIPCOT Pudukkottai", "We relocate to a site at SIPCOT Industrial Complex, Pudukkottai, allotted by the Government of Tamil Nadu: 8,000 sq ft of manufacturing space on more than an acre."),
      ("Today", "50+ people, pan-India projects", "A growing team serving power, process and manufacturing industries, and training local youth in FRP skills."),
    ]
    tl_html = "".join(f'<div class="timeline-item reveal"><div class="timeline-year">{y}</div><h3>{t}</h3><p>{d}</p></div>' for y, t, d in tl)
    ind = "".join(f'<div class="industry reveal">{I[ic]}<span>{t}</span></div>' for ic, t, _ in INDUSTRIES[:10])
    html = head("About Laybond | FRP Manufacturer Since 1994 – SIPCOT Pudukkottai",
                "Founded in 1994, Laybond Pipings & Equipments manufactures FRP and dual-laminate tanks, piping and scrubbers from its ISO 9001 facility at SIPCOT, Pudukkottai.", path)
    html += header(path)
    html += page_hero("About Laybond", "Three decades of composite engineering: designing, fabricating and installing corrosion-resistant equipment for India's process industries.",
                      [("About", None)], "assets/images/hero/about-hero.jpg", "About hero", "Since 1994")
    html += f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Who we are</span>
        <h2>A total composite engineering company</h2>
        <p class="lead">Laybond designs, fabricates and supplies FRP and dual-laminate thermoplastic products, and takes on complete turnkey projects.</p>
        <p>We manufacture contact-moulded tanks from 1 m³ to 300 m³ for chemical processing, food processing, iron &amp; steel, wastewater, metal finishing, bulk storage, pharmaceutical and other applications. Tanks up to 50 m³ are built in our factory; larger tanks are fabricated on site.</p>
        <p>We build cone-bottom, dish-bottom, flat-bottom, slope-bottom, horizontal and vertical tanks, designed to <strong>BS 4994-1987</strong>, <strong>ASTM D-3299</strong> and <strong>D-4097</strong>, with <strong>ASME RTP-1</strong> design-by-rules available on request.</p>
      </div>
      <div class="reveal reveal-d1">
        {media("assets/images/about/factory.jpg", "Laybond factory", "media--tall")}
      </div>
    </div>
  </div>
</section>

<section class="section section--darker">
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="reveal" style="position:sticky;top:120px">
        <span class="eyebrow">Our journey</span>
        <h2>How it happened</h2>
        <p class="lead">From a single technician in a rented shed to a government-allotted manufacturing campus.</p>
        <div class="stats mt-2" style="grid-template-columns:1fr 1fr">
          <div class="stat"><strong data-count="8000">8,000</strong><span>sq ft manufacturing</span></div>
          <div class="stat"><strong>50<small>+</small></strong><span>skilled people</span></div>
        </div>
      </div>
      <div class="timeline">{tl_html}</div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="grid grid-3">
      <div class="feature reveal"><div class="feature-icon">{I['shield']}</div><h3>Our vision</h3><p>To be India's most trusted partner against corrosion, delivering composite equipment that outlasts the alternatives and protects people, plant and environment.</p></div>
      <div class="feature reveal reveal-d1"><div class="feature-icon">{I['award']}</div><h3>Quality first</h3><p>An ISO 9001 quality system, international design standards and a resin-rich, male-mould construction for every tank we build.</p></div>
      <div class="feature reveal reveal-d2"><div class="feature-icon">{I['wrench']}</div><h3>Turnkey service</h3><p>Design, specification, fabrication, delivery, installation, commissioning, maintenance, repairs and emergency service, all from one team.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Projects, consultants &amp; clients</span><h2>Who we work with</h2>
      <p class="lead">Our equipment is at work in power stations, refineries, food &amp; beverage plants, automotive, petrochemical, pharmaceutical, textile, oil &amp; gas, leather &amp; tannery and metal refining operations.</p></div>
    <div class="grid grid-4">{ind}</div>
    <div class="clients-wall mt-3 reveal"><img src="assets/images/clients/laybond-clients.jpg" alt="Laybond clients include Lanxess, NCC, JSW, Vedanta, Nalco, TVS Tyres, Nippon Paint, Punj Lloyd, Chettinad Cement, Tagros and others" loading="lazy" onerror="this.parentNode.remove()"></div>
  </div>
</section>
{cta("Let's build something that lasts", "Talk to our engineering team about your next tank, scrubber, piping or lining project.")}
"""
    html += footer()
    return html


def industries():
    path = "industries.html"
    cards = "".join(f'<div class="feature reveal reveal-d{i % 3}"><div class="feature-icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(INDUSTRIES))
    apps = ["Acids", "Caustics", "Solvents", "Petroleum products", "Chemicals", "Water treatment plants", "Effluent treatment plants", "Electroplating", "Brine solutions",
            "Pollution control equipment", "Food processing", "Pickling lines", "Cooling towers", "Fire protection", "Underground fuel piping", "Clarifiers &amp; aeration tanks", "Neutralisation pits", "Dyke walls"]
    html = head("Industries Served | Laybond FRP Equipment", "Laybond FRP and dual-laminate equipment serves power, refinery, food & beverage, pharma, textile, tannery, metal finishing, water treatment and fertilizer industries.", path)
    html += header(path)
    html += page_hero("Industries we serve", "Wherever there are aggressive chemicals, corrosive fumes or hard-working water, there's a place for Laybond composite equipment.",
                      [("Industries", None)], "assets/images/hero/industries-hero.jpg", "Industries hero", "Applications")
    html += f"""<section class="section section--darker">
  <div class="container">
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Applications</span><h2>Typical services</h2><p class="lead">A snapshot of the media and duties our equipment handles every day.</p></div>
      <div class="reveal reveal-d1">{chips(apps)}</div>
    </div>
  </div>
</section>
{cta()}
"""
    html += footer()
    return html


def gallery():
    path = "gallery.html"
    filters = [("all", "All"), ("tanks", "Tanks &amp; Vessels"), ("acid", "Acid Handling"), ("scrubbers", "Scrubbers"), ("piping", "Piping"), ("linings", "Linings"), ("fabrication", "Fabrication"), ("site", "Site Work")]  # add ("video", "Videos") once videos exist
    fh = "".join(f'<button type="button" class="filter{" is-active" if k == "all" else ""}" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button>' for k, t in filters)
    html = head("Project Gallery | Laybond FRP Tanks, Scrubbers & Piping", "Photos and videos of Laybond FRP tanks, acid handling systems, scrubbers, piping, linings and fabrication projects.", path)
    html += header(path)
    html += page_hero("Project gallery", "Photos and videos from our factory floor and project sites across India.", [("Gallery", None)], "assets/images/hero/gallery-hero.jpg", "Gallery hero", "Our work")
    html += f"""<section class="section">
  <div class="container">
    <div class="filters" role="toolbar" aria-label="Filter gallery">{fh}</div>
    <div class="gallery-grid" id="gallery-grid"></div>
    <noscript><p>Please enable JavaScript to view the gallery.</p></noscript>
  </div>
</section>
{lightbox()}
{cta("Like what you see?", "We can build it for your plant too. Share your requirement and we will get back within one working day.")}
"""
    html += footer('<script src="assets/js/gallery-data.js"></script>\n')
    return html


def contact():
    path = "contact.html"
    opts = "".join(f'<option value="{t}">{t}</option>' for _, t, *_ in PRODUCTS)
    html = head("Contact Laybond | Get a Quote for FRP Tanks, Piping & Scrubbers", "Contact Laybond Pipings & Equipments, 14-B SIPCOT Industrial Complex, Pudukkottai. Call +91 98400 32218 or email sales@laybond.co.in for a quote.", path)
    html += header(path)
    html += page_hero("Let's talk", "Send us your requirement (chemical, concentration, temperature, capacity) and our engineers will respond with a solution and quote.",
                      [("Contact", None)], "assets/images/hero/contact-hero.jpg", "Contact hero", "Contact &amp; quotes")
    html += f"""<section class="section">
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="form-card reveal">
        <h2 style="font-size:2rem">Request a quote</h2>
        <p class="form-note" style="margin-bottom:24px">Fields marked <span style="color:#d14343">*</span> are required. We usually reply within one working day.</p>
        <form class="form" id="contact-form" action="contact.php" method="post" novalidate>
          <div class="form-row">
            <div class="field"><label for="f-name">Your name <span class="req">*</span></label><input id="f-name" name="name" type="text" autocomplete="name" required><div class="field-error">Please enter your name.</div></div>
            <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="f-phone">Phone <span class="req">*</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required><div class="field-error">Please enter a valid phone number.</div></div>
            <div class="field"><label for="f-email">Email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required><div class="field-error">Please enter a valid email.</div></div>
          </div>
          <div class="field"><label for="f-product">Product of interest</label>
            <select id="f-product" name="product"><option value="">Select a product…</option>{opts}<option value="Other / Not sure">Other / Not sure</option></select></div>
          <div class="field"><label for="f-msg">Your requirement <span class="req">*</span></label><textarea id="f-msg" name="message" required placeholder="e.g. 20 m³ storage tank for 33% HCl, ambient temperature, with fume scrubber"></textarea><div class="field-error">Please tell us a little about your requirement.</div></div>
          <div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
          <input type="hidden" name="ts" value="">
          <div class="form-status" role="status" aria-live="polite"></div>
          <div><button class="btn btn--primary" type="submit">Send enquiry {I['arrow']}</button></div>
        </form>
      </div>
      <div class="reveal reveal-d1 contact-card">
        <h2 style="font-size:2rem">Head office &amp; works</h2>
        <div class="contact-item"><span class="contact-icon">{I['pin']}</span><div><h4>Address</h4><address>{ADDRESS_HTML}</address></div></div>
        <div class="contact-item"><span class="contact-icon">{I['phone']}</span><div><h4>Phone</h4><a href="tel:{PHONE1_RAW}">{PHONE1}</a></div></div>
        <div class="contact-item"><span class="contact-icon">{I['mail']}</span><div><h4>Email</h4><a href="mailto:{EMAIL1}">{EMAIL1}</a><a href="mailto:{EMAIL2}">{EMAIL2}</a></div></div>
        <div class="contact-item"><span class="contact-icon">{I['wa']}</span><div><h4>WhatsApp</h4><a href="{WA}your%20requirement" target="_blank" rel="noopener">Chat with us on WhatsApp</a></div></div>
        <div class="contact-item"><span class="contact-icon">{I['clock']}</span><div><h4>Working hours</h4><span class="contact-text">Mon – Sat, 9:00 AM – 6:00 PM</span></div></div>
      </div>
    </div>
  </div>
</section>
<section class="section section--tight section--white">
  <div class="container">
    <iframe class="map-embed" title="Map – Laybond, SIPCOT Industrial Complex, Pudukkottai" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://www.google.com/maps?q=SIPCOT+Industrial+Complex,+Pudukkottai,+Tamil+Nadu+622002&amp;output=embed"></iframe>
  </div>
</section>
"""
    html += footer()
    return html


def warranty():
    path = "warranty.html"
    html = head("Warranty | Laybond Pipings & Equipments", "Warranty terms for Laybond FRP and dual-laminate products.", path)
    html += header(path)
    html += page_hero("Warranty", "Terms covering Laybond-manufactured FRP and dual-laminate products.", [("Warranty", None)], "assets/images/hero/technical-hero.jpg", "Warranty", None)
    html += """<section class="section section--white"><div class="container"><div class="prose">
<h2 style="margin-top:0">A. Standard warranty</h2>
<p>The Seller warrants that goods manufactured by it will conform to the Seller's applicable specifications and will be free from defects in material and workmanship. This warranty is given in lieu of all other warranties, express or implied, including any implied warranty of merchantability or fitness for a particular purpose.</p>
<h2>B. Goods made to the Buyer's specifications</h2>
<p>Where goods are manufactured to the Buyer's specifications and those specifications have been accepted in writing by the Seller, the Seller warrants only that the goods will conform to those specifications and be free from defects in material and workmanship.</p>
<h2>C. Goods not manufactured by the Seller</h2>
<p>The Seller gives no warranty on goods it did not manufacture. Such goods carry only the warranty, if any, of their original manufacturer.</p>
<div class="note mt-2">This is a plain-language summary of the warranty previously published on our website. For the binding terms applicable to your order, please refer to your quotation and purchase order, or <a href="contact.html">contact us</a>.</div>
</div></div></section>
"""
    html += footer()
    return html


def not_found():
    path = "404.html"
    html = head("Page not found | Laybond", "The page you are looking for could not be found.", path)
    html += header(path, solid=True)
    html += f"""<section class="not-found"><div><div class="big">404</div><h2>Page not found</h2><p style="color:var(--steel-300)">The page may have moved in our website redesign.</p>
<div class="btn-row" style="justify-content:center;margin-top:24px"><a class="btn btn--primary" href="index.html">Go to homepage {I['arrow']}</a><a class="btn btn--ghost" href="contact.html">Contact us</a></div></div></section>
"""
    html += footer()
    # 404 can be served from any depth; use absolute asset paths
    return html.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('href="index.html"', 'href="/"').replace('.html"', '.html"')


def thank_you():
    path = "thank-you.html"
    html = head("Thank you | Laybond", "Thank you for contacting Laybond.", path)
    html = html.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"')
    html += header(path, solid=True)
    html += f"""<section class="not-found"><div><div class="feature-icon" style="margin:0 auto 24px;width:84px;height:84px;border-radius:50%">{I['check']}</div><h1 style="font-size:clamp(2.4rem,6vw,4rem)">Thank you!</h1>
<p style="color:var(--steel-300);max-width:48ch;margin:0 auto">Your enquiry has reached our sales team. We'll get back to you within one working day. For anything urgent, call <a href="tel:{PHONE1_RAW}">{PHONE1}</a>.</p>
<div class="btn-row" style="justify-content:center;margin-top:28px"><a class="btn btn--primary" href="index.html">Back to homepage {I['arrow']}</a><a class="btn btn--ghost" href="gallery.html">View our work</a></div></div></section>
"""
    html += footer()
    return html
