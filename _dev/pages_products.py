from layout import *


def product_page(path, title, desc, hero_title, hero_lead, eyebrow, hero_img, body, product_name):
    html = head(title, desc, path)
    html += header(path)
    html += page_hero(hero_title, hero_lead, [("Products", None), (product_name, None)], hero_img, product_name, eyebrow)
    html += product_strip(path)
    html += body
    html += cta(product=product_name.replace(" ", "+").replace("&amp;", "%26"))
    html += related(path)
    html += footer()
    return html


def chem_table(rows):
    return '<div class="table-wrap"><table class="spec-table"><thead><tr><th>Parameter</th><th>Specification</th></tr></thead><tbody>' + \
        "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</tbody></table></div>"


def acid():
    path = "chemical-handling-systems.html"
    chems = [
      ("HCl", "Hydrochloric acid handling system", "Controlling a chemical and its fumes",
       "Also known as muriatic acid. Its very low pH makes it highly corrosive, and its toxic fumes attack surrounding equipment and can be fatal if inhaled. Fuming also makes maintenance difficult. The answer is a corrosion-resistant tank tied into a fume scrubber.",
       ["Very low pH; highly corrosive", "Toxic fumes that degrade nearby equipment", "Fumes can be fatal", "Maintenance complicated by fuming"],
       [("Concentration", "≥ 37% HCl"), ("Specific gravity", "1.16"), ("Tank material", "FRP – vinyl ester (FRVE)"), ("Gaskets", "Neoprene / EPDM"), ("Fasteners", "SS 316")]),
      ("NaOCl", "Sodium hypochlorite handling system", "An aggressive oxidiser that presents a major storage challenge",
       "Widely used to disinfect drinking water and wastewater. Three factors make storage difficult: UV degradation, transition metals (nickel, iron, copper) that cause off-gassing, and its strong oxidising nature. Our tank systems are designed to meet NSF/ANSI Standard 61.",
       ["Degrades under UV light", "Transition metals (Ni, Fe, Cu) cause off-gassing", "Strong oxidiser"],
       [("Concentration", "9 – 15% NaOCl"), ("Specific gravity", "1.20"), ("Tank material", "CPVC / PVC / PP dual laminate"), ("Gaskets", "PTFE (Teflon) / Viton / EPDM"), ("Fasteners", "SS 316")]),
      ("NaOH", "Sodium hydroxide (caustic soda) system", "Defying a chemical that “finds” leaks",
       "Used for pH control and in countless manufacturing processes. Caustic soda is notorious for finding any weakness in a joint. It is extremely corrosive to body tissue, toxic if swallowed, and crystallises if the temperature drops.",
       ["Prone to finding and causing leaks", "Extremely corrosive to body tissue", "Toxic if swallowed", "Crystallises at low temperatures"],
       [("Concentration", "50% NaOH"), ("Specific gravity", "1.52"), ("Tank material", "CPVC / PVC dual laminate"), ("Gaskets", "EPDM"), ("Fasteners", "SS 316")]),
      ("H<sub>2</sub>SO<sub>4</sub>", "Sulphuric acid handling system", "Challenging a tank's strength and design safety",
       "Very heavy, which puts high loads on tank walls and supports. Diluting it is strongly exothermic: water added to concentrated acid can cause aerosols or even an explosion. It generates hydrogen gas in contact with metals and causes serious burns.",
       ["Very high density; high structural loads", "Violently exothermic on dilution", "Hydrogen gas risk with metals", "Causes severe burns"],
       [("Concentration", "≥ 93% H<sub>2</sub>SO<sub>4</sub>"), ("Specific gravity", "1.85"), ("Tank material", "MS / CPVC"), ("Gaskets", "Viton®"), ("Fasteners", "GI / SS 316")]),
    ]
    blocks = ""
    for i, (f, t, sub, d, haz, rows) in enumerate(chems):
        blocks += f"""<article class="chem reveal" id="chem-{i+1}">
      <div class="split" style="align-items:start">
        <div>
          <div class="chem-formula">{f}</div>
          <h3>{t}</h3>
          <p class="chem-sub">{sub}</p>
          <p>{d}</p>
          <div class="hazards"><h4>Key hazards</h4>{checks(haz)}</div>
        </div>
        <div>{chem_table(rows)}</div>
      </div>
    </article>
"""
    acc = ["Secondary containment", "Acid-proof lining", "Fume scrubbers / breathers", "Transfer &amp; dosing pumps", "Day tanks", "Interconnecting pipes &amp; valves", "Ladders &amp; railings", "Level indicators", "Safety showers", "Motor covers"]
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Complete chemical storage &amp; dosing systems</h2>
        <p class="lead">We design and build complete acid and chemical handling systems from 1 m³ to 300 m³. Tanks up to 50 m³ are shop-fabricated; larger tanks are built on site.</p>
        <p>Each system is engineered around the specific chemical, concentration and temperature, from tank material, gaskets and fasteners to the scrubbers, pumps and safety equipment around it.</p>
        <dl class="spec-list mt-2">
          <div><dt>Capacity</dt><dd>1 – 300 m³</dd></div>
          <div><dt>Shop-built up to</dt><dd>50 m³</dd></div>
        </dl>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/acid-handling.jpg", "Acid handling system", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Chemistry-specific design</span><h2>Systems by chemical</h2><p class="lead">Every chemical presents a different challenge. Here is how we engineer for four of the most common.</p></div>
    {blocks}
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Accessories</span><h2>Everything around the tank</h2><p class="lead">We supply and integrate the complete system for safe, compliant chemical handling.</p>{chips(acc)}</div>
      <div class="grid reveal reveal-d1" style="grid-template-columns:1fr 1fr">
        {media("assets/images/products/acid-accessories-1.jpg", "Dosing skid", "media--tall")}
        {media("assets/images/products/acid-accessories-2.jpg", "Containment &amp; scrubber", "media--tall")}
      </div>
    </div>
  </div>
