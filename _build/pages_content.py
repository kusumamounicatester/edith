# -*- coding: utf-8 -*-
"""
Per-page content for every EDITH page beyond the homepage. Each entry in
PAGES becomes one finished, standalone .html file when generate_pages.py
runs. Keys map straight to brief section numbers in comments so a developer
(or Kusuma) can find the source requirement fast.
"""

CONSENT_ROW = """
<div class="consent-row">
  <input type="checkbox" id="consent-{id}" name="consent" required>
  <label for="consent-{id}"><span data-i18n="t0161">I agree to EDITH contacting me about this enquiry and storing my details for that purpose, per the</span> <a href="privacy-policy.html"><span data-i18n="t0153">Privacy Policy</span></a><span data-i18n="t0162">. Required under India's DPDP Act 2023 (brief §10, §16).</span></label>
</div>
"""

PAGES = {}

# ============================================================
# 6.1 — INVEST WITH US
# ============================================================
PAGES["invest-with-us.html"] = dict(
    title="Invest With Us — Investment Collaboration | EDITH",
    description="Put capital into an EDITH construction project. Choose a discounted flat at handover or a monetary return — both structured through a per-project SPV.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0163">EDITH-01 · Investment Collaboration</span></p>
    <h1><span data-i18n="t0164">Deploy capital into a project you can actually see</span></h1>
    <p><span data-i18n="t0165">Two ways in: take a flat at a discount once we hand over, or take a monetary return once the project sells or completes. Both are structured project-by-project, never as a pooled promise.</span></p>
    <div class="page-hero__actions">
      <a href="#register-interest" class="btn btn-primary"><span data-i18n="t0166">Register interest</span></a>
      <a href="#how-protected" class="btn btn-secondary"><span data-i18n="t0167">How your money is protected</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><h2><span data-i18n="t0168">Two models, compared</span></h2></div>
    <div class="table-scroll">
      <table class="compare-table">
        <thead><tr><th></th><th><span data-i18n="t0169">Discounted flat</span></th><th><span data-i18n="t0170">Monetary return</span></th></tr></thead>
        <tbody>
          <tr><td><span data-i18n="t0171">What you get</span></td><td><span data-i18n="t0172">A completed flat at a price below the eventual market rate</span></td><td><span data-i18n="t0173">Your capital back, plus a profit share, once the project sells or completes</span></td></tr>
          <tr><td><span data-i18n="t0174">Minimum ticket size</span></td><td colspan="2">₹25,00,000</td></tr>
          <tr><td><span data-i18n="t0175">Indicative timeline</span></td><td colspan="2"><span data-i18n="t0176">18–24 months from entry to handover/exit</span></td></tr>
          <tr><td><span data-i18n="t0177">When it happens</span></td><td><span data-i18n="t0178">At handover / possession</span></td><td><span data-i18n="t0179">At project sale or completion, per the signed agreement</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="example-box">
      <strong><span data-i18n="t0180">Illustrative example — not a guarantee</span></strong>
      <span data-i18n="t0181">₹50L invested could translate to a flat worth roughly ₹65L at handover under the discounted-flat model. Actual figures depend on the specific project, stage of entry, and signed agreement. (Demo figures for illustration — final worked examples pending lawyer review per project type.)</span>
    </div>

    <h2 id="how-protected"><span data-i18n="t0167">How your money is protected</span></h2>
    <p><span data-i18n="t0182">Each project is ring-fenced through a per-project SPV (Special Purpose Vehicle — a separate legal entity that owns and runs that one project), so investors are genuine co-owners of that entity rather than depositors in a pooled scheme. Every investment is backed by a signed agreement covering exit terms and update frequency, and funds move through an escrow arrangement rather than directly to EDITH.</span> <a href="blog/index.html"><span data-i18n="t0183">Read the full explainer in the Knowledge Hub</span></a> <span data-i18n="t0184">— and see the legal note at the bottom of this page.</span></p>

    <h2><span data-i18n="t0185">Open projects</span></h2>
    <p class="field-hint"><span data-i18n="t0186">Only RERA-registered projects are listed here, per brief §16 — the site itself counts as an advertisement under RERA.</span></p>
    <div class="listing-grid">
      <article class="listing-card">
        <img src="assets/project-placeholder-1.jpg" alt="Jubilee Heights, Kondapur" data-i18n-attr-alt="t0078">
        <div class="listing-card__body">
          <span class="pill"><span data-i18n="t0079">Under construction</span></span>
          <h3><span data-i18n="t0080">Jubilee Heights</span></h3>
          <p><span data-i18n="t0187">Kondapur, Hyderabad · Ticket size ₹25L+ · RERA P02200003456</span></p>
          <a href="#register-interest" class="btn btn-ghost"><span data-i18n="t0166">Register interest</span></a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--band" id="register-interest">
  <div class="container split-layout">
    <div>
      <h2><span data-i18n="t0188">Not sure yet? That's fine.</span></h2>
      <p><span data-i18n="t0189">Register interest with basic details first — full KYC (PAN, address proof) is only ever requested after we've spoken, never on this public form, per brief §6.1.</span></p>
      <p class="disclaimer"><span data-i18n="t0190">The words "assured" or "guaranteed returns" never appear on this site, in any project description, or in any conversation with our team — this is a structural legal requirement, not a style choice (brief §16).</span></p>
    </div>
    <form class="form-card" data-module="investment-collaboration">
      <h2><span data-i18n="t0191">Register your interest</span></h2>
      <div class="form-grid">
        <div class="field"><label for="inv-name"><span data-i18n="t0192">Full name</span></label><input type="text" id="inv-name" name="name" required></div>
        <div class="field"><label for="inv-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="inv-phone" name="phone" required></div>
        <div class="field"><label for="inv-email"><span data-i18n="t0194">Email</span></label><input type="email" id="inv-email" name="email" required></div>
        <div class="field"><label for="inv-city"><span data-i18n="t0195">City</span></label><input type="text" id="inv-city" name="city" required></div>
        <div class="field"><label for="inv-type"><span data-i18n="t0196">Investor type</span></label>
          <select id="inv-type" name="investorType">
            <option><span data-i18n="t0197">Individual</span></option><option><span data-i18n="t0198">NRI</span></option><option><span data-i18n="t0199">HNI</span></option><option><span data-i18n="t0200">Company</span></option>
          </select>
        </div>
        <div class="field"><label for="inv-amount"><span data-i18n="t0201">Indicative amount range</span></label>
          <select id="inv-amount" name="amountRange">
            <option><span data-i18n="t0202">Under ₹10L</span></option><option>₹10L – ₹50L</option><option><span data-i18n="t0203">₹50L – ₹1Cr</span></option><option><span data-i18n="t0204">Above ₹1Cr</span></option>
          </select>
        </div>
        <div class="field"><label for="inv-model"><span data-i18n="t0205">Preferred model</span></label>
          <select id="inv-model" name="preferredModel"><option><span data-i18n="t0169">Discounted flat</span></option><option><span data-i18n="t0170">Monetary return</span></option><option><span data-i18n="t0206">Not sure yet</span></option></select>
        </div>
        <div class="field"><label for="inv-timeframe"><span data-i18n="t0207">Timeframe</span></label>
          <select id="inv-timeframe" name="timeframe"><option><span data-i18n="t0208">Ready now</span></option><option><span data-i18n="t0209">Within 3 months</span></option><option><span data-i18n="t0210">Just exploring</span></option></select>
        </div>
        <div class="field form-grid--full"><label for="inv-heard"><span data-i18n="t0211">How did you hear about EDITH?</span></label><input type="text" id="inv-heard" name="source"></div>
        <div class="field form-grid--full"><label for="inv-message"><span data-i18n="t0212">Message (optional)</span></label><textarea id="inv-message" name="message"></textarea></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0166">Register interest</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="invest"))
)

