"""Generate the paper's figures from the tidy datasets in site/data/.

Run from the project root:
    uv run --with matplotlib python -I paper/figures/make_figures.py
"""
import csv, os
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "site", "data")
OUT = os.path.join(ROOT, "paper", "figures")

# Validated categorical palette (light mode), fixed order.
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e1e0d9"
plt.rcParams.update({
    "font.family": "sans-serif", "font.size": 9, "axes.edgecolor": "#c3c2b7", "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 200, "savefig.bbox": "tight",
    "lines.linewidth": 1.8, "legend.frameon": False,
})


def rows(name):
    with open(os.path.join(DATA, name)) as f:
        return list(csv.DictReader(f))


def save(fig, name):
    fig.savefig(os.path.join(OUT, name))
    plt.close(fig)
    print("wrote", name)


# Figure 1: Australian labour productivity index by sector
s = defaultdict(list)
for r in rows("au_labour_productivity_quarterly.csv"):
    s[r["sector"]].append((r["quarter_end"], float(r["index_jun2014_eq_100"])))
fig, ax = plt.subplots(figsize=(6.5, 3.2))
for (k, lab), col in zip([("market_sector", "Market sector"), ("whole_economy", "Whole economy"),
                          ("non_market_sector", "Non-market sector")], C):
    xs = [int(d[:4]) + (int(d[5:7]) - 1) / 12 for d, _ in s[k]]
    ax.plot(xs, [v for _, v in s[k]], color=col, label=lab)
    ax.annotate(f"{lab} {s[k][-1][1]:.1f}", (xs[-1], s[k][-1][1]), xytext=(4, 0), textcoords="offset points",
                va="center", fontsize=8, color=INK)
ax.set_ylabel("Index, June 2014 = 100")
ax.legend(loc="upper left", ncol=3, fontsize=8)
save(fig, "fig1_au_lp_index.png")

# Figure 2: GDP per hour as % of US
gap = defaultdict(dict)
for r in rows("oecd_gdp_per_hour.csv"):
    if r["pct_of_us"]:
        gap[r["country_code"]][int(r["year"])] = float(r["pct_of_us"])
fig, ax = plt.subplots(figsize=(6.5, 3.4))
for (code, lab), col in zip([("AUS", "Australia"), ("CAN", "Canada"), ("EU27_2020", "EU-27"), ("DEU", "Germany"),
                             ("GBR", "UK"), ("JPN", "Japan")], C):
    yrs = sorted(gap[code])
    ax.plot(yrs, [gap[code][y] for y in yrs], color=col, lw=2.4 if code == "AUS" else 1.6, label=lab)
    ax.annotate(f"{lab} {gap[code][yrs[-1]]:.0f}%", (yrs[-1], gap[code][yrs[-1]]), xytext=(4, 0),
                textcoords="offset points", va="center", fontsize=8, color=INK)
ax.axhline(100, color=MUTED, ls="--", lw=1)
ax.set_ylabel("GDP per hour worked, % of US (2020 PPP)")
ax.legend(loc="lower left", ncol=3, fontsize=8)
save(fig, "fig2_gap_vs_us.png")

# Figure 3: growth before/after 2019
g = defaultdict(dict)
for r in rows("growth_summary.csv"):
    if r["source"] == "OECD" and r["avg_annual_growth_pct"]:
        g[r["country"]][r["period"]] = float(r["avg_annual_growth_pct"])
order = sorted(g, key=lambda c: g[c]["2019-2025"])
fig, ax = plt.subplots(figsize=(6.5, 4))
y = range(len(order))
ax.barh([i + 0.2 for i in y], [g[c]["2014-2019"] for c in order], 0.38, color=C[0], label="2014–19")
ax.barh([i - 0.2 for i in y], [g[c]["2019-2025"] for c in order], 0.38, color=C[1], label="2019–25")
ax.set_yticks(list(y), order)
for t in ax.get_yticklabels():
    if t.get_text() == "Australia":
        t.set_fontweight("bold")