</section>
{DUAL_LAMINATE}"""
    return product_page(path, "Acid Handling Systems | HCl, NaOCl, NaOH & H2SO4 Storage – Laybond",
        "Complete FRP and dual-laminate acid handling and chemical dosing systems from 1 to 300 m³ for hydrochloric acid, sodium hypochlorite, caustic soda and sulphuric acid.",
        "Acid handling systems", "Safe storage, dosing and fume control for the most aggressive chemicals: hydrochloric acid, hypochlorite, caustic soda and sulphuric acid.",
        "Chemical handling", "assets/images/hero/acid-hero.jpg", body, "Acid Handling Systems")


def tanks():
    path = "frp-tanks.html"
    tops = [("Closed dome top", "Our most requested top. ASME flanged-and-dished design with a standard top manhole and loose cover."),
            ("Closed flat top", "Fixed flat surface where headspace is limited, agitator rails are required, or a walking surface is needed."),
            ("Open top, 90° flanged rim", "For a flat cover, agitator rails or full access to the tank."),
            ("Open top, Type II rim", "The most economical option when no cover or rails are needed.")]
    types = [
      ("Flat bottom", "Most common", "flat-bottom", "Our most common design, built to ASTM D-3299 or D-4097. Requires a flat, fully supporting foundation.", []),
      ("Slope bottom", "Better drainage", "slope-bottom", "Available with internal or external slope. Internal slope uses a 1″ minor and bottom core with a standard pitch of ¼″ per foot. External slope requires a customer-supplied sloped pad.", []),
      ("Cone bottom", "Complete drainage", "cone-bottom", "Provides complete drainage with a standard 90° apex angle. Supplied with a primed carbon-steel pipe leg stand, floor plates and 18″ clearance.",
       ["Leg options: painted carbon steel, FRP, SS 304 or SS 316", "FRP skirt available"]),
      ("Dish bottom", "Head pressure at outlet", "dish-bottom", "Near-complete drainage with ASME flanged-and-dished (torispherical) heads, chosen when head pressure is needed at the outlet. 18″ leg stand standard.",
       ["Leg options: painted carbon steel, FRP, SS 304 or SS 316"]),
      ("Horizontal", "Low headroom", "horizontal", "Ideal where floor space is available but headroom is limited. ASME flanged-and-dished ends, minimum two primed carbon-steel saddles with 12″ clearance.",
       ["Saddle options: painted carbon steel, FRP, SS 304 or SS 316"]),
    ]
    tops_html = "".join(f"<li><strong>{t}:</strong> {d}</li>" for t, d in tops)
    acc = ""
    for i, (t, tag, img, d, extra) in enumerate(types):
        top_section = "" if t == "Horizontal" else f'<h4 class="mt-2">Top options</h4><ul class="check-list">{tops_html}</ul>'
        acc += f"""<div class="acc-item{' is-open' if i == 0 else ''} reveal">
      <button class="acc-btn" type="button" aria-expanded="{'true' if i == 0 else 'false'}"><h3>{t}</h3><span class="acc-tag">{tag}</span><span class="acc-plus" aria-hidden="true"></span></button>
      <div class="acc-panel"><div><div class="acc-content">
        {media(f"assets/images/tanks/{img}.jpg", t + " tank")}
        <div><p>{d}</p>{checks(extra) if extra else ""}{top_section}</div>
      </div></div></div>
    </div>"""
    apps = ["Acids", "Caustics", "Solvents", "Petroleum products", "Chemicals", "Water treatment plants", "Electroplating", "Brine solutions", "Pollution control equipment", "Food processing"]
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>FRP storage tanks built for aggressive chemicals</h2>
        <p class="lead">Laybond FRP tanks safely store bleach, sodium hydroxide, sulphuric acid, hydrochloric acid and many other corrosive and caustic chemicals across a wide range of industries.</p>
        <p>Tanks are engineered to <strong>BS 4994-1987</strong>. Most are cylindrical, but rectangular and custom shapes are available.</p>
        <dl class="spec-list mt-2">
          <div><dt>Capacity</dt><dd>1 – 300 m³</dd></div>
          <div><dt>Design code</dt><dd>BS 4994 / ASTM D-3299</dd></div>
        </dl>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/frp-tanks.jpg", "FRP storage tanks", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Service</span><h2>More than a tank</h2></div>
    <div class="grid grid-4">
      <div class="feature reveal"><div class="feature-icon">{I['ruler']}</div><h3>Custom fittings</h3><p>Flanged nozzles, threaded couplings, access &amp; view ports, level gauges, internal baffles, agitator supports, ladders, platforms and handrails.</p></div>
      <div class="feature reveal reveal-d1"><div class="feature-icon">{I['feather']}</div><h3>Lifting &amp; handling</h3><p>Lifting lugs and handling arrangements designed in, plus competitive shipping rates.</p></div>
      <div class="feature reveal reveal-d2"><div class="feature-icon">{I['wrench']}</div><h3>On-site service</h3><p>Installation, commissioning, maintenance, repairs and modifications.</p></div>
      <div class="feature reveal reveal-d3"><div class="feature-icon">{I['clock']}</div><h3>Emergency support</h3><p>Rapid-response emergency service to keep your plant running.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Configurations</span><h2>Tank types</h2><p class="lead">Choose the bottom and top configuration that suits your process, drainage and site constraints.</p></div>
    <div class="accordion">{acc}</div>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Applications</span><h2>Where our tanks work</h2>{chips(apps)}</div>
      <div class="grid reveal reveal-d1" style="grid-template-columns:1fr 1fr">
        {media("assets/images/products/storage-tanks-1.jpg", "Storage tank farm", "media--tall")}
        {media("assets/images/products/storage-tanks-2.jpg", "Process vessel", "media--tall")}
      </div>
    </div>
  </div>
</section>
{DUAL_LAMINATE}"""
    return product_page(path, "FRP Storage Tanks & Vessels | Cone, Dish, Flat, Horizontal – Laybond",
        "FRP chemical storage tanks and vessels to BS 4994 and ASTM D-3299/D-4097: flat, slope, cone, dish-bottom and horizontal tanks, 1 to 300 m³, with custom fittings and on-site service.",
        "Storage tanks &amp; vessels", "FRP and dual-laminate tanks for corrosive and caustic chemicals, engineered to international standards and built to last 35+ years.",
        "Tanks &amp; vessels", "assets/images/hero/tanks-hero.jpg", body, "Tanks &amp; Vessels")