# ============================================================
# 6.2 — BUILDER JOINT VENTURES
# ============================================================
PAGES["builder-jv.html"] = dict(
    title="Builder Joint Ventures | EDITH",
    description="Pool land, finance, and execution with EDITH on a single project — shared compliance, joint branding, and better vendor/lender rates from combined scale.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0214">EDITH-02 · Builder Joint Ventures</span></p>
    <h1><span data-i18n="t0215">Bigger than either of us could take on alone</span></h1>
    <p><span data-i18n="t0216">A JV is a formal, temporary partnership for one specific project. Bring land, capital, or manpower — EDITH brings the rest, and the combined scale gets better rates from suppliers and lenders than either company would get solo.</span></p>
    <div class="page-hero__actions"><a href="#jv-form" class="btn btn-primary"><span data-i18n="t0217">Start a JV enquiry</span></a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2><span data-i18n="t0218">How the split works</span></h2>
      <p><span data-i18n="t0219">Profit or built area is split based on what each side contributes — land, cash, or labour — agreed contract by contract. Nothing below is binding; it's a starting point for a conversation, not a term sheet.</span></p>
    </div>

    <div class="calc-card" style="max-width:640px;">
      <h3><span data-i18n="t0220">JV Sharing Calculator</span></h3>
      <p class="field-hint"><span data-i18n="t0221">Model a rough split before you ever make contact — brief §6.2 calls this out as a strong hook precisely because it gives real value with zero commitment.</span></p>
      <form id="jvCalcForm">
        <div class="calc-field"><label for="jv-land"><span data-i18n="t0222">Land value contributed (₹)</span></label><input type="number" id="jv-land" min="0" step="10000" value="5000000"></div>
        <div class="calc-field"><label for="jv-cash"><span data-i18n="t0223">Cash/finance contributed (₹)</span></label><input type="number" id="jv-cash" min="0" step="10000" value="3000000"></div>
        <div class="calc-field"><label for="jv-edith"><span data-i18n="t0224">EDITH's contribution — cash + execution (₹)</span></label><input type="number" id="jv-edith" min="0" step="10000" value="4000000"></div>
        <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0225">Estimate split</span></button>
      </form>
      <div class="calc-result" id="jvResult" hidden>
        <strong id="jvSplit">—</strong>
        <span><span data-i18n="t0226">Indicative only — the real split is negotiated per contract, factoring in risk, timeline, and execution effort, not contribution value alone.</span></span>
      </div>
      <p class="disclaimer"><span data-i18n="t0227">Indicative and for general information only; not professional, legal, tax or investment advice (brief §8, §16).</span></p>
    </div>
  </div>
</section>

<section class="section section--band" id="jv-form">
  <div class="container split-layout">
    <div>
      <h2><span data-i18n="t0228">What EDITH brings to a JV</span></h2>
      <ul>
        <li><span data-i18n="t0229">Shared compliance costs — CA/CS-led, in-house</span></li>
        <li><span data-i18n="t0230">Joint branding and marketing reach</span></li>
        <li><span data-i18n="t0231">Better vendor and lender rates from combined project scale</span></li>
      </ul>
    </div>
    <form class="form-card" data-module="builder-jv">
      <h2><span data-i18n="t0232">Tell us about your firm</span></h2>
      <div class="form-grid">
        <div class="field"><label for="jv-firm"><span data-i18n="t0233">Firm name</span></label><input type="text" id="jv-firm" name="firmName" required></div>
        <div class="field"><label for="jv-reg"><span data-i18n="t0234">GST / RERA / registration no.</span></label><input type="text" id="jv-reg" name="registrationNo"></div>
        <div class="field"><label for="jv-years"><span data-i18n="t0043">Years active</span></label><input type="number" id="jv-years" name="yearsActive" min="0"></div>
        <div class="field"><label for="jv-city"><span data-i18n="t0195">City</span></label><input type="text" id="jv-city" name="city" required></div>
        <div class="field form-grid--full"><label for="jv-current"><span data-i18n="t0235">Current project(s)</span></label><input type="text" id="jv-current" name="currentProjects"></div>
        <div class="field form-grid--full"><label for="jv-bring"><span data-i18n="t0236">What land/finance do you bring?</span></label><textarea id="jv-bring" name="contribution"></textarea></div>
        <div class="field form-grid--full"><label for="jv-want"><span data-i18n="t0237">What do you want from the JV?</span></label><textarea id="jv-want" name="wants"></textarea></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0238">Submit JV enquiry</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="jv")),
    extra_scripts='<script src="js/jv-calculator.js"></script>',
)

# ============================================================
# 6.3 — PROFESSIONAL & COMPLIANCE SERVICES
# ============================================================
PAGES["professional-services.html"] = dict(
    title="Professional & Compliance Services | EDITH",
    description="CA/CS-led RERA registration, GST advisory, MCA/ROC filings, and financial modelling — for other builders and agents in the trade.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0239">EDITH-03 · Professional &amp; Compliance Services</span></p>
    <h1><span data-i18n="t0240">The same team that keeps EDITH compliant, now working for you</span></h1>
    <p><span data-i18n="t0241">EDITH's in-house CA (Chartered Accountant) and CS (Company Secretary) normally just handle EDITH's own paperwork. This is that same expertise, sold as a service to other builders and agents in the trade.</span></p>
    <div class="page-hero__actions"><a href="#quote-form" class="btn btn-primary"><span data-i18n="t0242">Request a quote</span></a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <h2><span data-i18n="t0146">Services</span></h2>
      <p><span data-i18n="t0243">Every card below is either "starting from" pricing or a request-a-quote — depends on how standardised the work is.</span></p>
    </div>
    <div class="offer-grid">
      <div class="offer-card" id="rera">
        <h3><span data-i18n="t0244">RERA project registration</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0245">Turnaround: 25–35 working days</span></p>
        <p><span data-i18n="t0246">Full registration for a project so it can be legally advertised and sold.</span></p>
        <span class="offer-card__price"><span data-i18n="t0242">Request a quote</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0247">RERA agent registration</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0248">Turnaround: 7–10 working days</span></p>
        <p><span data-i18n="t0249">Registration for individual agents joining EDITH's network or operating independently.</span></p>
        <span class="offer-card__price"><span data-i18n="t0250">Starting from ₹7,500</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0251">Financial modelling &amp; DPRs</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0252">Turnaround: 10–15 working days</span></p>
        <p><span data-i18n="t0253">Detailed Project Reports projecting a project's costs and returns.</span></p>
        <span class="offer-card__price"><span data-i18n="t0242">Request a quote</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0254">GST advisory</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0255">Includes JDA &amp; works-contract scenarios</span></p>
        <p><span data-i18n="t0256">How GST applies to your specific project or transaction structure.</span></p>
        <span class="offer-card__price"><span data-i18n="t0257">Starting from ₹5,000</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0258">MCA/ROC &amp; LLP filings</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0259">Turnaround: 5–7 working days</span></p>
        <p><span data-i18n="t0260">Company and LLP registration and maintenance filings.</span></p>
        <span class="offer-card__price"><span data-i18n="t0261">Starting from ₹4,000</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0262">Project funding / bank liaison</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0263">Turnaround: 20–30 working days</span></p>
        <p><span data-i18n="t0264">Support arranging and structuring project financing.</span></p>
        <span class="offer-card__price"><span data-i18n="t0242">Request a quote</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0265">Valuation under Rule 11UA</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0259">Turnaround: 5–7 working days</span></p>
        <p><span data-i18n="t0266">The Income Tax rule governing how a company's shares are valued.</span></p>
        <span class="offer-card__price"><span data-i18n="t0242">Request a quote</span></span>
      </div>
      <div class="offer-card">
        <h3><span data-i18n="t0267">Statutory compliance calendars</span></h3>
        <p class="offer-card__meta"><span data-i18n="t0268">Turnaround: 3–5 working days</span></p>
        <p><span data-i18n="t0269">A running schedule of your legally mandated filing deadlines.</span></p>
        <span class="offer-card__price"><span data-i18n="t0270">Starting from ₹3,000</span></span>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="quote-form">
  <div class="container" style="max-width:640px;">
    <form class="form-card" data-module="professional-services">
      <h2><span data-i18n="t0242">Request a quote</span></h2>
      <div class="form-grid">
        <div class="field"><label for="ps-name"><span data-i18n="t0271">Name</span></label><input type="text" id="ps-name" name="name" required></div>
        <div class="field"><label for="ps-firm"><span data-i18n="t0272">Firm / individual</span></label><input type="text" id="ps-firm" name="firm"></div>
        <div class="field"><label for="ps-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="ps-phone" name="phone" required></div>
        <div class="field"><label for="ps-email"><span data-i18n="t0194">Email</span></label><input type="email" id="ps-email" name="email" required></div>
        <div class="field form-grid--full"><label for="ps-service"><span data-i18n="t0273">Which service?</span></label>
          <select id="ps-service" name="service">
            <option><span data-i18n="t0244">RERA project registration</span></option><option><span data-i18n="t0247">RERA agent registration</span></option>
            <option><span data-i18n="t0274">Financial modelling / DPR</span></option><option><span data-i18n="t0254">GST advisory</span></option>
            <option><span data-i18n="t0258">MCA/ROC &amp; LLP filings</span></option><option><span data-i18n="t0262">Project funding / bank liaison</span></option>
            <option><span data-i18n="t0275">Rule 11UA valuation</span></option><option><span data-i18n="t0276">Statutory compliance calendar</span></option>
          </select>
        </div>
        <div class="field form-grid--full"><label for="ps-details"><span data-i18n="t0277">Details</span></label><textarea id="ps-details" name="details"></textarea></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0278">Request quote</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="ps")),
)

