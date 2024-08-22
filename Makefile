# Other Makefile config....

# Html theme pour documentation
HTMLTHEME=furo

# Other Makefile config...

docs: docs: $(wildcard docs/html/*.html)
      	HTMLTHEME=$(HTMLTHEME) docs/build_docs.sh

docs-clean:
	rm -rf docs/html docs/code-doc docs/xml-dir docs/venv