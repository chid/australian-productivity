# Data and framework {#sec:data}

## Sources

We use four sources. All of the datasets we compiled are published with full schemas in the accompanying repository.

1. **Productivity Commission chart data** (September 2026 update; June 2026 quarterly bulletin). These give quarterly, seasonally adjusted labour productivity indices for the whole economy, the market sector and the non-market sector from June 2004 to June 2026. They also give cumulative MFP growth by industry over 2001–02 to 2023–24 [@PC2026update; @PC2026qbjun].
2. **OECD Productivity Database** (SDMX dataflow `DSD_PDB@DF_PDB` v2.0). This gives GDP per hour worked in constant 2020 PPP US dollars, GDP per capita, hours worked per head of population, and growth-accounting contributions of MFP and capital deepening to labour productivity growth, for the whole economy in calendar years 2000–2025 [@OECDpdb].
3. **ABS Estimates of Industry Multifactor Productivity** (February 2026 release). These are market-sector MFP, labour productivity and capital services on a financial-year basis [@ABS2026mfp].
4. **ILOSTAT modelled estimates** of output per hour worked (constant 2021 PPP dollars), used only for Southeast Asia, which the OECD does not cover [@ILOSTAT]. Years after 2025 are projections and are excluded from all calculations.

## Growth-accounting framework

Under constant returns and competitive factor markets, log labour productivity growth decomposes as

$$
\Delta \ln\!\left(\frac{Y}{H}\right) = \underbrace{\bar{s}_K\,\Delta \ln\!\left(\frac{K}{H}\right)}_{\text{capital deepening}} + \underbrace{\Delta \ln A}_{\text{MFP}},
$$

where $Y$ is output, $H$ hours worked, $K$ capital services, $\bar{s}_K$ the average capital income share, and $A$ the residual, multifactor productivity. The OECD series measures labour input in raw hours, so its MFP term includes any improvement in labour quality. The US Bureau of Labor Statistics (BLS) and the ABS's quality-adjusted series separate out a labour-composition term [@BLS2026tfp; @ABS2026mfp]. This distinction matters when US and Australian figures are compared (section [4](#sec:ga)).

## Reconciling the sources

Table 1 sets out the main Australian measures. They range from about −0.3% to about 1.0% a year, depending on coverage, timing and the labour-input concept.

: Table 1. Measures of Australian labour productivity growth since 2019

| Measure | Coverage and timing | Window | Growth (%/yr) | Source |
|---|---|---|---|---|
| GDP per hour | Whole economy, calendar year | 2019–2025 | **0.10** | OECD PDB (authors' calculation) |
| GDP per hour index | Whole economy, quarterly | Jun 2019–Jun 2025 | ≈0.15 | PC (2026) chart data |
| GVA per hour index | Market sector, quarterly | Jun 2019–Jun 2025 | ≈0.47 | PC (2026) chart data |
| GVA per hour index | Non-market sector, quarterly | Jun 2019–Jun 2025 | ≈−0.34 | PC (2026) chart data |
| Labour productivity | ABS market sector, financial year | 2019–20 to 2024–25 | ≈0.45 (≈0.22 excl. 2019–20) | ABS (2026) |
| Quality-adjusted labour productivity | Market sector | 2018–19 to 2023–24 | ≈0.3 | Bruno, Hambur and Wang (2025) |
| Labour productivity | Market sector excluding mining | 2017–18 to 2023–24 | ≈1.0 | Plumb (2025) |
| GDP per hour (modelled) | Whole economy, ILO | 2019–2025 | 0.84 | ILOSTAT (authors' calculation) |

The differences have six sources [@ABSunderstanding; @PC2026bulletin]:

- **Coverage.** The ABS publishes MFP for the market sector only. The OECD covers the whole economy, including health, education and public administration, where output is largely measured by inputs.
- **Output concept.** The OECD uses GDP; the ABS uses gross value added.
- **Timing.** Financial-year windows that begin in 2019–20 capture the COVID-era composition spike in productivity. A calendar-2019 base largely does not.
- **Start-year sensitivity.** In the PC's quarterly series, whole-economy growth is about 0.15% a year from June 2019 but about 0.02% from December 2019.
- **Labour-input basis.** Market-sector MFP in 2024–25 was −0.8% on a quality-adjusted labour basis and −0.5% on an hours basis.
- **Arithmetic and vintage.** The PC uses percentage changes and the ABS log changes; for example, mining MFP is −3.2% in PC figures and −3.3% in ABS figures. The 2025 annual national accounts also revised hours worked.

The ILO's modelled series puts Australian growth well above the OECD figure. But its Australia–US gap, about 1.5 percentage points a year, is close to the OECD's 1.8. We therefore treat the size of the gap as robust and Australia's own growth rate as uncertain within a band of roughly 0–0.5% a year.

Level comparisons depend on the PPP vintage. The ICP 2021 revisions moved Australia, Canada and the UK "further from top OECD performers" [@OECD2024icp], and earlier Treasury work put Australia at 75–85% of US GDP per hour over four decades [@TreasuryComparing]. The fall from 95% to 81% should therefore be read as a fall *within the current vintage*.