# ============================================================
# 6.4 — CONSUMER SERVICES & QUOTE ENGINE
# ============================================================
PAGES["get-a-quote.html"] = dict(
    title="Get a Quote — Masonry, Interiors & Borewell | EDITH",
    description="Get an instant indicative estimate for masonry, interior design, or borewell drilling — confirmed with a site visit.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0279">EDITH-04 · Consumer Services &amp; Quote Engine</span></p>
    <h1><span data-i18n="t0280">Everyday construction work, priced fast</span></h1>
    <p><span data-i18n="t0281">Not building a whole house — just need masonry, interior design, or a borewell drilled? Get an instant indicative estimate below, confirmed later with a site visit.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="offer-grid" style="margin-bottom: var(--space-8);">
      <div class="offer-card" id="construction"><h3><span data-i18n="t0011">Construction &amp; Masonry</span></h3><p><span data-i18n="t0282">Bricklaying and wall construction, small to mid-size jobs.</span></p><span class="offer-card__price"><span data-i18n="t0283">See sample work →</span></span></div>
      <div class="offer-card" id="interiors"><h3><span data-i18n="t0012">Interior Design</span></h3><p><span data-i18n="t0284">Room-by-room design and execution.</span></p><span class="offer-card__price"><span data-i18n="t0283">See sample work →</span></span></div>
      <div class="offer-card" id="borewell"><h3><span data-i18n="t0013">Borewell Drilling</span></h3><p><span data-i18n="t0285">Groundwater access, sized to your site's soil type.</span></p><span class="offer-card__price"><span data-i18n="t0283">See sample work →</span></span></div>
    </div>

    <div class="wizard" id="quoteWizard">
      <div class="wizard__steps">
        <span class="is-active" data-step="1"><span data-i18n="t0286">1. Service</span></span>
        <span data-step="2"><span data-i18n="t0287">2. Details</span></span>
        <span data-step="3"><span data-i18n="t0288">3. Location</span></span>
        <span data-step="4"><span data-i18n="t0289">4. Contact</span></span>
      </div>

      <div class="wizard__panel is-active" data-panel="1">
        <div class="field"><label for="q-service"><span data-i18n="t0290">What do you need?</span></label>
          <select id="q-service" name="service">
            <option value="construction"><span data-i18n="t0011">Construction &amp; Masonry</span></option>
            <option value="interiors"><span data-i18n="t0012">Interior Design</span></option>
            <option value="borewell"><span data-i18n="t0013">Borewell Drilling</span></option>
          </select>
        </div>
        <div class="wizard__nav"><span></span><button type="button" class="btn btn-primary" data-next><span data-i18n="t0291">Next</span></button></div>
      </div>

      <div class="wizard__panel" data-panel="2">
        <div id="paramsConstruction">
          <div class="field"><label for="q-area"><span data-i18n="t0105">Built-up area (sq. ft.)</span></label><input type="number" id="q-area" value="1000"></div>
          <div class="field"><label for="q-quality"><span data-i18n="t0106">Quality tier</span></label><select id="q-quality"><option><span data-i18n="t0107">Basic</span></option><option selected><span data-i18n="t0108">Standard</span></option><option><span data-i18n="t0109">Premium</span></option></select></div>
        </div>
        <div id="paramsInteriors" hidden>
          <div class="field"><label for="q-rooms"><span data-i18n="t0292">Room count</span></label><input type="number" id="q-rooms" value="2"></div>
          <div class="field"><label for="q-style"><span data-i18n="t0293">Style</span></label><select id="q-style"><option><span data-i18n="t0294">Minimal</span></option><option><span data-i18n="t0295">Modern</span></option><option><span data-i18n="t0296">Traditional</span></option></select></div>
        </div>
        <div id="paramsBorewell" hidden>
          <div class="field"><label for="q-depth"><span data-i18n="t0297">Estimated site depth (ft.)</span></label><input type="number" id="q-depth" value="300"></div>
          <div class="field"><label for="q-soil"><span data-i18n="t0298">Soil type</span></label><select id="q-soil"><option><span data-i18n="t0299">Soft</span></option><option><span data-i18n="t0300">Mixed</span></option><option><span data-i18n="t0301">Rocky</span></option></select></div>
        </div>
        <div class="wizard__nav"><button type="button" class="btn btn-ghost" data-prev><span data-i18n="t0302">Back</span></button><button type="button" class="btn btn-primary" data-next><span data-i18n="t0291">Next</span></button></div>
      </div>

      <div class="wizard__panel" data-panel="3">
        <div class="field"><label for="q-location"><span data-i18n="t0303">Site location / pincode</span></label><input type="text" id="q-location"></div>
        <div class="wizard__nav"><button type="button" class="btn btn-ghost" data-prev><span data-i18n="t0302">Back</span></button><button type="button" class="btn btn-primary" data-next><span data-i18n="t0291">Next</span></button></div>
      </div>

      <div class="wizard__panel" data-panel="4">
        <form data-module="consumer-quote">
          <div class="form-grid">
            <div class="field"><label for="q-name"><span data-i18n="t0271">Name</span></label><input type="text" id="q-name" name="name" required></div>
            <div class="field"><label for="q-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="q-phone" name="phone" required></div>
          </div>
          __CONSENT__
          <button type="submit" class="btn btn-primary btn-block" id="quoteSubmit"><span data-i18n="t0304">See my estimate</span></button>
        </form>
        <div class="wizard__estimate" id="quoteEstimate" hidden>
          <strong id="quoteEstimateValue">—</strong>
          <p style="margin-top:var(--space-2);"><span data-i18n="t0305">Indicative only — we'll confirm with a site visit before anything is booked.</span></p>
        </div>
        <div class="wizard__nav"><button type="button" class="btn btn-ghost" data-prev><span data-i18n="t0302">Back</span></button><span></span></div>
      </div>
    </div>

    <p class="disclaimer" style="max-width:640px;"><span data-i18n="t0306">Indicative and for general information only; not professional, legal, tax or investment advice. Quotes are estimates subject to confirmation via an actual site visit (brief §8, §16). Full rate-card detail is above, under "how pricing works."</span></p>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="quote")),
    extra_scripts='<script src="js/quote-wizard.js"></script>',
)

