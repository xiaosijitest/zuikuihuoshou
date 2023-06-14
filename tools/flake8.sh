#!/bin/sh
set -e -x
cd $(dirname "$0")/..
# use /bin/sh to support "*.py"
# FIXME: add zuikuihuoshou-wx (currrently broken)
flake8 zuikuihuoshou/ tests/ runtests.py setup.py doc/examples/*.py
