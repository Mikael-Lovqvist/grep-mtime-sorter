#!/bin/bash
grep --color=always -rin "$@" --include "*.py" | python /absolute/path/to/grep-mtime-sorter.py