# ============================================================
# 6.5 — STUDENT INTERNSHIPS
# ============================================================
PAGES["internships.html"] = dict(
    title="Student Internships | EDITH",
    description="Real construction-site exposure — cost estimation, billing, site supervision — with a stipend and a possible job pathway.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0307">EDITH-05 · Student Internships</span></p>
    <h1><span data-i18n="t0308">Real site exposure, not just classroom theory</span></h1>
    <p><span data-i18n="t0309">A structured, stipend-paid placement on actual construction sites — cost estimation, billing, site supervision, and exposure to RERA/GST processes — sometimes leading to a full job offer.</span></p>
    <div class="page-hero__actions"><a href="#apply" class="btn btn-primary"><span data-i18n="t0310">Apply now</span></a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><h2><span data-i18n="t0311">Programme structure</span></h2></div>
    <div class="offer-grid">
      <div class="offer-card"><h3><span data-i18n="t0312">Duration</span></h3><p><span data-i18n="t0313">3–6 months, full-time on-site</span></p></div>
      <div class="offer-card"><h3><span data-i18n="t0314">What you'll learn</span></h3><p><span data-i18n="t0315">Cost estimation, billing, site supervision, and real exposure to RERA/GST paperwork in practice.</span></p></div>
      <div class="offer-card"><h3><span data-i18n="t0316">Stipend</span></h3><p><span data-i18n="t0317">₹8,000–₹15,000/month training allowance, based on year of study</span></p></div>
      <div class="offer-card"><h3><span data-i18n="t0318">Certificate &amp; job pathway</span></h3><p><span data-i18n="t0319">Certificate of completion issued; strong performers get priority consideration for EDITH's Engineer Partnership and Training-to-Placement tracks</span></p></div>
    </div>

    <h2><span data-i18n="t0320">Eligibility &amp; current openings</span></h2>
    <p><span data-i18n="t0321">Open to pre-final and final-year students in Civil Engineering, B.Arch, or Diploma (Civil) · Current openings: 6</span></p>

    <h2><span data-i18n="t0322">From past interns</span></h2>
    <div class="testimonial-grid">
      <div class="testimonial"><blockquote><span data-i18n="t0323">"I learned more about real site billing and RERA paperwork in one summer here than in two years of college labs."</span></blockquote><cite><span data-i18n="t0324">Sai Kiran — Former Intern</span></cite></div>
    </div>
  </div>
</section>

<section class="section section--band" id="apply">
  <div class="container" style="max-width:640px;">
    <form class="form-card" data-module="internships">
      <h2><span data-i18n="t0325">Apply for an internship</span></h2>
      <div class="form-grid">
        <div class="field"><label for="int-name"><span data-i18n="t0271">Name</span></label><input type="text" id="int-name" name="name" required></div>
        <div class="field"><label for="int-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="int-phone" name="phone" required></div>
        <div class="field"><label for="int-email"><span data-i18n="t0194">Email</span></label><input type="email" id="int-email" name="email" required></div>
        <div class="field"><label for="int-college"><span data-i18n="t0326">College</span></label><input type="text" id="int-college" name="college" required></div>
        <div class="field"><label for="int-branch"><span data-i18n="t0327">Branch of study</span></label><input type="text" id="int-branch" name="branch"></div>
        <div class="field"><label for="int-year"><span data-i18n="t0328">Year</span></label><input type="text" id="int-year" name="year"></div>
        <div class="field"><label for="int-domain"><span data-i18n="t0329">Preferred domain</span></label><input type="text" id="int-domain" name="domain"></div>
        <div class="field"><label for="int-avail"><span data-i18n="t0330">Availability</span></label><input type="text" id="int-avail" name="availability"></div>
        <div class="field form-grid--full"><label for="int-resume"><span data-i18n="t0331">Resume</span></label><input type="file" id="int-resume" name="resume"></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0332">Submit application</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="int")),
)

# ============================================================
# 6.6 — CIVIL ENGINEER PARTNERSHIP ("Authorised Partner" — never "franchise")
# ============================================================
PAGES["engineer-partnership.html"] = dict(
    title="Civil Engineer Partnership — Authorised Partner Programme | EDITH",
    description="Run a construction site under the EDITH brand. EDITH arranges funding and handles compliance; you run execution — profit split per project.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0333">EDITH-06 · Civil Engineer Partnership</span></p>
    <h1><span data-i18n="t0334">Run something bigger than you could fund or brand alone</span></h1>
    <p><span data-i18n="t0335">Operate under the EDITH brand and standard procedures, with EDITH arranging project funding and handling compliance behind the scenes — both sides split the profit.</span></p>
    <div class="page-hero__actions"><a href="#apply-engineer" class="btn btn-primary"><span data-i18n="t0336">Apply to partner</span></a></div>
    <p class="field-hint" style="color:rgba(255,255,255,0.6);margin-top:var(--space-4);"><span data-i18n="t0337">Called an "Authorised Partner" or "Channel Associate" agreement in every document — never "franchise" (brief §6.6, §16: that word carries specific legal weight under Indian trademark-licensing law this arrangement isn't set up to meet).</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="story-columns">
      <div>
        <h3><span data-i18n="t0338">What EDITH provides</span></h3>
        <ul>
          <li><span data-i18n="t0339">Brand &amp; marketing</span></li>
          <li><span data-i18n="t0340">Funding arrangement</span></li>
          <li><span data-i18n="t0341">Compliance kept fully in EDITH's own books (RERA, GST, statutory filings)</span></li>
          <li><span data-i18n="t0342">Financial rigor and a network of vendors/lenders</span></li>
          <li><span data-i18n="t0343">Standard Operating Procedures and quality control</span></li>
        </ul>
      </div>
      <div>
        <h3><span data-i18n="t0344">What you provide</span></h3>
        <ul>
          <li><span data-i18n="t0345">On-site execution</span></li>
          <li><span data-i18n="t0346">Local presence and team management</span></li>
          <li><span data-i18n="t0347">Delivery quality, under EDITH's brand and operational control</span></li>
        </ul>
      </div>
      <div>
        <h3><span data-i18n="t0348">How both sides win</span></h3>
        <ul>
          <li><span data-i18n="t0349">Transparent profit/area share per project</span></li>
          <li><span data-i18n="t0350">A defined territory or project allocation</span></li>
          <li><span data-i18n="t0351">A growth path to bigger projects as you build a track record</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="apply-engineer">
  <div class="container" style="max-width:680px;">
    <form class="form-card" data-module="engineer-partnership">
      <h2><span data-i18n="t0352">Apply &amp; vetting form</span></h2>
      <div class="form-grid">
        <div class="field"><label for="eng-name"><span data-i18n="t0271">Name</span></label><input type="text" id="eng-name" name="name" required></div>
        <div class="field"><label for="eng-qual"><span data-i18n="t0353">Qualification</span></label><input type="text" id="eng-qual" name="qualification" required></div>
        <div class="field"><label for="eng-exp"><span data-i18n="t0354">Experience (years)</span></label><input type="number" id="eng-exp" name="experience"></div>
        <div class="field"><label for="eng-loc"><span data-i18n="t0355">Current location / territory</span></label><input type="text" id="eng-loc" name="territory"></div>
        <div class="field"><label for="eng-team"><span data-i18n="t0356">Team size</span></label><input type="number" id="eng-team" name="teamSize"></div>
        <div class="field"><label for="eng-capital"><span data-i18n="t0357">Capital you can bring (if any)</span></label><input type="text" id="eng-capital" name="capital"></div>
        <div class="field form-grid--full"><label for="eng-projects"><span data-i18n="t0358">Sample past projects</span></label><textarea id="eng-projects" name="pastProjects"></textarea></div>
        <div class="field form-grid--full"><label for="eng-refs"><span data-i18n="t0359">References</span></label><textarea id="eng-refs" name="references"></textarea></div>
        <div class="field form-grid--full"><label for="eng-motivation"><span data-i18n="t0360">Why do you want to partner with EDITH?</span></label><textarea id="eng-motivation" name="motivation"></textarea></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0332">Submit application</span></button>
    </form>
    <p class="field-hint" style="margin-top:var(--space-4);"><span data-i18n="t0361">Applications proceed to an interview stage inside the admin dashboard workflow (brief §6.6, §11).</span></p>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="eng")),
)

