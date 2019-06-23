# jedi-vim-pyversion
Auto set jedi-vim python version with jedi#force_py_version

If current python file belong to python2 path, force jedi-vim py version to
python2 to allow completion. Fallback to jedi 'auto' mode otherwise.
Version can also be forced by touch .python{2|3} in project dir

defaults:

    let jedi_pyversion#enable = 1
    let jedi_pyversion#debug = 0