def scrubbers():
    path = "fume-extraction.html"
    apps = ["Acid plants", "Electroplating", "Power plants", "Pulp &amp; paper (Kraft process)", "Liquor recovery", "Dissolving tanks", "Lime kilns &amp; shakers", "Fertilizer plants", "Paper grinding", "Steel mills"]
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Air pollution control, engineered in FRP</h2>
        <p class="lead">We design, fabricate and install acid gas scrubbers for a wide range of industries, built to client requirements and industry standards.</p>
        <p>Our range covers fume scrubbers, ducts for corrosive gases, exhaust fans and custom fittings: a complete fume-extraction system from hood to stack.</p>
        <h3 class="mt-2">Ducts &amp; stacks</h3>
        <p>Ductwork and fume stacks up to 2,000 mm diameter and larger, available in fire-retardant and/or heat-resistant constructions.</p>
        <h3>Dampers</h3>
        <p class="mb-0">Proprietary flow-control and isolation dampers.</p>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/scrubbers.jpg", "Fume scrubber", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section section--darker">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Performance</span><h2>Scrubber specifications</h2></div>
    <dl class="spec-list reveal">
      <div><dt>Gas handling capacity</dt><dd>1,500 – 70,000 cfm</dd></div>
      <div><dt>Pressure drop</dt><dd>5″ – 9″ w.c.</dd></div>
      <div><dt>Particulate removal (≥ 2 µm)</dt><dd>97% – 99.9%+</dd></div>
      <div><dt>Soluble gas removal</dt><dd>Up to 98%</dd></div>
      <div><dt>Duct / stack diameter</dt><dd>Up to 2,000 mm+</dd></div>
      <div><dt>Construction</dt><dd>FRP · PVC · CPVC · PP</dd></div>
    </dl>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal reveal-d1">{media("assets/images/products/scrubber-detail.jpg", "Packed-bed scrubber", "media--tall")}</div>
      <div class="reveal">
        <span class="eyebrow">How it works</span>
        <h2>Wet scrubbing technology</h2>
        <p>Wet scrubbers remove soluble gases and particulates by bringing the gas stream into intimate contact with a scrubbing liquid. Absorption can be enhanced by a chemical reaction in the liquid.</p>
        <h4>Contacting methods</h4>
        {chips(["Random packed beds", "Structured packed beds", "Sieve trays", "Water jets", "Venturis", "Spray chambers", "Fine-bubble diffusion"])}
        <h4 class="mt-2">Configurations</h4>
        <p>Vertical counter-flow or horizontal cross-flow, usually with packed beds, using recycled water or water with an additive such as sodium hydroxide.</p>
        <h4>Construction</h4>
        <p class="mb-0">FRP and dual-laminated thermoplastics (PVC, CPVC, polypropylene) to ASTM and relevant product standards.</p>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Applications</span><h2>Industries we clean up for</h2></div>
      <div class="reveal reveal-d1">{chips(apps)}</div>
    </div>
  </div>