# ============================================================
# 6.7 — TRAINING & PLACEMENT TRACK
# ============================================================
PAGES["training-placement.html"] = dict(
    title="Training & Placement Track | EDITH",
    description="Train, get placed, build a credit profile, access funding, and earn a project share over time — explained honestly, including what you commit to.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0362">EDITH-07 · Training-to-Placement Track</span></p>
    <h1><span data-i18n="t0363">A career-building pathway — explained honestly</span></h1>
    <p><span data-i18n="t0364">This goes further than an internship: you're trained, formally placed, and your credit profile is built over time — eventually earning a small ownership share in a project. Read exactly what that means before you apply.</span></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="step-timeline">
      <div class="step-timeline__item"><h3><span data-i18n="t0365">1. Train</span></h3><p><span data-i18n="t0366">Structured training in real construction operations.</span></p></div>
      <div class="step-timeline__item"><h3><span data-i18n="t0367">2. Get placed</span></h3><p><span data-i18n="t0368">A formal role within EDITH or a sister company.</span></p></div>
      <div class="step-timeline__item"><h3><span data-i18n="t0369">3. Build profile</span></h3><p><span data-i18n="t0370">EDITH helps build your financial credit profile over time — your track record of reliability that banks look at when lending.</span></p></div>
      <div class="step-timeline__item"><h3><span data-i18n="t0371">4. Access funding</span></h3><p><span data-i18n="t0372">EDITH arranges funding on your behalf as your profile strengthens.</span></p></div>
      <div class="step-timeline__item"><h3><span data-i18n="t0373">5. Earn a project share</span></h3><p><span data-i18n="t0374">An eventual small ownership stake in a project.</span></p></div>
    </div>

    <div class="example-box">
      <strong><span data-i18n="t0375">Read this before applying</span></strong>
      <span data-i18n="t0376">This is an unusually generous, career-building pathway — which is exactly why it needs to be explained honestly. In return, trainees commit to a minimum 3-year retention period with EDITH or a sister company, and any funding arranged on your behalf is repaid through a fixed monthly deduction from your project-share earnings, not your salary. Leaving before the minimum term converts remaining funding into a standard repayable loan.</span>
    </div>

    <details class="faq-item" open>
      <summary><span data-i18n="t0377">How it works — read before applying</span></summary>
      <p><span data-i18n="t0378">"Credit profile" here means EDITH reports your salary, tenure, and repayment conduct to help build the formal credit history banks use for loan eligibility — it is not a line of credit EDITH extends itself. "Funding" means EDITH arranging or co-signing project-related financing (such as a two-wheeler or tools loan) once your profile qualifies, capped per your placement grade. Eligibility opens after 12 months of placement with a clean performance record. In return, you commit to the minimum retention period above and to the repayment terms attached to any funding arranged on your behalf.</span></p>
    </details>
  </div>
</section>

<section class="section section--band">
  <div class="container" style="max-width:640px;">
    <form class="form-card" data-module="training-placement">
      <h2><span data-i18n="t0379">Apply to the Training-to-Placement Track</span></h2>
      <div class="consent-row">
        <input type="checkbox" id="tp-read" name="readExplainer" required>
        <label for="tp-read"><span data-i18n="t0380">I have read the "how it works" explainer above and understand what I am applying for and what I commit to.</span></label>
      </div>
      <div class="form-grid">
        <div class="field"><label for="tp-name"><span data-i18n="t0271">Name</span></label><input type="text" id="tp-name" name="name" required></div>
        <div class="field"><label for="tp-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="tp-phone" name="phone" required></div>
        <div class="field"><label for="tp-email"><span data-i18n="t0194">Email</span></label><input type="email" id="tp-email" name="email" required></div>
        <div class="field"><label for="tp-background"><span data-i18n="t0381">Current background</span></label><input type="text" id="tp-background" name="background"></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0332">Submit application</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="tp")),
)

# ============================================================
# 6.8 — PROPERTY & LAND MARKETPLACE
# ============================================================
PAGES["property-marketplace.html"] = dict(
    title="Property & Land Marketplace | EDITH",
    description="Browse flats, plots, and land across Andhra Pradesh and Telangana, or list your own property with EDITH's verified network.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0382">EDITH-08 · Property &amp; Land Marketplace</span></p>
    <h1><span data-i18n="t0383">Flats, plots, and land — browsed or listed, verified either way</span></h1>
    <p><span data-i18n="t0384">Every listing goes through moderation before it goes live. Are you an agent?</span> <a href="become-an-agent.html" style="color:var(--edith-gold-600);"><span data-i18n="t0385">Join the network here →</span></a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="listing-filters">
      <select aria-label="Type" data-i18n-attr-aria-label="t0386"><option><span data-i18n="t0387">All types</span></option><option><span data-i18n="t0388">Flat</span></option><option><span data-i18n="t0389">Plot</span></option><option><span data-i18n="t0390">Land</span></option><option><span data-i18n="t0391">Commercial</span></option></select>
      <select aria-label="Budget" data-i18n-attr-aria-label="t0392"><option><span data-i18n="t0393">Any budget</span></option><option><span data-i18n="t0394">Under ₹50L</span></option><option><span data-i18n="t0395">₹50L–1Cr</span></option><option><span data-i18n="t0204">Above ₹1Cr</span></option></select>
      <input type="text" placeholder="Location" data-i18n-attr-placeholder="t0396">
      <button class="btn btn-ghost"><span data-i18n="t0397">Filter</span></button>
    </div>

    <div class="listing-grid">
      <!-- Demo listings — real listings go live once moderation/CMS is wired up, §6.8, §11 -->
      <article class="listing-card">
        <span class="badge-verified" style="margin:var(--space-3) 0 0 var(--space-3);"><span data-i18n="t0398">Verified</span></span>
        <img src="assets/listing-placeholder-1.jpg" alt="Open plot, Shamshabad" data-i18n-attr-alt="t0399">
        <div class="listing-card__body">
          <h3><span data-i18n="t0400">Residential plot, HMDA-approved layout</span></h3>
          <p><span data-i18n="t0401">Shamshabad, Hyderabad · 200 sq.yd</span></p>
          <p class="listing-card__price">₹42,00,000</p>
        </div>
      </article>
      <article class="listing-card">
        <span class="badge-verified" style="margin:var(--space-3) 0 0 var(--space-3);"><span data-i18n="t0398">Verified</span></span>
        <img src="assets/listing-placeholder-2.jpg" alt="Agricultural land, Amaravati" data-i18n-attr-alt="t0402">
        <div class="listing-card__body">
          <h3><span data-i18n="t0403">Agricultural land, road-facing</span></h3>
          <p><span data-i18n="t0404">Amaravati, AP · 2.5 acres</span></p>
          <p class="listing-card__price">₹1,25,00,000</p>
        </div>
      </article>
      <article class="listing-card">
        <span class="badge-verified" style="margin:var(--space-3) 0 0 var(--space-3);"><span data-i18n="t0398">Verified</span></span>
        <img src="assets/listing-placeholder-3.jpg" alt="Commercial plot, Vijayawada" data-i18n-attr-alt="t0405">
        <div class="listing-card__body">
          <h3><span data-i18n="t0406">Commercial corner plot</span></h3>
          <p><span data-i18n="t0407">Vijayawada, AP · 350 sq.yd</span></p>
          <p class="listing-card__price">₹78,00,000</p>
        </div>
      </article>
    </div>

    <h2 style="margin-top:var(--space-8);"><span data-i18n="t0408">List your property or land</span></h2>
    <form class="form-card" data-module="property-listing" style="max-width:720px;">
      <div class="form-grid">
        <div class="field"><label for="lp-type"><span data-i18n="t0386">Type</span></label>
          <select id="lp-type" name="type"><option><span data-i18n="t0388">Flat</span></option><option><span data-i18n="t0389">Plot</span></option><option><span data-i18n="t0390">Land</span></option><option><span data-i18n="t0391">Commercial</span></option></select>
        </div>
        <div class="field"><label for="lp-location"><span data-i18n="t0396">Location</span></label><input type="text" id="lp-location" name="location" required></div>
        <div class="field"><label for="lp-extent"><span data-i18n="t0409">Extent</span></label><input type="text" id="lp-extent" name="extent" placeholder="e.g. 2.5 acres, 200 sq.yd, 6 cents" data-i18n-attr-placeholder="t0410"></div>
        <div class="field-hint form-grid--full"><span data-i18n="t0411">Supports sq.yd, sq.ft, acres, cents, and gunta — the common land-measurement units in Andhra Pradesh/Telangana (brief §6.8 flags this as critical).</span></div>
        <div class="field"><label for="lp-price"><span data-i18n="t0412">Price expectation (₹)</span></label><input type="number" id="lp-price" name="price"></div>
        <div class="field"><label for="lp-jv"><input type="checkbox" id="lp-jv" name="jvPotential" style="width:auto;display:inline;margin-right:0.4rem;"> <span data-i18n="t0413">Open to JV / development potential</span></label></div>
        <div class="field form-grid--full"><label for="lp-details"><span data-i18n="t0414">Key details</span></label><textarea id="lp-details" name="details"></textarea></div>
        <div class="field form-grid--full"><label for="lp-photos"><span data-i18n="t0415">Photos</span></label><input type="file" id="lp-photos" name="photos" multiple></div>
        <div class="field"><label for="lp-name"><span data-i18n="t0416">Your name</span></label><input type="text" id="lp-name" name="ownerName" required></div>
        <div class="field"><label for="lp-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="lp-phone" name="phone" required></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0417">Submit listing for review</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="listing")),
)

