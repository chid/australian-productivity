# Review of the project so far, and further ideas

*Written 7 November 2026, after the site, international comparison, subagent findings and deep research were complete.*

## What holds up

- **The Australia–US gap is robust.** It is about 1.5–1.8 percentage points a year on both OECD and ILO data, and it matches the BLS and PC level comparisons (the US is about 23% higher in the non-agricultural market sector).
- **The finding that "living standards rose through hours, not productivity" is the strongest result.** GDP per capita grew 0.97% a year; hours per head grew about 0.87% a year; GDP per hour grew 0.10% a year. It is simple, robust and not yet prominent in Australian debate.
- **The comparison with other countries reframes the problem.** The US is the outlier, and Canada, the UK and Europe resemble Australia. That changes the policy question from "what did Australia do wrong" to "what did the US do that nobody else did, and what extra drags does Australia carry".

## Problems to fix

1. **Canada's growth accounting on the site is misleading.** Over 2020–24 the OECD file averages a Canadian MFP contribution of −1.74 points and capital deepening of +2.12, driven by a 2021 observation of −13.0 and +8.9. The paper uses 2022–24 instead (MFP +0.04, capital −0.58), which agrees with Statistics Canada. **Action:** switch the site's growth-accounting chart to 2022–24, or show both windows, with a footnote.
2. **Australia's own growth figure is sensitive to the start year.** On PC quarterly data, whole-economy growth is about 0.15% a year from June 2019 and about 0.02% from December 2019. **Action:** add a start-year sensitivity panel (a fan of start quarters) to the site and the paper.
3. **The level comparison depends on the PPP vintage.** The fall from 95% to 81% holds in the current OECD vintage only, and a DBnomics mirror shows a break in the Australian current-PPP levels series. **Action:** recompute the levels using the 2017 and 2021 ICP PPPs and report both.
4. **Weak sources are still cited in places.** Fraser and C.D. Howe on Canadian investment are labelled as leaning towards advocacy, but the 54%-of-US figure should be cross-checked against StatCan's flows and stocks of fixed non-residential capital. Several entries in `references.bib` carry "Reliability: unverified": media reports, summaries by law firms and figures relayed second-hand. **Action:** replace each with a primary source before submission.
5. **Figures the paper relies on that have not been checked against primary documents:** e61's estimate that reduced mobility explains a quarter of the slowdown (seen only via media); the journal that published Brynjolfsson, Li and Raymond; the authors of the ELRR article; the 13-of-17 reform areas; and the split of the 47 PC recommendations by report.

## Further ideas

### For the data and the site
- **Market sector excluding mining as a headline series.** This is the RBA's preferred view, at about 1.0% a year over 2017–18 to 2023–24. Build it from the ABS 5260.0.55.002 industry tables.
- **Hours per head as a first-class series.** Show the decomposition of GDP per capita into output per hour plus hours per head for every country, as a small-multiples chart.
- **State-level productivity.** Use ABS state accounts to test whether the stagnation is concentrated in Western Australia and Queensland (mining) or is national.
- **Real wages and productivity.** Add a chart of real consumer wages against labour productivity to test whether the long-run link holds after 2019.
- **An automatic quarterly refresh.** A GitHub Action that runs `build/fetch_sources.sh` and `build_data.py` after each PC quarterly update, then opens a pull request.

### For the paper
- **A formal bridge between OECD and ABS measures** (research question 1). Table 1 is the start. A shift-share bridge that steps from ABS market-sector MFP to OECD whole-economy MFP one adjustment at a time would be a standalone contribution.
- **A difference-in-differences on the care economy.** Compare NDIS rollout timing across regions with local measured productivity, to separate the measurement effect from the real effect.
- **Mining MFP adjusted for natural resources.** Extend the ABS experimental series to 2024–25 using Geoscience Australia data on reserves and ore grades.
- **Effective tax rates on investment.** Compute a 2026 Australian marginal effective tax rate using the Devereux–Griffith method and compare it with Canada's (6.4% after the Mega Deduction), the US and the UK.
- **The cost of reallocation forgone through JobKeeper.** Use BLADE to compare firm exits and job-to-job flows in 2020–22 with a counterfactual based on the US or New Zealand.
- **A recommendation tracker** (research question 7). This is the most novel idea and is feasible as a stand-alone dataset.

### For the narrative
- Lead with "Australia swapped productivity growth for hours". It is memorable and correct.
- Present every headline figure as a range across measures (about 0, 0.2–0.5% and 1.0% a year) rather than a single number.
- Keep the Southeast Asia section short and framed around engagement in the region, because the ILO data are modelled and the city-state comparison with Singapore is weak.
