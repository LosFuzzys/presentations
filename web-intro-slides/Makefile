BASEFILE=presentation
TEXFILE=$(BASEFILE).tex

TEXCMD=pdflatex
BIBCMD=biber

all:
	$(TEXCMD) $(TEXFILE)

full: clean
	$(TEXCMD) $(TEXFILE)
	$(TEXCMD) $(TEXFILE)

clean:
	@$(RM) *.blg
	@$(RM) *.log
	@$(RM) *.out
	@$(RM) *.aux
	@$(RM) *.run.xml
	@$(RM) *.toc
	@$(RM) *.nav
	@$(RM) *.snm
	@$(RM) *.vrb

cleanbib:
	@$(RM) *.bbl
	@$(RM) *.bst
	@$(RM) *.bcf

cleanpdf:
	@$(RM) *.pdf

cleanall: clean cleanbib cleanpdf
