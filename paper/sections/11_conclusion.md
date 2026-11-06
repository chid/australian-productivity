# Conclusion {#sec:conclusion}

Australia's post-2019 stagnation is the point at which several slow-moving problems stopped being hidden. In turn, the mining boom, the terms of trade, and then rapid growth in population and hours kept income per person rising while output per hour lost momentum. Once the growth in hours is netted out, very little is left. The comparison with Canada and Europe matters as much as the comparison with the United States, because it shows that the forces behind the US acceleration were absent almost everywhere else. What is distinctively Australian is the combination of additional drags: a care economy, measured by its inputs, that has expanded by policy design; resource and electricity sectors in capital-heavy phases; and two decades of weaker firm entry and slower diffusion.

The question to ask is therefore not why Australian productivity collapsed, since measured MFP has been weak since the mid-2000s. It is why Australia's growth model drifted from capital deepening and diffusion toward expanding labour input, and whether its statistics can distinguish real stagnation from statistical convention. The defensible headline is a range: roughly zero for the whole economy on OECD data, about 0.2–0.5% a year for the market sector, and about 1.0% for the market sector excluding mining. Every version is well below US growth and below Australia's own history.

# References {-}

::: {#refs}
:::

# Appendix A. Data and replication {-}

All data, code and figures are available at <https://github.com/chid/australian-productivity>. The script `build/fetch_sources.sh` downloads the raw source files, `build/build_data.py` produces the tidy CSVs in `site/data/`, and `paper/figures/make_figures.py` regenerates every figure. OECD series are whole-economy, calendar-year data; growth rates are compound annual rates between endpoint years; growth-accounting contributions are simple averages of annual percentage-point contributions. ILO data are used only for comparisons within the ILO series. PC quarterly data are seasonally adjusted, and their quarters are labelled by the month in which each quarter ends.
