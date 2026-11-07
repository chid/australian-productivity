# Australian productivity, compared

The source data, build scripts and static site for an explainer that compares Australia's labour productivity (Productivity Commission data) with the US, Canada, Europe and Southeast Asia (OECD and ILO data).

- `site/`: the published site (index.html + `data/` CSVs), deployed to the `gh-pages` branch. See `site/README.md`.
- `build/fetch_sources.sh`: re-downloads the raw sources into `data/`.
- `build/build_data.py`: builds `site/data/` from the raw sources: `uv run --with openpyxl python -I build/build_data.py`
- `data/`: the raw downloads. The OECD file (`data/intl/pdb.csv`, ~175 MB) is gitignored; fetch it with the script.

To redeploy after a rebuild: `git subtree push --prefix site origin gh-pages`

## Paper

`paper/` holds a working paper built from this data and the deep-research report in `reports/`. Notes for each research area are in `research_notes/`. Build it with `cd paper && make html docx` (requires pandoc). See `paper/REVIEW.md` for a review of the project and further ideas, and `paper/PROMPT.md` for a single-shot prompt that reproduces the whole project.

## Ask the data

`site/ask.html` (live at https://chid.github.io/australian-productivity/ask.html) lets anyone query the datasets in the browser: preset questions and a SQL console run on DuckDB-WASM with no key, and a plain-English mode sends questions to Claude (`claude-opus-5-5`) with the visitor's own API key. Claude answers by calling a `run_sql` tool that executes locally, and every answer shows the SQL it ran.

The paper is published at https://chid.github.io/australian-productivity/paper/ (`make html` in `paper/` copies it into `site/paper/`).
