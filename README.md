# Sample repo for documentation generation for C/C++ projects

## Requirements
For this to work, we need:
- Python >= 3.8 (Verify with python3 -v)
- Doxgen (doxygen)

## Generating
The theme is configurable in each type of file 

Makefile: `make docs` 

CMake: `cmake --build <cmake-build-dir> --target docs`

Search for themes here: https://sphinx-themes.org/