PAGES["become-an-agent.html"] = dict(
    title="Become an Agent | EDITH",
    description="Join EDITH's agent network — post listings directly and earn commission through a closed, trusted network.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0418">EDITH-08 · Agent Onboarding</span></p>
    <h1><span data-i18n="t0419">Post listings, earn commission, inside EDITH's own network</span></h1>
    <p><span data-i18n="t0420">Once approved, you get your own dashboard: post listings directly and see your commission terms. This connects to our</span> <a href="professional-services.html#rera" style="color:var(--edith-gold-600);"><span data-i18n="t0421">RERA agent-registration service</span></a> <span data-i18n="t0422">if you're not registered yet.</span></p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:640px;">
    <form class="form-card" data-module="agent-onboarding">
      <h2><span data-i18n="t0423">Agent registration</span></h2>
      <div class="form-grid">
        <div class="field"><label for="ag-name"><span data-i18n="t0271">Name</span></label><input type="text" id="ag-name" name="name" required></div>
        <div class="field"><label for="ag-area"><span data-i18n="t0424">Area covered</span></label><input type="text" id="ag-area" name="area" required></div>
        <div class="field"><label for="ag-rera"><span data-i18n="t0425">RERA agent number (if any)</span></label><input type="text" id="ag-rera" name="reraNumber"></div>
        <div class="field"><label for="ag-exp"><span data-i18n="t0354">Experience (years)</span></label><input type="number" id="ag-exp" name="experience"></div>
        <div class="field"><label for="ag-phone"><span data-i18n="t0193">Phone</span></label><input type="tel" id="ag-phone" name="phone" required></div>
        <div class="field"><label for="ag-email"><span data-i18n="t0194">Email</span></label><input type="email" id="ag-email" name="email" required></div>
      </div>
      __CONSENT__
      <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0426">Submit registration</span></button>
    </form>
  </div>
</section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="agent")),
)

