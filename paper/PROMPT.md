# Single-shot prompt: Australian productivity paper

Paste everything below the line into a capable model with web access, a shell and file tools. It reproduces this project end to end: data, website, research and paper. It is self-contained and assumes no earlier conversation.

---

You are a research economist and data engineer. In a single run, produce a replicable working paper titled **"Working More, Producing Little: Australia's Post-2019 Productivity Stagnation in International Perspective"**, together with an open dataset and a static explainer website. Today's date is {{DATE}}. Work in the directory {{WORKDIR}}.

## 1. Data (use primary sources only; save raw downloads to `data/`, never edit them)

1. **Productivity Commission (PC)**: download the chart-data XLSX files for the latest *Productivity update* and *Quarterly productivity bulletin* from pc.gov.au/ongoing/productivity-insights. Extract the quarterly labour productivity index (whole economy, market sector and non-market sector; June 2014 = 100), the dashboard quarterly and annual changes in output, hours and labour productivity, and cumulative industry MFP growth (2001–02 to 2023–24). The workbook labels are sometimes stale: derive periods from each value's position in the series, and record any label problems you find.
2. **OECD Productivity Database** via SDMX: `https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB,2.0/{AREAS}.A.......?startPeriod=2000&format=csvfilewithlabels` for AUS, USA, CAN, EU27_2020, DEU, FRA, GBR, ITA, ESP, NLD, NZL, JPN, KOR and OECD. Use whole-economy series (`ACTIVITY=_T`):
   - GDPHRS in USD_PPP_H at constant prices (`PRICE_BASE=LR`), untransformed (`TRANSFORMATION=N`)
   - GDPPOP in USD_PPP_PS, LR
   - HRSPOP
   - MFP_PCCONLP and KSERHRS_PCCONLP with `ASSET_CODE=_T` and `TRANSFORMATION=GY`

   The file is about 175 MB, so gitignore it and provide a fetch script.
3. **ILOSTAT** via SDMX: `https://sdmx.ilo.org/rest/data/ILO,DF_GDP_2HRW_NOC_NB,1.0/{AREAS}..?startPeriod=2005` with the header `Accept: application/vnd.sdmx.data+csv;version=1.0.0`. Cover all ten ASEAN members plus AUS, USA, CAN, DEU, FRA, GBR, KOR, JPN, CHN, IND and NZL. Flag years after the latest actual year as projections and exclude them from every calculation.
4. **ABS** Estimates of Industry Multifactor Productivity (cat. 5260.0.55.002, latest release): market-sector MFP, labour productivity and capital services on both the hours and the quality-adjusted labour-input bases.

## 2. Build (`build/build_data.py`, run with `uv run --with openpyxl python -I`)

Write tidy CSVs to `site/data/`:
- `au_labour_productivity_quarterly.csv`
- `au_headline_change.csv`
- `au_industry_mfp_growth_2002_2024.csv`
- `oecd_gdp_per_hour.csv`, including % of the US
- `ilo_gdp_per_hour.csv`, including % of Australia and a status column
- `growth_summary.csv`: compound annual growth for 2005–14, 2014–19 and 2019–25
- `oecd_extra_metrics.csv`: GDP per capita and its % of the US; hours per head in 2019 and 2025; MFP and capital-deepening contributions averaged over 2015–19, 2020–24 **and 2022–24**

Also write a compact `productivity.json` and a Frictionless `datapackage.json` with a schema and licence (CC BY 4.0) for each file.

**Sanity checks:** flag any growth-accounting year where an absolute contribution exceeds 5 points; Canada 2021 is a known example. Verify that Australian GDP per capita growth ≈ hours-per-head growth + GDP-per-hour growth.

## 3. Website (`site/index.html`, GitHub Pages ready, no build step)