ax.axvline(0, color="#c3c2b7", lw=1)
ax.set_xlabel("Average annual growth in GDP per hour worked, %")
ax.legend(loc="lower right")
ax.grid(axis="y", visible=False)
save(fig, "fig3_growth_periods.png")

# Figure 4: growth accounting 2020-24
ex = rows("oecd_extra_metrics.csv")
ex.sort(key=lambda r: float(r["mfp_contrib_2020_2024"]) + float(r["capdeep_contrib_2020_2024"]))
fig, ax = plt.subplots(figsize=(6.5, 3.6))
y = range(len(ex))
ax.barh([i + 0.2 for i in y], [float(r["mfp_contrib_2020_2024"]) for r in ex], 0.38, color=C[0], label="MFP")
ax.barh([i - 0.2 for i in y], [float(r["capdeep_contrib_2020_2024"]) for r in ex], 0.38, color=C[1], label="Capital deepening")
ax.set_yticks(list(y), [r["country"] for r in ex])
ax.axvline(0, color="#c3c2b7", lw=1)
ax.set_xlabel("Contribution to labour productivity growth, pp per year, average 2020–24")
ax.legend(loc="lower right")
ax.grid(axis="y", visible=False)
save(fig, "fig4_growth_accounting.png")

# Figure 5: hours per person change vs GDP per person growth
fig, ax = plt.subplots(figsize=(5.2, 3.6))
for r in ex:
    x, yv = float(r["hrs_pop_change_2019_2025"]), float(r["gdp_pc_growth_2019_2025"])
    aus = r["code"] == "AUS"
    ax.scatter(x, yv, s=46 if aus else 30, color=C[1] if aus else C[0], zorder=3, edgecolor="white", linewidth=1)
    off = {"GBR": (5, -11), "CAN": (-8, 5)}.get(r["code"], (5, 3))
    ax.annotate(r["country"], (x, yv), xytext=off, textcoords="offset points", fontsize=8,
                ha="right" if r["code"] == "CAN" else "left",
                color=INK, fontweight="bold" if aus else "normal")
ax.set_xlabel("Change in hours worked per person, 2019–25, %")
ax.set_ylabel("GDP per person growth, % per year")
save(fig, "fig5_hours_vs_gdppc.png")

# Figure 6: industry MFP
ind = rows("au_industry_mfp_growth_2002_2024.csv")
ind.sort(key=lambda r: float(r["cumulative_mfp_growth_pct"]))
fig, ax = plt.subplots(figsize=(6.5, 3.8))
vals = [float(r["cumulative_mfp_growth_pct"]) for r in ind]
ax.barh(range(len(ind)), vals, color=[C[0] if v >= 0 else "#e34948" for v in vals])
ax.set_yticks(range(len(ind)), [r["industry"] for r in ind])
ax.axvline(0, color="#c3c2b7", lw=1)
ax.set_xlabel("Cumulative MFP growth, 2001–02 to 2023–24, %")
ax.grid(axis="y", visible=False)
save(fig, "fig6_industry_mfp.png")

# Figure 7: ASEAN levels vs Australia (ILO)
ilo = [r for r in rows("ilo_gdp_per_hour.csv") if r["year"] == "2025" and r["region"] in ("Southeast Asia", "Australia & NZ")
       and r["country_code"] != "NZL"]
ilo.sort(key=lambda r: float(r["pct_of_australia"]))
fig, ax = plt.subplots(figsize=(6.5, 3.4))
ax.barh(range(len(ilo)), [float(r["pct_of_australia"]) for r in ilo],
        color=[C[1] if r["country_code"] == "AUS" else C[0] for r in ilo])
ax.set_yticks(range(len(ilo)), [r["country"] for r in ilo])
ax.set_xlabel("GDP per hour worked, 2025, % of Australia (ILO modelled, 2021 PPP)")
ax.grid(axis="y", visible=False)
save(fig, "fig7_asean_levels.png")
