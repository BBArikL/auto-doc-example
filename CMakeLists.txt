cmake_minimum_required(VERSION 3.28)

set(CMAKE_CXX_COMPILER 17)
set(HTMLTHEME "furo")

project(auto-doc-example)

add_custom_target(docs COMMAND ${CMAKE_COMMAND} -E env "HTMLTHEME=${HTMLTHEME}" "docs/build_docs.sh" WORKING_DIRECTORY "../")
add_custom_target(docs-clean COMMAND rm -rf docs/code-doc docs/html docs/venv docs/xml-dir WORKING_DIRECTORY "../")

add_library(auto-doc-example library.cpp library.h)