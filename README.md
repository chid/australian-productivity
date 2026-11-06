# Australian productivity, compared

The source data, build scripts and static site for an explainer that compares Australia's labour productivity (Productivity Commission data) with the US, Canada, Europe and Southeast Asia (OECD and ILO data).

- `site/`: the published site (index.html + `data/` CSVs), deployed to the `gh-pages` branch. See `site/README.md`.
- `build/fetch_sources.sh`: re-downloads the raw sources into `data/`.
- `build/build_data.py`: builds `site/data/` from the raw sources: `uv run --with openpyxl python -I build/build_data.py`
- `data/`: the raw downloads. The OECD file (`data/intl/pdb.csv`, ~175 MB) is gitignored; fetch it with the script.

To redeploy after a rebuild: `git subtree push --prefix site origin gh-pages`