</section>
{DUAL_LAMINATE}"""
    return product_page(path, "FRP Fume Scrubbers, Ducts & Stacks | Air Pollution Control – Laybond",
        "FRP and dual-laminate acid gas scrubbers, ducting, stacks and dampers. 1,500–70,000 cfm, up to 99.9% particulate removal and 98% soluble gas removal.",
        "Scrubbing systems", "Fume scrubbers, corrosive-gas ducting, stacks, dampers and exhaust fans that keep your plant and your people safe.",
        "Air pollution control", "assets/images/hero/scrubber-hero.jpg", body, "Scrubbing Systems")


def pipes():
    path = "pipe-fittings.html"
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>FRP pipe built to your plant's spec</h2>
        <p class="lead">Laybond FRP pipes are built to meet or exceed your plant specifications, pressure ratings and industry standards, in whatever resin your service requires.</p>
        <p>We manufacture, fabricate and install FRP pipe from <strong>25 mm to 1,500 mm</strong> with a full line of fittings. We also help with site layout, anchoring, support spacing, flow design, material selection and installation. Coca-Cola has relied on our piping for over 23 years.</p>
        <dl class="spec-list mt-2">
          <div><dt>Diameter range</dt><dd>25 – 1,500 mm</dd></div>
          <div><dt>Standards</dt><dd>BS 6464 · ASTM D-3567</dd></div>
        </dl>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/pipe-fittings.jpg", "FRP pipe &amp; fittings", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="grid grid-3">
      <div class="feature reveal"><div class="feature-icon">{I['check']}</div><h3>Performance tested</h3><p>Every system is engineered and tested to its specified pressure rating.</p></div>
      <div class="feature reveal reveal-d1"><div class="feature-icon">{I['shield']}</div><h3>Leak-free joints</h3><p>Precision-made joints and flanges for reliable, leak-free service.</p></div>
      <div class="feature reveal reveal-d2"><div class="feature-icon">{I['rupee']}</div><h3>Low maintenance</h3><p>No rust, no scaling, no painting, for a lower total cost of ownership.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Applications</span><h2>Piping systems</h2></div>
    <div class="grid grid-2">
      <div class="card reveal">
        {media("assets/images/products/pipe-fuel.jpg", "Underground fuel piping", "media--wide")}
        <div class="card-body"><h3>Motor fuel underground piping</h3><p>For the transfer of petroleum products, alcohol and alcohol-blended fuels.</p>
        <dl class="spec-list" style="margin-top:8px"><div><dt>Diameter</dt><dd>50 – 150 mm</dd></div></dl></div>
      </div>
      <div class="card reveal reveal-d1">
        {media("assets/images/products/pipe-industrial.jpg", "Industrial process piping", "media--wide")}
        <div class="card-body"><h3>Municipal, chemical &amp; industrial piping</h3><p>Above- and below-ground lines for acids, caustics and solvents, cooling towers, fire protection, wastewater process lines, raw-water intake and discharge. Includes no-dig methods: pipe jacking, slip lining and micro-tunnelling.</p>
        <dl class="spec-list" style="margin-top:8px"><div><dt>Diameter</dt><dd>25 – 1,500 mm</dd></div></dl></div>
      </div>
    </div>
  </div>
</section>
{DUAL_LAMINATE}"""
    return product_page(path, "FRP Pipes & Fittings 25–1500 mm | Process & Underground Piping – Laybond",
        "FRP pipes and fittings from 25 mm to 1500 mm for chemical, municipal, industrial and underground fuel piping. Design, fabrication and installation by Laybond.",
        "Pipe &amp; fittings", "FRP piping from 25 mm to 1,500 mm with a complete fittings range, designed, fabricated and installed by our team.",
        "Piping systems", "assets/images/hero/pipe-hero.jpg", body, "Pipe &amp; Fittings")