# ============================================================
# 6.9 — BLOG / KNOWLEDGE HUB (nested one level: blog/index.html)
# ============================================================
PAGES["blog/index.html"] = dict(
    title="Knowledge Hub — Blog | EDITH",
    description="Myth-busting guides on GST, RERA, JDA, and land — in plain English and Tenglish, written by EDITH's CA/CS-led team.",
    prefix="../",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0427">EDITH-09 · Knowledge Hub</span></p>
    <h1><span data-i18n="t0428">Straight answers on GST, RERA, and land — no jargon</span></h1>
    <p><span data-i18n="t0429">Written by EDITH's own CA/CS-led team. Every post links to a related calculator and service — free content that's also genuinely useful.</span></p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="listing-filters">
      <span class="pill"><span data-i18n="t0430">Myth-busters</span></span><span class="pill"><span data-i18n="t0118">GST in practice</span></span><span class="pill"><span data-i18n="t0120">RERA &amp; legal</span></span>
      <span class="pill"><span data-i18n="t0431">JDA &amp; land</span></span><span class="pill"><span data-i18n="t0432">Home-buying guides</span></span><span class="pill"><span data-i18n="t0433">Investment basics</span></span>
      <span class="pill"><span data-i18n="t0434">Cost &amp; estimation</span></span><span class="pill"><span data-i18n="t0435">AP/Telangana rules</span></span>
    </div>
    <div class="blog-grid">
      <!-- Demo starter posts — real posts to be repurposed from EDITH's existing Reels, brief §6.9, §17 -->
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-1.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0118">GST in practice</span></span><h3><span data-i18n="t0119">GST on Under-Construction Flats: What You Actually Pay</span></h3></a>
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-2.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0120">RERA &amp; legal</span></span><h3><span data-i18n="t0121">How to Verify a Project's RERA Number Before You Book</span></h3></a>
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-3.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0122">Myth-buster</span></span><h3><span data-i18n="t0123">"Registration Value = Market Value" and Other Myths</span></h3></a>
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-4.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0431">JDA &amp; land</span></span><h3><span data-i18n="t0436">JDA vs. Outright Sale: Which Suits Your Land Better?</span></h3></a>
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-5.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0433">Investment basics</span></span><h3><span data-i18n="t0437">Discounted Flat or Monetary Return — How to Choose</span></h3></a>
      <a class="blog-card" href="#"><img src="../assets/blog-placeholder-6.jpg" alt=""><span class="blog-card__tag"><span data-i18n="t0435">AP/Telangana rules</span></span><h3><span data-i18n="t0438">Stamp Duty &amp; Registration Charges in AP, Explained</span></h3></a>
    </div>
    <p class="field-hint" style="margin-top:var(--space-6);"><span data-i18n="t0439">Each post (once written) should include: a summary box up top, a "watch the 60-second version" embed of the matching Reel, a link to a related calculator, a related service CTA, an author credibility line, and share buttons — plus full Telugu and Tenglish versions (brief §6.9, §9).</span></p>
  </div>
</section>
""",
)

# ============================================================
# CALCULATORS INDEX — brief §8, 10 total
# ============================================================
PAGES["calculators.html"] = dict(
    title="Calculators & Tools | EDITH",
    description="Ten free calculators — construction cost, land-unit conversion, home-loan EMI, stamp duty, GST, JDA share, ROI, rental yield, plot vs flat, and feasibility.",
    body="""
<section class="page-hero">
  <div class="container">
    <p class="page-hero__eyebrow"><span data-i18n="t0440">EDITH-09 · Calculators &amp; Tools</span></p>
    <h1><span data-i18n="t0441">Ten calculators, one purpose: answer a real question fast</span></h1>
    <p><span data-i18n="t0442">No login, no waiting. Every calculator below carries the same disclaimer: indicative and for general information only.</span></p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="calc-teaser" style="margin-bottom: var(--space-8);">
      <div><h2><span data-i18n="t0443">Construction cost estimator</span></h2><p><span data-i18n="t0444">Built-up area, quality tier, and floor count → a total cost range.</span> <strong><span data-i18n="t0445">Live now</span></strong> <span data-i18n="t0446">— see the homepage teaser or use it inline below.</span></p></div>
      <div class="calc-card">
        <form id="costCalcForm">
          <div class="calc-field"><label for="builtUpArea"><span data-i18n="t0105">Built-up area (sq. ft.)</span></label><input type="number" id="builtUpArea" min="100" step="10" value="1500" required></div>
          <div class="calc-field"><label for="qualityTier"><span data-i18n="t0106">Quality tier</span></label><select id="qualityTier"><option value="basic"><span data-i18n="t0107">Basic</span></option><option value="standard" selected><span data-i18n="t0108">Standard</span></option><option value="premium"><span data-i18n="t0109">Premium</span></option></select></div>
          <div class="calc-field"><label for="floors"><span data-i18n="t0110">Number of floors</span></label><input type="number" id="floors" min="1" max="10" value="1" required></div>
          <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0447">Calculate</span></button>
        </form>
        <div class="calc-result" id="calcResult" hidden><strong id="calcTotal">—</strong><span id="calcBreakdown">—</span></div>
        <p class="disclaimer"><span data-i18n="t0448">Indicative and for general information only; not professional, legal, tax or investment advice.</span></p>
      </div>
    </div>

    <div class="offer-grid">
      <div class="offer-card"><h3><span data-i18n="t0449">Land-unit converter</span></h3><p><span data-i18n="t0450">sq.ft ⇄ sq.yd ⇄ cent ⇄ acre ⇄ gunta.</span></p><span class="offer-card__price"><span data-i18n="t0451">Live below</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0452">Home-loan EMI</span></h3><p><span data-i18n="t0453">Loan amount, rate, tenure → monthly EMI + amortisation summary.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0455">Stamp duty &amp; registration (AP)</span></h3><p><span data-i18n="t0456">Property value, type, location slab → all-in registration cost.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0457">GST on under-construction property</span></h3><p><span data-i18n="t0458">Property value + project type → applicable GST.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0459">JDA share calculator</span></h3><p><span data-i18n="t0460">Land extent, ratio, saleable rate → landowner vs. developer share.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0461">Investor ROI projection</span></h3><p><span data-i18n="t0462">Investment amount, model, tenure → a projected outcome range.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0463">Rental yield</span></h3><p><span data-i18n="t0464">Property price + monthly rent → gross and net yield.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0465">Plot vs. flat comparison</span></h3><p><span data-i18n="t0466">Prices, appreciation, and rent assumptions → side-by-side projection.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
      <div class="offer-card"><h3><span data-i18n="t0467">Feasibility / break-even</span></h3><p><span data-i18n="t0468">Land + construction cost, saleable area → break-even rate per sq.ft.</span></p><span class="offer-card__price"><span data-i18n="t0454">Coming soon</span></span></div>
    </div>

    <div class="calc-card" style="max-width:520px; margin-top:var(--space-8);">
      <h3><span data-i18n="t0449">Land-unit converter</span></h3>
      <form id="landConvForm">
        <div class="calc-field"><label for="lc-value"><span data-i18n="t0469">Value</span></label><input type="number" id="lc-value" value="1" step="0.01"></div>
        <div class="calc-field"><label for="lc-unit"><span data-i18n="t0470">Unit</span></label>
          <select id="lc-unit"><option value="acre"><span data-i18n="t0471">Acre</span></option><option value="cent"><span data-i18n="t0472">Cent</span></option><option value="sqyd"><span data-i18n="t0473">Sq. yard</span></option><option value="sqft"><span data-i18n="t0474">Sq. foot</span></option><option value="gunta"><span data-i18n="t0475">Gunta</span></option></select>
        </div>
        <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0476">Convert</span></button>
      </form>
      <div class="calc-result" id="landConvResult" hidden><span id="landConvOut">—</span></div>
      <p class="disclaimer"><span data-i18n="t0477">Indicative and for general information only.</span></p>
    </div>

    <p class="field-hint" style="margin-top:var(--space-6);"><span data-i18n="t0478">Every rate/slab above must be admin-editable once the admin panel exists, per brief §8 — never hard-coded permanently in a JS file (see README).</span></p>
  </div>
</section>
""",
    extra_scripts='<script src="js/calculator.js"></script>\n<script src="js/land-converter.js"></script>',
)

# ============================================================
# SECONDARY / STANDALONE PAGES
# ============================================================
PAGES["about.html"] = dict(
    title="About & Track Record | EDITH",
    description="EDITH's registration details, track record, and the team behind the brand.",
    body="""
<section class="page-hero"><div class="container">
  <p class="page-hero__eyebrow"><span data-i18n="t0025">About &amp; Track Record</span></p>
  <h1><span data-i18n="t0479">The credibility engine behind every module</span></h1>
  <p><span data-i18n="t0480">EDITH is CA/CS-led — every arrangement across all nine streams is backed by the same compliance and financial rigor.</span></p>
</div></section>
<section class="section"><div class="container">
  <div class="trust-strip__stats" style="color:var(--edith-navy-900);">
    <div class="trust-stat"><strong style="color:var(--edith-gold-600);">8+</strong><span><span data-i18n="t0043">Years active</span></span></div>
    <div class="trust-stat"><strong style="color:var(--edith-gold-600);">42</strong><span><span data-i18n="t0044">Projects delivered</span></span></div>
    <div class="trust-stat"><strong style="color:var(--edith-gold-600);">18L</strong><span><span data-i18n="t0045">Sq. ft. built</span></span></div>
    <div class="trust-stat"><strong style="color:var(--edith-gold-600);">6</strong><span><span data-i18n="t0046">Cities served</span></span></div>
  </div>
  <h2 style="margin-top:var(--space-8);"><span data-i18n="t0481">Registration details</span></h2>
  <p><span data-i18n="t0482">CIN: U43900AP2023PTC111419 · RERA: Applied For · GST: 37AAHCE6199E1ZA</span></p>
  <h2><span data-i18n="t0483">Our story</span></h2>
  <p><span data-i18n="t0484">EDITH started in 2018 as an in-house CA/CS compliance desk for a single Visakhapatnam builder. As other builders and agents began asking for the same rigor, EDITH grew into a nine-module platform spanning investment, construction JVs, compliance services, and career pathways for engineers and students — all run on the same discipline that keeps its own projects RERA-clean, still headquartered in Visakhapatnam today.</span></p>
</div></section>
""",
)

PAGES["contact.html"] = dict(
    title="Contact | EDITH",
    description="Get in touch with EDITH — phone, WhatsApp, email, and office address.",
    body="""
<section class="page-hero"><div class="container">
  <p class="page-hero__eyebrow"><span data-i18n="t0026">Contact</span></p><h1><span data-i18n="t0485">Talk to us</span></h1>
  <p><span data-i18n="t0486">Phone: +91 89775 30174 · WhatsApp: +91 89775 30174 · Email: hello@edith.in</span></p>
</div></section>
<section class="section"><div class="container split-layout">
  <div>
    <h2><span data-i18n="t0487">Offices</span></h2>
    <div class="office-block office-block--hq">
      <span class="office-block__tag"><span data-i18n="t0569">HQ</span></span>
      <p><span data-i18n="t0567">Door No 49-58-6/2, Sree Maan Sree Nidhi Nilayam, Green Park Colony, Balayya Sastri Layout, P &amp; T Colony (VM), Visakhapatnam, Andhra Pradesh 530013</span></p>
    </div>
    <div class="office-block">
      <span class="office-block__tag"><span data-i18n="t0568">Regional office</span></span>
      <p><span data-i18n="t0488">3rd Floor, Sundaram Towers, Kondapur Main Road, Hyderabad, Telangana 500084</span></p>
    </div>
    <p><span data-i18n="t0489">(Map embed to be added once the addresses above are confirmed by EDITH.)</span></p>
  </div>
  <form class="form-card" data-module="general-contact">
    <h2><span data-i18n="t0490">Send a message</span></h2>
    <div class="field"><label for="c-name"><span data-i18n="t0271">Name</span></label><input type="text" id="c-name" name="name" required></div>
    <div class="field"><label for="c-email"><span data-i18n="t0194">Email</span></label><input type="email" id="c-email" name="email" required></div>
    <div class="field"><label for="c-message"><span data-i18n="t0491">Message</span></label><textarea id="c-message" name="message" required></textarea></div>
    __CONSENT__
    <button type="submit" class="btn btn-primary btn-block"><span data-i18n="t0492">Send</span></button>
  </form>
</div></section>
""".replace("__CONSENT__", CONSENT_ROW.format(id="contact")),
)

PAGES["careers.html"] = dict(
    title="Careers | EDITH",
    description="Open roles at EDITH, across construction, compliance, and technology.",
    body="""
<section class="page-hero"><div class="container">
  <p class="page-hero__eyebrow"><span data-i18n="t0493">Grow with us · Careers</span></p><h1><span data-i18n="t0494">Open roles at EDITH</span></h1>
  <p><span data-i18n="t0495">We're currently hiring for Site Engineer, RERA/GST Compliance Associate, and CRM Executive roles across Hyderabad and Vijayawada. Looking for hands-on site experience instead? See</span> <a href="internships.html" style="color:var(--edith-gold-600);"><span data-i18n="t0018">Student Internships</span></a> <span data-i18n="t0496">or the</span> <a href="training-placement.html" style="color:var(--edith-gold-600);"><span data-i18n="t0068">Training-to-Placement Track</span></a>.</p>
</div></section>
""",
)

PAGES["faqs.html"] = dict(
    title="FAQs | EDITH",
    description="Common questions about investing, joint ventures, services, and careers with EDITH.",
    body="""
<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0497">Learn · FAQs</span></p><h1><span data-i18n="t0498">Frequently asked questions</span></h1></div></section>
<section class="section"><div class="container" style="max-width:760px;">
  <details class="faq-item"><summary><span data-i18n="t0499">Is my investment guaranteed?</span></summary><p><span data-i18n="t0500">No — EDITH never uses the words "assured" or "guaranteed returns" for any investment. All figures are illustrative only (brief §16).</span></p></details>
  <details class="faq-item"><summary><span data-i18n="t0501">How is my money protected as an investor?</span></summary><p><span data-i18n="t0502">Through a per-project SPV structure and signed agreements — see the</span> <a href="invest-with-us.html"><span data-i18n="t0503">Invest With Us</span></a> <span data-i18n="t0504">page for detail.</span></p></details>
  <details class="faq-item"><summary><span data-i18n="t0505">Is this a franchise?</span></summary><p><span data-i18n="t0506">No. The Civil Engineer Partnership is an "Authorised Partner" / "Channel Associate" arrangement, deliberately not a legal franchise (brief §6.6, §16).</span></p></details>
  <details class="faq-item"><summary><span data-i18n="t0507">Which cities does EDITH operate in?</span></summary><p><span data-i18n="t0508">EDITH currently operates across Andhra Pradesh and Telangana, with active projects in Hyderabad, Vijayawada, and Amaravati.</span></p></details>
</div></section>
""",
)

PAGES["privacy-policy.html"] = dict(
    title="Privacy Policy | EDITH",
    description="How EDITH collects, uses, and protects personal data, per India's DPDP Act 2023.",
    body="""
<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0152">Legal</span></p><h1><span data-i18n="t0153">Privacy Policy</span></h1></div></section>
<section class="section"><div class="container" style="max-width:760px;">
  <p class="example-box"><strong><span data-i18n="t0509">Not yet lawyer-reviewed</span></strong> <span data-i18n="t0510">This is placeholder structure only — brief §16 requires every policy below to be reviewed by a qualified lawyer before go-live.</span></p>
  <p><span data-i18n="t0511">EDITH ("we", "us") collects the information you submit through any form on this site — including your name, phone number, email, and details relevant to that module (investment interest, JV proposal, service request, application, or listing) — solely to respond to your enquiry and administer the relevant service. By checking the consent box on a form, you agree to this collection and to EDITH contacting you, as required under India's Digital Personal Data Protection Act, 2023.</span></p>
  <p><span data-i18n="t0512">Data is stored on access-controlled systems and is visible only to the EDITH team members responsible for the module you contacted us about (e.g., only the compliance team sees Professional Services enquiries). We do not sell your data to third parties. You may request access to, correction of, or deletion of your data at any time by writing to</span> <a href="contact.html"><span data-i18n="t0513">our contact page</span></a><span data-i18n="t0514">. This page is a structural placeholder pending full legal review before go-live.</span></p>
</div></section>
""",
)

PAGES["terms.html"] = dict(
    title="Terms of Use | EDITH", description="Terms of use for the EDITH website and platform.",
    body="""<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0152">Legal</span></p><h1><span data-i18n="t0154">Terms of Use</span></h1></div></section>
<section class="section"><div class="container" style="max-width:760px;"><p class="example-box"><strong><span data-i18n="t0515">Not yet lawyer-reviewed.</span></strong></p><p><span data-i18n="t0516">By using this website, you agree to use it only for lawful purposes connected to EDITH's nine service modules. Content, branding, and calculator tools on this site are the property of EDITH and may not be reproduced without permission. Figures shown by calculators, quote tools, and illustrative examples are indicative only and do not constitute a binding offer — a binding offer is made only through a signed agreement specific to your project or transaction. EDITH may update these terms from time to time; continued use of the site after an update constitutes acceptance of the revised terms.</span></p></div></section>""",
)

