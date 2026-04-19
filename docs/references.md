# Thesis Reference Library

> **Student:** Cheuk Fung Donald Man · **Module:** MEng Individual Research Project · **Supervisor:** Dr. Po-Heng Lee · **Thesis title:** *Data-Driven Analysis of HVAC Decarbonisation Pathways in Commercial Office Buildings Under Climate Change*

This file is the canonical bibliography for the thesis. Every numeric or qualitative claim in a notebook markdown cell or thesis chapter draft cites a **short-key** from this file (e.g. `[IPCC_AR6_Ch9]`). New sources are added here *in the same commit* as the work that uses them.

---

## Contents

- [How to use this file](#how-to-use-this-file)
- [Pillar A — Climate Change Impact on HVAC Demand](#pillar-a--climate-change-impact-on-hvac-demand)
- [Pillar B — Grid Carbon Intensity & Demand Response](#pillar-b--grid-carbon-intensity--demand-response)
- [Pillar C — Retrofit MACC & Carbon Pricing](#pillar-c--retrofit-macc--carbon-pricing)
- [Reference-to-notebook mapping](#reference-to-notebook-mapping)
- [Sources flagged for primary-source verification](#sources-flagged-for-primary-source-verification)
- [Style conventions](#style-conventions)

---

## How to use this file

**Short-key format:** `[FirstAuthorLastNameYYYY]` or `[Org-YYYY-Topic]`.

**Each entry contains:**
- Full citation (authors, year, title)
- Venue (journal / publisher / report number)
- DOI or stable URL
- **Finding** — the exact quantitative or qualitative claim being cited
- **Use** — the notebook(s) or chapter(s) where the finding appears

**Maintenance rule:** when a new reference is discovered or a stat is used in the write-up, add it here in the commit that introduces it. Entries flagged `[needs verification]` must be re-checked against primary source before final thesis quote.

---

## Pillar A — Climate Change Impact on HVAC Demand

### `[Isaac2009]`
Isaac, M. & van Vuuren, D.P., 2009 — *Modeling global residential sector energy demand for heating and air conditioning in the context of climate change.*
**Venue:** Energy Policy, 37(2), 507–521.
**DOI:** https://doi.org/10.1016/j.enpol.2008.09.051
**Finding:** Global heating demand −34% and cooling demand +72% by 2100 due to climate change alone.
**Use:** Canonical global baseline for asymmetric heating-vs-cooling warming response — Chapter 1 framing; nb 05 discussion.

### `[VanRuijven2019]`
van Ruijven, B.J., De Cian, E. & Sue Wing, I., 2019 — *Amplification of future energy demand growth due to climate change.*
**Venue:** Nature Communications, 10, 2762.
**DOI:** https://doi.org/10.1038/s41467-019-10399-3
**Finding:** Vigorous (moderate) warming lifts climate-exposed energy demand 25–58% (11–27%) above socio-economic baseline by 2050; >25% rises across southern US.
**Use:** Justifies climate-contribution quantification in nb 05 §4; Chapter 1 stat.

### `[Santamouris2014]`
Santamouris, M., 2014 — *On the energy impact of urban heat island and global warming on buildings.*
**Venue:** Energy and Buildings, 82, 100–113.
**DOI:** https://doi.org/10.1016/j.enbuild.2014.07.022
**Finding:** Urban cooling demand ~13% higher than rural equivalents; ~0.7 kWh/m² per K cooling-energy elasticity.
**Use:** Elasticity anchor for interpreting AlphaBuilding 18-year CDD sensitivity (nb 05 §3).

### `[Dirks2015]`
Dirks, J.A., Gorrissen, W.J., Hathaway, J.H., Skorski, D.R., Scott, M.J., Pulsipher, T.C., Huang, M., Liu, Y. & Rice, J.S., 2015 — *Impacts of climate change on energy consumption and peak demand in buildings: a detailed regional approach.*
**Venue:** Energy, 79, 20–32.
**DOI:** https://doi.org/10.1016/j.energy.2014.08.081
**Finding:** State-level summer electricity demand rises >50% by 2080–99; fixed 18.3 °C balance point overstates change by up to 14 pp in Oregon.
**Use:** Critiques fixed CDD base temperature — supports sensitivity test in nb 05 §2.

### `[IPCC_AR6_Ch9]`
Cabeza, L.F., Bai, Q., Ürge-Vorsatz, D. et al., 2022 — *Chapter 9: Buildings.* In: IPCC, 2022: Climate Change 2022: Mitigation of Climate Change. Contribution of WG III to the Sixth Assessment Report of the IPCC.
**Venue:** Cambridge University Press.
**DOI:** https://doi.org/10.1017/9781009157926.011
**URL:** https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-9/
**Finding:** Buildings = 31% of global final energy + 21% of GHG emissions (2019); cooling end-use grew ~75% from 1990–2019 (fastest-growing thermal service). `[needs verification — Section 9.3 PDF]`
**Use:** Chapter 1 authoritative building-sector framing; replaces the colloquial "buildings 40%" figure used in CLAUDE.md.

### `[IEA2018_FoC]`
International Energy Agency, 2018 — *The Future of Cooling: Opportunities for Energy-Efficient Air Conditioning.*
**Venue:** IEA, Paris (CC BY 4.0).
**URL:** https://www.iea.org/reports/the-future-of-cooling
**Finding:** Global space-cooling energy demand more than triples by 2050; AC stock grows from 1.6 B to 5.6 B units; cooling ~20% of today's buildings electricity.
**Use:** Chapter 1 headline motivator; nb 05 projection discussion.

### `[IEA2024_Urban]`
International Energy Agency, 2024 — *Empowering Urban Energy Transitions: Cities and grids on a heating planet.*
**Venue:** IEA, Paris.
**URL:** https://www.iea.org/reports/empowering-urban-energy-transitions
**Finding:** Installed space-cooling capacity 850 GW (2023) nearly doubles by 2030; cooling ~30% of peak demand in ASEAN by 2040.
**Use:** Post-2018 trajectory update — climate-driven peak demand argument (Chapter 1, nb 06 peak coincidence).

### `[EPA2021_CDD]`
US Environmental Protection Agency, 2021 — *Climate Change Indicators: Heating and Cooling Degree Days (Technical Documentation).*
**Venue:** EPA Climate Change Indicators Program.
**URL:** https://www.epa.gov/climate-indicators/climate-change-indicators-heating-and-cooling-degree-days
**Finding:** Contiguous-US HDD declining at −4.59 dd/yr and CDD rising at +1.59 dd/yr (1895–2020); 44 states show significant HDD decline, 29 show significant CDD rise.
**Use:** Primary observational evidence for nb 05 CDD/HDD trend analysis across FL/CA/IL.

### `[Biardeau2020]`
Biardeau, L.T., Davis, L.W., Deschenes, O. & Gonzalez, C., 2020 — *Heat exposure and global air conditioning.*
**Venue:** Nature Sustainability, 3(1), 25–28.
**DOI:** https://doi.org/10.1038/s41893-019-0441-9
**Finding:** Ranks 219 countries / 1,692 cities by total CDD exposure (base 18.3 °C); US uses 400 TWh/yr for AC; 8 developing countries now exceed US total CDD exposure.
**Use:** Defines CDD18 exposure metric; Miami cooling-intensity benchmarking (nb 05).

### `[Petri2015]`
Petri, Y. & Caldeira, K., 2015 — *Impacts of global warming on residential heating and cooling degree-days in the United States.*
**Venue:** Scientific Reports, 5, 12427.
**DOI:** https://doi.org/10.1038/srep12427
**Finding:** Per 1 °C global warming, US population-weighted CDD18 rises ~20% and HDD18 falls ~10%; strongest cooling elasticity in the Southeast (Florida). `[needs verification — exact %]`
**Use:** US-specific CDD/HDD elasticities benchmarking AlphaBuilding-derived sensitivities (nb 05 §3).

### `[Sailor2003]`
Sailor, D.J. & Pavlova, A.A., 2003 — *Air conditioning market saturation and long-term response of residential cooling energy demand to climate change.*
**Venue:** Energy, 28(9), 941–951.
**DOI:** https://doi.org/10.1016/S0360-5442(03)00033-1
**Finding:** AC tipping-temperature varies 14 °C (North) to 21 °C (Florida) across 39 US cities.
**Use:** Empirical support for location-specific base-temperature selection (nb 05 §2 sensitivity).

### `[DayGD2017]`
Day, A.R. & Karayiannis, T.G., 2017 — *Degree-day based non-domestic building energy analytics and modelling should use building and type-specific base temperatures.*
**Venue:** Energy and Buildings, 158, 874–881.
**DOI:** https://doi.org/10.1016/j.enbuild.2017.10.072
**Finding:** Empirical base temperatures span 11.6 °C (storage) to 20.5 °C (office); UK default 15.5 °C can understate non-domestic heating materially.
**Use:** Critiques the fixed 18 °C CDD / 15 °C HDD convention for commercial offices (nb 05 §2).

---

## Pillar B — Grid Carbon Intensity & Demand Response

### `[eGRID2022]`
US Environmental Protection Agency, 2024 — *eGRID Technical Guide with Year 2022 Data.*
**Venue:** EPA Clean Air Markets Division Technical Support Document (Jan 2024).
**URL:** https://www.epa.gov/system/files/documents/2024-01/egrid2022_technical_guide.pdf
**Finding:** CO₂ / CH₄ / N₂O factors at plant, state, balancing authority, subregion, NERC and national levels; eGRID2022 revised plant-to-subregion assignment to follow where power is *supplied*.
**Use:** Primary source for annual subregion emissions factors (nb 06 baseline emissions accounting).

### `[Cambium2023]`
Gagnon, P., Sanchez Perez, P.A., Obika, K., Schwarz, M., Morris, J., Gu, J. & Eisenman, J., 2024 — *Cambium 2023 Scenario Descriptions and Documentation.*
**Venue:** NREL Technical Report NREL/TP-6A40-88507.
**URL:** https://docs.nrel.gov/docs/fy24osti/88507.pdf
**Finding:** Hourly CO₂ intensity + LRMER projections to 2050 across 18 GEA regions; scenarios span mid-case through 95%-by-2050 decarbonisation.
**Use:** Hourly grid carbon profiles per climate-matched region for carbon-optimal scheduling (nb 06, nb 07).

### `[LRMER2023]`
Gagnon, P., Cowiestoll, B. & Schwarz, M., 2023 — *Long-run Marginal Emission Rates for Electricity: Workbooks for 2023 Cambium Data.*
**Venue:** NREL Data Catalog (OSTI 2305481) — dataset accompanying Cambium 2023.
**URL:** https://data.nrel.gov/submissions/230
**Finding:** LRMER captures both operational and structural grid response to a demand change — distinct from short-run marginal.
**Use:** Methodological basis for defensible CO₂-savings attribution from load-shifting (nb 06, nb 07).

### `[SilerEvans2012]`
Siler-Evans, K., Azevedo, I.L. & Morgan, M.G., 2012 — *Marginal Emissions Factors for the U.S. Electricity System.*
**Venue:** Environmental Science & Technology, 46(9), 4742–4748.
**DOI:** https://doi.org/10.1021/es300145v
**Finding:** First systematic regional MEFs from hourly CEMS (2006–2011); average EFs can "grossly misestimate" avoided emissions; large regional + hour-of-day variation.
**Use:** Canonical justification for using marginal (not average) emissions when evaluating load-shifting (nb 06 methods, Chapter 2 literature review).

### `[Ryan2016]`
Ryan, N.A., Johnson, J.X. & Keoleian, G.A., 2016 — *Comparative Assessment of Models and Methods To Calculate Grid Electricity Emissions.*
**Venue:** Environmental Science & Technology, 50(17), 8937–8953.
**DOI:** https://doi.org/10.1021/acs.est.5b05216
**Finding:** Reviews 32 EF methods; at a given site, 10 methods yield up to 68% spread from mean CO₂ EF.
**Use:** Motivates multi-lens emissions accounting (nb 06 reports both average and marginal).

### `[Hawkes2010]`
Hawkes, A.D., 2010 — *Estimating Marginal CO₂ Emissions Rates for National Electricity Systems.*
**Venue:** Energy Policy, 38(10), 5977–5987.
**DOI:** https://doi.org/10.1016/j.enpol.2010.05.053
**Finding:** GB MEF ≈ 0.69 kgCO₂/kWh (2002–2009, ±10%); MEFs diverge from average EFs especially for peak-shifting.
**Use:** European/GB anchor for marginal-vs-average generalisation (Chapter 2 lit review).

### `[Braun1990]`
Braun, J.E., 1990 — *Reducing Energy Costs and Peak Electrical Demand through Optimal Control of Building Thermal Storage.*
**Venue:** ASHRAE Transactions, 96(2), 876–888.
**URL:** https://www.semanticscholar.org/paper/cf88bba94d6e383c1e6e1afd489cff90ecd39d06
**Finding:** Optimal precooling using structural mass → up to 40% peak cooling-load reduction and 51% daily cooling-load shift to off-peak.
**Use:** Seminal demonstration of commercial thermal mass as grid resource (nb 07 flexibility envelope; Chapter 2). `[paywalled primary — cited via secondary sources]`

### `[Kircher2015]`
Kircher, K.J. & Zhang, K.M., 2015 — *Model Predictive Control of Thermal Storage for Demand Response.*
**Venue:** Proc. 2015 American Control Conference, Chicago, pp. 956–961, IEEE.
**DOI:** https://doi.org/10.1109/ACC.2015.7170857
**Finding:** Convex MPC combining dynamic price + demand charge + DR → ~25% peak-hour energy cut and ~50% demand-charge cut with ice storage.
**Use:** Heavyweight MPC benchmark against which this thesis's lighter carbon-signal overlay is positioned (Chapter 2; archived nb 05 Limitations discussion).

### `[Reynders2017]`
Reynders, G., Diriken, J. & Saelens, D., 2017 — *Generic Characterization Method for Energy Flexibility: Applied to Structural Thermal Storage in Residential Buildings.*
**Venue:** Applied Energy, 198, 192–202.
**DOI:** https://doi.org/10.1016/j.apenergy.2017.04.061
**Finding:** Three quantitative flexibility metrics — available storage capacity (kWh), storage efficiency (%), power-shifting capability (kW × duration).
**Use:** Vocabulary for per-climate flexibility envelopes (nb 07 §2).

### `[Pean2019]`
Péan, T.Q., Salom, J. & Costa-Castelló, R., 2019 — *Review of Control Strategies for Improving the Energy Flexibility Provided by Heat Pump Systems in Buildings.*
**Venue:** Journal of Process Control, 74, 35–49.
**DOI:** https://doi.org/10.1016/j.jprocont.2018.03.006
**Finding:** Review of rule-based vs MPC strategies; economic / price objectives dominate, **CO₂-signal objectives are rare** — carbon-aware control identified as under-served.
**Use:** **LITERATURE GAP CITATION** — precise under-served topic the thesis addresses (Chapter 1, Chapter 2, archived nb 05 preamble).

### `[Arteconi2012]`
Arteconi, A., Hewitt, N.J. & Polonara, F., 2012 — *State of the Art of Thermal Storage for Demand-Side Management.*
**Venue:** Applied Energy, 93, 371–389.
**DOI:** https://doi.org/10.1016/j.apenergy.2011.12.045
**Finding:** Peak-shifting potentials of 10–40% across TES-enabled DSM for residential + commercial sectors.
**Use:** Establishes thermal storage as legitimate grid-facing resource (Chapter 2).

### `[Neukomm2019]`
Neukomm, M., Nubbe, V. & Fares, R., 2019 — *Grid-Interactive Efficient Buildings.*
**Venue:** US DOE / BTO Technical Report DOE/EE-1968.
**DOI:** https://doi.org/10.2172/1508212
**Finding:** Defines GEBs as efficient, connected, smart, flexible; introduces the BTO GEB Technical Report Series. `[Specific flexibility-MW figures live in companion sub-reports — needs verification for any single percentage]`
**Use:** Canonical US policy framing for carbon-aware scheduling (Chapter 1, Chapter 2).

### `[Satchwell2021]`
Satchwell, A., Piette, M.A., Khandekar, A., Granderson, J. et al. (15 authors), 2021 — *A National Roadmap for Grid-Interactive Efficient Buildings.*
**Venue:** LBNL / US DOE Report, May 2021 (OSTI 1784302).
**URL:** https://gebroadmap.lbl.gov/A%20National%20Roadmap%20for%20GEBs%20-%20Final.pdf
**Finding:** GEB deployment 2021–2040 → $100–200 B cumulative power-system savings; ~80 Mt CO₂/yr reduction by 2030 (~6% of US power-sector CO₂).
**Use:** Macro-scale CO₂ prize — headline statistic for Chapter 1 and Conclusions.

### `[Radovanovic2021]`
Radovanović, A., Koningstein, R., Schneider, I., Chen, B., Duarte, A., Roy, B., Xiao, D., Haridasan, M., Hung, P., Care, N., Talukdar, S., Mullen, E., Smith, K., Cottman, M. & Cirne, W., 2021 — *Carbon-Aware Computing for Datacenters.*
**Venue:** arXiv:2106.11750 → IEEE Transactions on Power Systems, 2023.
**DOI (journal):** https://doi.org/10.1109/TPWRS.2022.3173250
**Finding:** Google shifts temporally-flexible compute via day-ahead Virtual Capacity Curves driven by grid-carbon-intensity forecasts — deployed globally.
**Use:** Direct analogue — carbon-signal overlay on flexible load is a mature, deployed pattern; validates the "schedule without closed-loop control" approach (Chapter 2, nb 07 discussion).

---

## Pillar C — Retrofit MACC & Carbon Pricing

### `[Hart2015-PNNL]`
Hart, P.R., Loper, S.A., Richman, E.E., Athalye, R.A., Rosenberg, M.I., Halverson, M.A. & Xie, Y., 2015 — *National Cost-Effectiveness of ANSI/ASHRAE/IES Standard 90.1-2013.*
**Venue:** PNNL Technical Report PNNL-23824 (prepared for US DOE).
**URL:** https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-23824.pdf
**Finding:** LCC analysis of 90.1-2010 → 90.1-2013 across 6 prototype buildings (~80% US commercial floor area), 5 climate locations; per-building-type incremental first-cost and LCC savings.
**Use:** **PRIMARY retrofit cost source** for MACC x-axis — Standard vs Low / Standard vs High CAPEX deltas (nb 07 §5).

### `[McKinsey2009-MACC]`
Nauclér, T. & Enkvist, P.-A., 2009 — *Pathways to a Low-Carbon Economy: Version 2 of the Global GHG Abatement Cost Curve.*
**Venue:** McKinsey & Company, v2.1.
**URL:** https://www.mckinsey.com/capabilities/sustainability/our-insights/pathways-to-a-low-carbon-economy
**Finding:** 38 GtCO₂e abatement potential by 2030 at ≤ €60/tCO₂e; building efficiency dominates the negative-cost segment.
**Use:** Canonical MACC methodology reference (Chapter 2, nb 07 §5 methodology).

### `[Kesicki2012]`
Kesicki, F. & Ekins, P., 2012 — *Marginal abatement cost curves: a call for caution.*
**Venue:** Climate Policy, 12(2), 219–236.
**DOI:** https://doi.org/10.1080/14693062.2011.582347
**Finding:** Bottom-up MACCs ignore measure interactions, exclude intertemporal dynamics, embed inconsistent baselines.
**Use:** MACC limitations subsection (Chapter 8 Discussion; nb 07 caveats).

### `[Huang2016]`
Huang, Y.-H., Kuo, T.-H. & Chou, T.-C., 2016 — *The applicability of marginal abatement cost approach: A comprehensive review.*
**Venue:** Journal of Cleaner Production, 127, 59–71.
**DOI:** https://doi.org/10.1016/j.jclepro.2016.04.013
**Finding:** Distinguishes expert-based (bottom-up engineering) vs model-based (top-down) MACCs; building-sector MACCs cluster in the negative-cost zone. `[needs verification — exact page range]`
**Use:** Locates the thesis MACC in the expert-based tradition (Chapter 2).

### `[PradaHernandez2015]`
Prada-Hernández, A.V., Vargas, S.E., Ozuna, A.F.R. & Ponz-Tienda, J.L., 2015 — *MACC for Carbon Emissions Reduction from Buildings: Implementation for Office Buildings in Colombia.*
**Venue:** Institute of Research Engineers & Doctors conference; indexed via SEEK DL / ResearchGate.
**URL:** https://www.semanticscholar.org/paper/db1aa285e6e3700a3bed1bbb80d8b4a0a19ee048
**Finding:** BIM-driven MACC finds ~20 ktCO₂ mitigation to 2040 in Colombian offices; HVAC automation + lighting stringency most cost-effective.
**Use:** Methodological analogue — office MACC across multiple climates (Chapter 2).

### `[HMT2023-GreenBook]`
HM Treasury / DESNZ, 2023 — *Valuation of Energy Use and GHG Emissions for Appraisal* (Green Book supplementary guidance).
**Venue:** UK Government guidance, November 2023 update.
**URL:** https://www.gov.uk/government/publications/valuation-of-energy-use-and-greenhouse-gas-emissions-for-appraisal
**Finding:** Since 2021 UK uses a single target-consistent carbon series (traded + non-traded merged); central ~£248/tCO₂e (2022), rising to ~£378/tCO₂e by 2050.
**Use:** UK policy-appraisal carbon value for MACC cost-effectiveness threshold (nb 07 §7 carbon-price sensitivity).

### `[UKGov2026-ETS]`
UK Government (DESNZ), 2026 — *UK ETS: Carbon price for use in civil penalties, 2026.*
**URL:** https://www.gov.uk/government/publications/determinations-of-the-uk-ets-carbon-price/uk-ets-carbon-price-for-use-in-civil-penalties-2026
**Finding:** Determined UK ETS price £49.41/tCO₂e for 2026 (vs £41.84 in 2025); ARP raised £22 → £28.
**Use:** Current-market UK ETS scenario for MACC carbon-price sensitivity (contrast with Green Book £248). Companion: Ember Carbon Price Tracker — https://ember-energy.org/data/carbon-price-tracker/.

### `[Rennert2022-SCC]`
Rennert, K., Errickson, F., Prest, B.C., Rennels, L., Newell, R.G., Pizer, W. et al. (24 authors), 2022 — *Comprehensive evidence implies a higher social cost of CO₂.*
**Venue:** Nature, 610(7933), 687–692.
**DOI:** https://doi.org/10.1038/s41586-022-05224-9
**Finding:** Central SC-CO₂ US\$185/tCO₂ (5–95% range \$44–\$413, 2020 USD) — ~3× prior US federal \$51.
**Use:** Benchmark SCC for MACC cost-effectiveness thresholds (nb 07 §7).

### `[EPA2023-SCGHG]`
US Environmental Protection Agency, 2023 — *Report on the Social Cost of Greenhouse Gases: Estimates Incorporating Recent Scientific Advances.*
**Venue:** EPA final report, December 2023.
**URL:** https://www.epa.gov/system/files/documents/2023-12/epa_scghg_2023_report_final.pdf
**Finding:** Central SC-CO₂ ~\$190/tCO₂ in 2020 at 2.0% near-term discount; CH₄ \$1,600/t; N₂O \$5,400/t.
**Use:** Primary regulatory-grade SCC for high-carbon-price sensitivity case.

### `[Ma2012-RetrofitReview]`
Ma, Z., Cooper, P., Daly, D. & Ledo, L., 2012 — *Existing building retrofits: Methodology and state-of-the-art.*
**Venue:** Energy and Buildings, 55, 889–902.
**DOI:** https://doi.org/10.1016/j.enbuild.2012.08.018
**Finding:** Typical HVAC-retrofit payback 3–10 years; deep-retrofit savings 20–50%.
**Use:** Methodological backbone for ECM screening feeding each MACC point (nb 07 §5).

### `[Chidiac2011]`
Chidiac, S.E., Catania, E.J.C., Morofsky, E. & Foo, S., 2011 — *Effectiveness of single and multiple energy retrofit measures on the energy consumption of office buildings.*
**Venue:** Energy, 36(8), 5037–5052 (companion screening paper: Energy and Buildings, 43(2–3), 614–620).
**DOIs:** https://doi.org/10.1016/j.energy.2011.05.050 · https://doi.org/10.1016/j.enbuild.2010.11.002
**Finding:** Simulated 20 ECM packages in 3 Canadian cities; combined-measure savings are sub-additive (10–25% interaction discount).
**Use:** Supports non-additivity treatment when stacking Low → Standard → High rungs (nb 07 §6).

### `[Rockefeller2012]`
DB Climate Change Advisors & The Rockefeller Foundation, 2012 — *United States Building Energy Efficiency Retrofits: Market Sizing and Financing Models.*
**Venue:** Joint report, March 2012.
**URL:** https://www.rockefellerfoundation.org/wp-content/uploads/United-States-Building-Energy-Efficiency-Retrofits.pdf
**Finding:** \$279 B investment unlocks >\$1 T lifetime energy savings, 10% US emissions cut, 3.3 M job-years.
**Use:** Market-scale CAPEX benchmark for national retrofit opportunity (Chapter 1).

### `[Wilson2022-ComStock]`
Wilson, E.J.H., Parker, A., Fontanini, A., Present, E., Reyna, J.L. et al., 2022 — *End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification.*
**Venue:** NREL Technical Report NREL/TP-5500-80889.
**DOI:** https://doi.org/10.2172/1854582
**Finding:** ComStock calibrated against AMI and CBECS at 15-min resolution across 14 commercial types, 7 climate zones; whole-building NMBE within ±10%.
**Use:** Bottom-up stock modelling benchmark — comparator to AlphaBuilding-derived MACC (Chapter 3, nb 07 sanity check).

### `[ASHRAE2019-ServiceLife]`
ASHRAE, 2019 — *ASHRAE Handbook — HVAC Applications*, Ch. 37 Owning & Operating Costs (+ Service Life Database).
**Venue:** ASHRAE, Atlanta GA.
**URL:** https://weblegacy.ashrae.org/publicdatabase/service_life.asp
**Finding:** Reciprocating chillers 20 yr, centrifugal 23 yr, packaged DX 15 yr, AHUs 20 yr, boilers 25–30 yr, envelope insulation 30+ yr.
**Use:** Asset-life assumption (conservatively 25 yr) for annualising CAPEX on MACC y-axis (nb 07 §5).

### `[IEA2021-NetZero]`
International Energy Agency, 2021 — *Net Zero by 2050: A Roadmap for the Global Energy Sector.*
**Venue:** IEA, Paris, May 2021 (revised Oct 2021).
**URL:** https://www.iea.org/reports/net-zero-by-2050
**Finding:** Renovation rate must rise from ~1%/yr to ≥ 2%/yr by 2030; 20% of stock zero-carbon-ready by 2030 and 85% by 2050; direct building emissions 3 Gt (2020) → 0.12 Gt (2050).
**Use:** Global retrofit-pace benchmark setting policy urgency (Chapter 1, Chapter 9).

### `[UKGBC2021-Roadmap]`
UK Green Building Council, 2021 — *Net Zero Whole Life Carbon Roadmap for the Built Environment.*
**Venue:** UKGBC, November 2021.
**URL:** https://ukgbc.org/resources/net-zero-whole-life-carbon-roadmap-for-the-built-environment/
**Finding:** UK non-domestic operational carbon requires 50–70% cut by 2035 vs 2018; commercial-office retrofit ~2%/yr; fabric-first delivers 30–40% heat-demand reduction.
**Use:** UK-specific decarbonisation pathway anchoring MACC interpretation (Chapter 8, Chapter 9).

---

## Reference-to-notebook mapping

| Notebook / Chapter | Primary short-keys |
|---|---|
| Ch.1 Introduction | `[IPCC_AR6_Ch9]`, `[IEA2018_FoC]`, `[IEA2024_Urban]`, `[IEA2021-NetZero]`, `[UKGBC2021-Roadmap]`, `[Satchwell2021]`, `[Pean2019]`, `[Rockefeller2012]` |
| Ch.2 Literature review | All Pillar A, B, C references organised by pillar |
| Ch.3 Dataset + EDA (existing nb 02) | — (self-contained) |
| Ch.4 ML model (existing nb 04) | — |
| Nb 05 climate trends | `[Isaac2009]`, `[VanRuijven2019]`, `[Dirks2015]`, `[EPA2021_CDD]`, `[Petri2015]`, `[Sailor2003]`, `[DayGD2017]`, `[Biardeau2020]`, `[Santamouris2014]` |
| Nb 06 grid carbon | `[eGRID2022]`, `[Cambium2023]`, `[LRMER2023]`, `[SilerEvans2012]`, `[Ryan2016]`, `[Hawkes2010]` |
| Nb 07 carbon optimisation | `[Braun1990]`, `[Kircher2015]`, `[Reynders2017]`, `[Pean2019]`, `[Arteconi2012]`, `[Neukomm2019]`, `[Satchwell2021]`, `[Radovanovic2021]`, `[Hart2015-PNNL]`, `[McKinsey2009-MACC]`, `[Kesicki2012]`, `[Huang2016]`, `[PradaHernandez2015]`, `[HMT2023-GreenBook]`, `[UKGov2026-ETS]`, `[Rennert2022-SCC]`, `[EPA2023-SCGHG]`, `[Ma2012-RetrofitReview]`, `[Chidiac2011]`, `[Rockefeller2012]`, `[Wilson2022-ComStock]`, `[ASHRAE2019-ServiceLife]` |
| Ch.8 Discussion | `[Pean2019]` (gap), `[Kesicki2012]` (MACC limits), `[Ryan2016]` (method sensitivity), `[UKGBC2021-Roadmap]` |
| Archived nb 05 preamble | `[Pean2019]` |

---

## Sources flagged for primary-source verification

Before quoting verbatim in the thesis, confirm the following against the primary PDF:

- **`[IPCC_AR6_Ch9]`** — the "cooling +75% 1990–2019" figure; confirm against published Section 9.3.
- **`[Petri2015]`** — the "+20% CDD / −10% HDD per K" phrasing; confirm exact wording from abstract/results.
- **`[Braun1990]`** — the 40% / 51% figures; primary ASHRAE Transactions PDF is paywalled; currently cited via secondary sources.
- **`[Neukomm2019]`** — specific flexibility-MW quantitatives live in companion sub-reports; cite sub-reports directly for numbers.
- **`[Huang2016]`** — exact page range of the MACC review.

---

## Style conventions

- Citations in notebook markdown use `[short-key]` inline; prose paraphrases must attribute the source explicitly (e.g. "Péan et al (2019) `[Pean2019]` identify carbon-signal objectives as under-served…").
- Never quote a specific number without linking it to a short-key here.
- Prefer DOI over URL when both exist.
- Where a primary source is paywalled and only secondary access is available, flag with `[paywalled primary]`.
- When a reference is added during a coding session, add its short-key to the relevant row in the **Reference-to-notebook mapping** table above in the same commit.

---

*Last updated: 2026-04-18 (initial library compiled during pivot from MPC framework to climate-and-carbon emissions analysis).*