def linings():
    path = "corrosion-proof-linings.html"
    apps = ["Chemical storage tanks", "Petroleum storage tanks", "Plating &amp; pickling lines", "Food-grade tanks &amp; silos", "Clarifiers &amp; aeration tanks",
            "Neutralisation tanks &amp; pits", "Trenches &amp; sump pits", "Online pipe leak repairs", "Dyke walls", "Steel &amp; concrete structures"]
    steps = [("01", "Surface preparation", "Abrasive blasting to create the profile a lasting bond needs."),
             ("02", "Lining application", "Skilled application of the selected FRP or high-performance lining system."),
             ("03", "Completion &amp; testing", "Curing, inspection and testing of the finished system before handover.")]
    st = "".join(f'<div class="feature reveal reveal-d{i}"><div class="card-num" style="color:var(--accent)">{n}</div><h3>{t}</h3><p>{d}</p></div>' for i, (n, t, d) in enumerate(steps))
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Protect and restore steel &amp; concrete</h2>
        <p class="lead">Corrosion from acids, caustics and aggressive chemicals costs industry heavily every year in repairs, replacement and downtime. Much of it is avoidable with the right lining, correctly applied.</p>
        <p>Laybond is an experienced supplier and applicator of high-performance coatings and lining systems for tanks, vessels, silos, pipes and other steel and concrete structures. Long-standing relationships with leading corrosion-control manufacturers let us recommend the right system, even for severe process or storage duty.</p>
        <p class="mb-0">On site, our crews work fast and as a team, in full cooperation with your production department and in line with your site rules, health &amp; safety regulations and industry best practice.</p>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/linings.jpg", "FRP tank lining", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section section--darker">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Turnkey installation</span><h2>How we line</h2></div>
    <div class="grid grid-3">{st}</div>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="split split--reverse">
      <div class="reveal">
        <span class="eyebrow">Thick-film FRP lining</span>
        <h2>The smarter alternative to new tank bottoms</h2>
        <p class="lead">A thick-film FRP lining is a proven alternative to replacing corroded steel tank bottoms, mitigating internal and even external corrosion.</p>
        {checks(["Vinyl ester resin systems resist many corrosive cargoes at elevated temperatures", "Costs less than replacing existing steel tank bottoms", "Faster installation and minimal downtime; tanks return to service sooner", "Many installations with a 35+ year service history"])}
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/lining-detail.jpg", "Lining in progress", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Applications</span><h2>What we line</h2></div>
      <div class="reveal reveal-d1">{chips(apps)}</div>
    </div>
  </div>
