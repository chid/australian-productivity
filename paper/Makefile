# Build the paper. Run from paper/.
#   make figures   regenerate figures from ../site/data
#   make html      standalone HTML (needs pandoc)
#   make docx      Word document (needs pandoc)
#   make tex       LaTeX source (needs pandoc)
#   make pdf       PDF (needs pandoc + a LaTeX engine, e.g. tectonic or xelatex)

SECTIONS := $(sort $(wildcard sections/*.md))
PANDOC   := pandoc metadata.yaml $(SECTIONS) --citeproc --bibliography=references.bib \
            --csl=apa.csl --resource-path=.:figures --number-sections

all: figures html docx

figures:
	cd .. && uv run --quiet --with matplotlib python -I paper/figures/make_figures.py

html:
	$(PANDOC) --standalone --embed-resources --toc -c paper.css -o build/paper.html

docx:
	$(PANDOC) -o build/paper.docx

tex:
	$(PANDOC) --standalone -o build/paper.tex

pdf:
	$(PANDOC) --pdf-engine=$${PDF_ENGINE:-tectonic} -V geometry:margin=1in -o build/paper.pdf

.PHONY: all figures html docx tex pdf
