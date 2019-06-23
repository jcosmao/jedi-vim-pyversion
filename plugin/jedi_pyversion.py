#!/usr/bin/env python

import json
import os
import subprocess
import vim


def set_jedi_py_version(version='auto'):
    try:
        debug = int(vim.eval("g:jedi_pyversion#debug"))
    except Exception:
        debug = None

    if debug == 1:
        print("JEDI version forced to '{}'".format(version))
    vim.command("let g:jedi#force_py_version = '{}'".format(version))


def force_pyversion_file(current_file_path):
    dirs = current_file_path.split('/')
    while len(dirs) > 0:
        if os.path.isfile("{}/.python2".format('/'.join(dirs))):
            set_jedi_py_version('2')
            return True
        elif os.path.isfile("{}/.python3".format('/'.join(dirs))):
            set_jedi_py_version('3')
            return True
        else:
            dirs.pop()
    return False


def jedi_force_python_version():
    try:
        current_file_path = vim.eval("expand('%:p:h')")

        # Check if a file .pythonX exist in project path
        if force_pyversion_file(current_file_path):
            return

        # get python2 sys.path (wether we are in pyton2 or 3)
        output = subprocess.check_output(
            'python2 -c "import sys; import json; print(json.dumps(sys.path))"',
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True,
        )
        py2_sys_path = json.loads(output)
        py2_sys_path.remove('')
        # check if we are in a python2 dir
        for python_path in py2_sys_path:
            if python_path in current_file_path:
                set_jedi_py_version('2')
                return
    except Exception:
        pass

    # Default behavior
    set_jedi_py_version('auto')