</section>
{DUAL_LAMINATE}"""
    return product_page(path, "Corrosion-Proof FRP Linings | Tank Bottom & Concrete Lining – Laybond",
        "FRP and high-performance corrosion-proof linings for steel and concrete tanks, pits, trenches, dyke walls and pipes. Turnkey blasting, application and testing.",
        "Corrosion-proof linings", "FRP and high-performance lining systems that protect and restore tanks, pits, pipes and structures, applied turnkey by our crews.",
        "Coatings &amp; linings", "assets/images/hero/linings-hero.jpg", body, "Corrosion-Proof Linings")


def fabrication():
    path = "steel-fabrications.html"
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Overview</span>
        <h2>Steel fabrication &amp; more</h2>
        <p class="lead">Industry-leading services in heavy, general, pipe and structural fabrication, in our workshop or on your site.</p>
        <p>We are known for mild steel and stainless steel equipment in a range of capacities and sizes: dust collectors, extraction vessels, agitator vessels, and mixing and reaction vessels. We also fabricate base frames, skids, chimneys, scrubbers, industrial blowers, dampers, ducting, utility pipelines and fittings.</p>
        <div class="grid mt-2" style="grid-template-columns:1fr 1fr;gap:14px">
          <div class="note"><strong>Workshop fabrication</strong></div>
          <div class="note"><strong>On-site fabrication, installation &amp; erection</strong></div>
        </div>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/fabrication.jpg", "Steel fabrication", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card reveal">
        {media("assets/images/products/ms-tanks.jpg", "Mild steel storage tank", "media--wide")}
        <div class="card-body"><h3>Mild steel storage tanks</h3><p>For HSD, furnace oil, LDO, petroleum and many other applications, designed and built to international codes and standards.</p></div>
      </div>
      <div class="card reveal reveal-d1">
        {media("assets/images/products/ss-tanks.jpg", "Stainless steel tank", "media--wide")}
        <div class="card-body"><h3>Stainless steel storage tanks</h3><p>Configured around your operating temperature and stored product. The choice where the substance or environment is caustic, or where contamination must be minimal.</p></div>
      </div>
    </div>
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Agitators</span>
        <h2>Mixing, built to order</h2>
        <p class="lead">Top-, side- and bottom-entering agitators, from small pilot units to large production machines.</p>
        {checks(["Right-angle and parallel-shaft units", "Gear-reduced, direct-drive and air-driven designs", "Beam/channel, tank-side clamp or vessel flange mounting, with a choice of seals", "For blending viscous liquids, re-suspending solids and dissolving powders", "FRP or thermoplastic-lined (PP, PVC, HDPE) for reaction-vessel service"])}
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/agitator.jpg", "Agitator", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="split split--reverse">
      <div class="reveal">
        <span class="eyebrow">FRP motor guards &amp; canopies</span>
        <h2>Weatherproof protection for every motor</h2>
        <p class="lead">FRP motor guard canopies, instrumentation canopies and PA-system canopies in numerous specifications.</p>
        {checks(["Fits all motor makes, horizontal (B3) and vertical (V1) mounting", "Frame sizes 71M to 630M; HT and LT motors", "Water-resistant, anti-rust, built-in colour, low maintenance", "Unaffected by corrosive chemicals, heavy rain or prolonged UV exposure", "Light and easy to handle"], cols=False)}
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/motor-guard.jpg", "FRP motor guard canopy", "media--tall")}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal"><span class="eyebrow">Applications</span><h2>Where we fabricate</h2></div>
      <div class="reveal reveal-d1">{chips(["Water treatment plants", "Effluent treatment plants", "Power plants", "IBR &amp; non-IBR piping", "Process &amp; pressure vessels", "Chemical dosing systems", "Storage tanks", "Sheet metal enclosures", "Structures &amp; roofing", "Erection &amp; site works"])}</div>
    </div>
  </div>
</section>
"""
    return product_page(path, "Steel Fabrication, Agitators & FRP Motor Guards – Laybond",
        "MS and SS storage tanks, process vessels, agitators, ducting, structures and FRP motor guard canopies. Workshop and on-site fabrication, installation and erection.",
        "Fabrication &amp; others", "Mild steel and stainless steel tanks and vessels, agitators, structures and FRP motor guards, fabricated in our workshop or on your site.",
        "Heavy &amp; structural fabrication", "assets/images/hero/fabrication-hero.jpg", body, "Fabrication &amp; Others")


