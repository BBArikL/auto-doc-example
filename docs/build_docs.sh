doxygen docs/Doxyfile -o docs
cd docs || return
test -d venv || python3 -m venv venv
source ./venv/bin/activate
pip install -U sphinx breathe myst_parser setuptools "$HTMLTHEME"
if sphinx-build -b html . html -D html_theme="$(echo "$HTMLTHEME" | sed "s/-/_/g")" ; then
  cp ../*.cpp ../*.h ../*.md -t html
  xdg-open html/index.html
fi
cd ..