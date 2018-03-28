BASEFILE=presentation
HANDOUTFILE=handout
NOTEFILE=notes
TEXFILE=$(BASEFILE).tex

TEXCMD=pdflatex
BIBCMD=biber

all:
	$(TEXCMD) $(TEXFILE)

full: clean
	$(TEXCMD) $(TEXFILE)
	$(BIBCMD) $(BASEFILE)
	$(TEXCMD) $(TEXFILE)
	$(TEXCMD) $(TEXFILE)

handout:
	$(TEXCMD) $(HANDOUTFILE).tex
	$(BIBCMD) $(HANDOUTFILE)
	$(TEXCMD) $(HANDOUTFILE).tex
	$(TEXCMD) $(HANDOUTFILE).tex

notes:
	$(TEXCMD) $(NOTEFILE).tex
	$(BIBCMD) $(NOTEFILE)
	$(TEXCMD) $(NOTEFILE).tex
	$(TEXCMD) $(NOTEFILE).tex

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

distclean: clean cleanbib cleanpdf

cleanall: distclean