PAGES["disclaimer.html"] = dict(
    title="Disclaimer | EDITH", description="General disclaimer covering calculators, quotes, and advisory content on the EDITH website.",
    body="""<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0152">Legal</span></p><h1><span data-i18n="t0155">Disclaimer</span></h1></div></section>
<section class="section"><div class="container" style="max-width:760px;">
<p><span data-i18n="t0517">Every calculator, blog post, and quote on this site is indicative and for general information only — not professional, legal, tax, or investment advice. Quotes are estimates subject to confirmation via an actual site visit (brief §16).</span></p>
<p class="example-box"><strong><span data-i18n="t0515">Not yet lawyer-reviewed.</span></strong> <span data-i18n="t0518">EDITH never uses the words "guaranteed" or "assured returns" for any investment, JV, or funding-related outcome. All illustrative examples, ROI ranges, and calculator outputs are estimates based on stated assumptions and general market conditions — actual outcomes depend on the specific project, agreement terms, and market movement at the time. Nothing on this site constitutes legal, tax, financial, or investment advice; please consult your own advisor before making a decision. Quotes generated through the Get a Quote tool are preliminary and subject to confirmation after an actual site visit.</span></p>
</div></section>""",
)

PAGES["refund-policy.html"] = dict(
    title="Refund / Cancellation Policy | EDITH", description="Refund and cancellation terms for EDITH's paid professional and consumer services.",
    body="""<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0152">Legal</span></p><h1><span data-i18n="t0519">Refund / Cancellation Policy</span></h1></div></section>
<section class="section"><div class="container" style="max-width:760px;"><p class="example-box"><strong><span data-i18n="t0515">Not yet lawyer-reviewed.</span></strong></p><p><span data-i18n="t0520">This policy applies to paid services booked under Professional &amp; Compliance Services (e.g., RERA/agent registration, GST advisory, filings) and any paid Consumer Services. A full refund is available if work has not yet commenced. Once work has commenced, fees already incurred for statutory filings or third-party costs are non-refundable, and remaining fees are refunded on a pro-rata basis. Cancellation requests must be sent in writing to</span> <a href="contact.html"><span data-i18n="t0513">our contact page</span></a><span data-i18n="t0521">; refunds are processed within 7–10 working days to the original payment method.</span></p></div></section>""",
)

PAGES["sitemap.html"] = dict(
    title="Sitemap | EDITH", description="Full list of pages on the EDITH website.",
    body="""<section class="page-hero"><div class="container"><p class="page-hero__eyebrow"><span data-i18n="t0157">Sitemap</span></p><h1><span data-i18n="t0522">Every page, one list</span></h1></div></section>
<section class="section"><div class="container">
<div class="offer-grid">
<div><h3><span data-i18n="t0144">Collaborate</span></h3><ul><li><a href="invest-with-us.html"><span data-i18n="t0005">Invest with us</span></a></li><li><a href="builder-jv.html"><span data-i18n="t0006">Builder JV</span></a></li><li><a href="engineer-partnership.html"><span data-i18n="t0007">Engineer Partnership</span></a></li><li><a href="property-marketplace.html"><span data-i18n="t0145">List Property/Land</span></a></li><li><a href="become-an-agent.html"><span data-i18n="t0009">Become an Agent</span></a></li></ul></div>
<div><h3><span data-i18n="t0146">Services</span></h3><ul><li><a href="get-a-quote.html"><span data-i18n="t0016">Get a Quote</span></a></li><li><a href="professional-services.html"><span data-i18n="t0523">Professional Services</span></a></li></ul></div>
<div><h3><span data-i18n="t0148">Grow &amp; Learn</span></h3><ul><li><a href="internships.html"><span data-i18n="t0524">Internships</span></a></li><li><a href="training-placement.html"><span data-i18n="t0149">Training &amp; Placement</span></a></li><li><a href="careers.html"><span data-i18n="t0020">Careers</span></a></li><li><a href="blog/index.html"><span data-i18n="t0150">Blog</span></a></li><li><a href="calculators.html"><span data-i18n="t0151">Calculators</span></a></li><li><a href="faqs.html"><span data-i18n="t0024">FAQs</span></a></li></ul></div>
<div><h3><span data-i18n="t0525">Other</span></h3><ul><li><a href="about.html"><span data-i18n="t0526">About</span></a></li><li><a href="contact.html"><span data-i18n="t0026">Contact</span></a></li><li><a href="privacy-policy.html"><span data-i18n="t0153">Privacy Policy</span></a></li><li><a href="terms.html"><span data-i18n="t0527">Terms</span></a></li><li><a href="disclaimer.html"><span data-i18n="t0155">Disclaimer</span></a></li><li><a href="refund-policy.html"><span data-i18n="t0528">Refund Policy</span></a></li></ul></div>
</div>
</div></section>""",
)
