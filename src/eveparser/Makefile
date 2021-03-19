ANTLR_JAR = __antlr__/antlr-4.9.2-complete.jar
ANTLR_JAR_URL = https://www.antlr.org/download/antlr-4.9.2-complete.jar
ANTLR = java -Xmx500M -cp "$(ANTLR_JAR)" org.antlr.v4.Tool
ANTLR_OPTIONS = -Dlanguage=Python3 -visitor
OUTDIR = ./parser_output

.PHONY: build clean

$(OUTDIR)/EveScriptParser.py: EveScript.g4 $(ANTLR_JAR)
	$(ANTLR) $(ANTLR_OPTIONS) -o $(OUTDIR) $<

$(ANTLR_JAR):
	wget $(ANTLR_JAR_URL) -O $(ANTLR_JAR)

build: $(OUTDIR)/EveScriptParser.py

clean:
	rm -rf $(OUTDIR)/__pycache__
	rm $(OUTDIR)/EveScript*