def technical():
    path = "technical.html"
    standards = [("BS 4994-1987", "Design and construction of vessels and tanks in reinforced plastics"),
                 ("BS 6464-1984", "Reinforced plastic pipes, fittings and joints for process plants"),
                 ("ASTM D-3567", "Determining dimensions of fibreglass pipe and fittings"),
                 ("NBS PS 15-69", "Custom contact-moulded reinforced-polyester chemical-resistant process equipment"),
                 ("ASME RTP-1", "Reinforced thermoset plastic corrosion-resistant equipment"),
                 ("ASTM D-4097", "Contact-moulded glass-fibre-reinforced thermoset resin corrosion-resistant tanks"),
                 ("ASTM D-695", "Compressive properties of rigid plastics"),
                 ("ASTM D-3982", "Contact-moulded fibreglass ducts and hoods")]
    std = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in standards)
    dl = [("SpecificationLaybond.pdf", "Specifications – FRP Tanks", "PDF · 10 pages"),
          ("HIManualLaybond.pdf", "Handling &amp; Installation Manual – FRP Tanks", "PDF · 10 pages"),
          ("OMManual-Laybond.pdf", "Operation &amp; Maintenance Manual – FRP Tanks", "PDF · 10 pages"),
          ("flangetable.pdf", "Pipe Flange Tables", "PDF · 10 pages"),
          ("IsopthalicPolyEsterResin-II.pdf", "Isophthalic Polyester Resin – Corrosion Chart", "PDF · 5 pages"),
          ("IsopthalicVinylEsterResin-I.pdf", "Isophthalic / Vinyl Ester Resin – Corrosion Chart", "PDF · 3 pages"),
          ("corrossionchartforvinylesters.pdf", "Vinyl Ester Resin – Corrosion Chart", "PDF · 6 MB"),
          ("chemicalresistanceofthermoplasticforduallaminatecons.pdf", "Thermoplastic (Dual Laminate) – Chemical Resistance Chart", "PDF · 143 pages")]
    dls = "".join(f'<a class="download reveal" href="assets/downloads/{f}" target="_blank" rel="noopener"><span class="download-icon">PDF</span><span><strong>{t}</strong><span>{m}</span></span>{I["download"]}</a>' for f, t, m in dl)
    body = f"""<section class="section section--white">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Construction</span>
        <h2>Laminate construction</h2>
        <p class="lead">Every Laybond tank is built on a male mould for a smooth, resin-rich internal surface, the first line of defence against chemical attack.</p>
        <p>The corrosion barrier, made up of the inner surface and interior layer, has a glass content of <strong>27% ± 5% by weight</strong>. A structural layer behind it carries the mechanical loads, finished with a protective outer surface.</p>
        <dl class="spec-list mt-2"><div><dt>Corrosion barrier glass content</dt><dd>27% ± 5%</dd></div><div><dt>Moulding</dt><dd>Male mould, contact-moulded</dd></div></dl>
      </div>
      <div class="reveal reveal-d1">{media("assets/images/products/laminate-construction.jpg", "Laminate construction diagram", "media--square")}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Resin systems</span><h2>Choose your grade</h2><p class="lead">Three standard resin systems to balance chemical resistance and cost.</p></div>
    <div class="grid grid-3">
      <div class="tier reveal"><span class="tier-label">Economy</span><h3>Isophthalic polyester</h3><dl><div><dt>Inner surface &amp; interior layer</dt><dd>Isophthalic polyester</dd></div><div><dt>Structural layer &amp; outer surface</dt><dd>Isophthalic polyester</dd></div></dl></div>
      <div class="tier tier--featured reveal reveal-d1"><span class="tier-label">Standard · most popular</span><h3>Vinyl ester barrier</h3><dl><div><dt>Inner surface &amp; interior layer</dt><dd>Vinyl ester</dd></div><div><dt>Structural layer &amp; outer surface</dt><dd>Isophthalic polyester</dd></div></dl></div>
      <div class="tier reveal reveal-d2"><span class="tier-label">Premium</span><h3>Vinyl ester throughout</h3><dl><div><dt>Inner surface &amp; interior layer</dt><dd>Vinyl ester</dd></div><div><dt>Structural layer &amp; outer surface</dt><dd>Vinyl ester</dd></div></dl></div>
    </div>
  </div>
</section>
<section class="section section--white">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Compliance</span><h2>Standards we design to</h2></div>
    <div class="table-wrap reveal"><table class="spec-table"><thead><tr><th>Standard</th><th>Scope</th></tr></thead><tbody>{std}</tbody></table></div>
  </div>
</section>
<section class="section section--darker">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Engineering details</span><h2>Design features</h2></div>
    <div class="grid grid-2">
      <div class="feature reveal"><h3>Tank bottoms</h3><p>Flat and sloped bottoms use a seamless, one-piece bottom-to-wall construction with a generous knuckle radius at the corner. Cone and dished bottoms are one-piece and seamless, with a steel support ring overlaid with fibreglass.</p></div>
      <div class="feature reveal reveal-d1"><h3>Tops</h3><p>Closed tops come with a 20″ or 24″ loose-cover manhole with grab handle. Open tops have a 90° flanged rim (one-, two- or three-piece cover) or a Type II rim.</p></div>
      <div class="feature reveal"><h3>Nozzles</h3><p>Flanged nozzles are hand lay-up construction, with conical and plate gussets available for added strength.</p></div>
      <div class="feature reveal reveal-d1"><h3>Insulation &amp; heating</h3><p>Insulated tanks have a reinforced FRP outer shell. A replaceable heat panel is offered as an alternative to wire heating systems.</p></div>
    </div>
    <div class="grid grid-3 mt-3">
      {media("assets/images/products/design-features-1.jpg", "Design features 1")}
      {media("assets/images/products/design-features-2.jpg", "Design features 2")}
      {media("assets/images/products/design-features-3.jpg", "Design features 3")}
    </div>
  </div>
</section>
<section class="section" id="downloads">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Downloads</span><h2>Specifications, manuals &amp; corrosion charts</h2><p class="lead">Free technical documents for engineers, consultants and purchasing teams.</p></div>
    <div class="grid grid-2" style="gap:14px">{dls}</div>
    <p class="mt-2"><a class="card-link" href="warranty.html">Read our warranty terms {I['arrow']}</a></p>
  </div>
</section>
"""
    html = head("Technical Data, Standards & Downloads | Laybond FRP", "FRP laminate construction, resin systems, design standards (BS 4994, ASTM D-4097, ASME RTP-1), design features and downloadable specifications, manuals and corrosion charts.", path)
    html += header(path)
    html += page_hero("Technical", "Construction, resin systems, standards and design details, plus specifications, manuals and corrosion charts to download.",
                      [("Technical", None)], "assets/images/hero/technical-hero.jpg", "Technical hero", "Engineering data")
    html += body + cta() + footer()
    return html
