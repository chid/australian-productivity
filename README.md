# Australian productivity, compared

A static site and open dataset. It compares Australia's labour productivity, using Productivity Commission data, with the United States, Canada, Europe and Southeast Asia, using OECD and ILO data.

- `index.html`: the explainer page with interactive charts. It reads `data/productivity.json`.
- `data/*.csv`: tidy datasets, described in `data/datapackage.json` (Frictionless Data format).

## Hosting on GitHub Pages

Copy the contents of this folder to the root of the branch that Pages serves (or to `/docs`), commit and push, then turn on Pages under **Settings → Pages**. The `.nojekyll` file stops Jekyll from processing the files.

To preview locally, run `python3 -m http.server` in this folder and open http://localhost:8000. Opening `index.html` straight from disk won't work, because browsers block `fetch` on `file://` URLs.

## Rebuilding

The raw sources and build scripts are on the `main` branch of this repository (`data/`, `build/`). To rebuild:

```sh
uv run --with openpyxl python -I build/build_data.py   # run from the project root
```

## Sources and licences

- Productivity Commission: Productivity update (September 2026) and Quarterly productivity bulletin (June 2026) chart data. © Commonwealth of Australia, CC BY 4.0.
- OECD Productivity Database (`OECD.SDD.TPS,DSD_PDB@DF_PDB,2.0`), CC BY 4.0.
- ILOSTAT modelled estimates (`ILO,DF_GDP_2HRW_NOC_NB,1.0`), CC BY 4.0.

This is an independent compilation, not endorsed by the PC, OECD or ILO. See the Caveats section of the page before citing the figures.
