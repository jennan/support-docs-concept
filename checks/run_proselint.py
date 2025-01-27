#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
"""

import sys
import proselint
from proselint import config, tools

if __name__ == "__main__":

    ret_code = 0

    files = sys.argv[1:]

    # Load defaults from config.
    config_custom = tools.load_options(config_file_path=".proselint.json", conf_default=config.default)

    for file in files:
        print(f"Running proselint on {file}")
        with open(file, "r", encoding="utf8") as f:
            for notice in proselint.tools.lint(f.read(), config=config_custom):
                ret_code += 1
                print(f"::{notice[7]} file={file},line={notice[2]+1},col={notice[3]+2},endColumn={notice[2]+notice[6]+1},title={notice[0]}::'{notice[1]}'", flush=True)
                sys.stdout.flush()
    sys.exit(0)
    # sys.exit(ret_code)
