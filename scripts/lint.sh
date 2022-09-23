#!/usr/bin/env bash

set -e
set -x

mypy msaUtils
flake8 msaUtils docs_src
black msaUtils docs_src --check
isort msaUtils docs_src scripts --check-only

