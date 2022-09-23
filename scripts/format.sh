#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --in-place msaUtils docs_src --exclude=__init__.py
black msaUtils docs_src
isort msaUtils docs_src