- **Charting:** vanilla JS and inline SVG reading `data/productivity.json`. Use a validated, colour-blind-safe categorical palette in fixed order, and separate light and dark modes with a theme toggle. Every chart needs a hover tooltip and a "show as table" view. The layout must work at 375px with no horizontal scroll. Use one axis per chart and never a dual axis.
- **Headline stat tiles:** labour productivity over the latest year; growth 2019–25 against the US and the OECD; GDP per hour as a % of the US; the non-market sector index.
- **Sections:**
  1. Australia's quarterly index with the 2015–19 average, plus industry MFP as diverging bars.
  2. GDP per hour as a % of the US over time for six economies, plus growth before and after 2019 as grouped bars.
  3. Southeast Asia levels as a % of Australia (ILO), with a toggle that adds China, India, Japan and Korea.
  4. Sources of growth (MFP against capital deepening) and the change in hours per head.
  5. Regional drivers, sourced.
  6. Policy lessons.
  7. Caveats, a data download table, and sources and licences.
- Add `.nojekyll` and a README.

## 4. Research

Research each of these five areas separately, prioritising official and peer-reviewed sources from 2023 onwards. Give every claim a source URL and a reliability label: official / peer-reviewed / think-tank / advocacy / unverified.

1. Growth accounting and measurement: ABS and PC bulletins, RBA labour-quality work, BLS TFP, StatCan, ONS, mismeasurement literature, non-market output, PPP vintages.
2. Hours, migration and composition: ABS Labour Account, PC COVID paper, Bank of Canada, ECB/ESM labour hoarding, Banque de France apprenticeships, e61 microdata.
3. Sectors: mining (Topp et al. 2008; ABS natural-resource-adjusted MFP), electricity (the PC's quality- and emissions-adjusted measures), housing construction, the German energy shock, Norway's mainland convention, Brunei, Thailand and Indonesian nickel.
4. Investment, competition and diffusion: non-mining investment, intangibles, BLADE concentration and markups, frontier–laggard divergence, firm entry and job mobility, US business formation, AI adoption and the J-curve, Canadian investment per worker, tax treatment of investment.
5. Policy and open questions: the PC five-pillar reports of December 2025 (47 recommendations, distinct from the 71 in the 2023 *Advancing Prosperity*), the 2024 revival of National Competition Policy, Canadian and EU (Draghi) implementation, Singapore, and the Southeast Asia strategy to 2040.

Save notes per area, then synthesise a report. Convert its bibliography to `paper/references.bib` with a script, keeping the reliability label in `note`.

## 5. Paper (`paper/`, pandoc Markdown → HTML/DOCX/PDF)

- **Files:** `metadata.yaml` (title, author {{AUTHOR}}, abstract of 200 words or fewer, JEL O47, O57, E01, D24, J24, L16); `sections/01_introduction.md` … `11_conclusion.md`; `figures/make_figures.py` (matplotlib, same palette as the site); a `Makefile` with figures, html, docx, tex and pdf targets; `apa.csl`.
- **Section structure:**
  - Introduction (three contributions)
  - Data and framework (the growth-accounting equation, and a reconciliation table of every Australian measure with its six sources of difference: coverage, GDP versus GVA, timing, start year, labour-input basis, arithmetic and vintage)
  - Stylised facts (five)
  - Growth accounting (a three-window table with Canada flagged)
  - Hours, migration and the care economy
  - Mining, electricity and construction
  - Investment, competition, dynamism and diffusion
  - International comparisons (a table)
  - Policy implications (eight)
  - Research agenda (seven questions)
  - Conclusion, references, and a data appendix
- **Rules:**
  - Cite with `[@key]` only; every key must exist in the .bib, and the build must produce no citation warnings.
  - Present headline growth as a range across measures.
  - Never mix ILO and OECD levels.
  - Label all derived numbers "authors' calculation".
  - Mark advocacy sources inline.
  - Do not invent figures. Where a fact cannot be verified, say so.

## 6. Review and deliver

Write `paper/REVIEW.md` covering:
- what holds up
- problems to fix, with concrete actions
- further ideas for the data, the paper and the narrative

Render the HTML and inspect it visually. Check for label collisions, for figures that fail to load, and that dark mode is readable. Then initialise git, create a public GitHub repo (`gh repo create`), push `main`, and publish `site/` to `gh-pages` with `git subtree push --prefix site origin gh-pages`. Confirm that the Pages URL returns 200.

**Report back with:**
- the live URL and the repo URL
- a five-sentence summary of the findings
- a list of every unverified claim still in the paper
