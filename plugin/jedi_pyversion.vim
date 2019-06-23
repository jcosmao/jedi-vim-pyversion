if exists('g:jedi_pyversion#enable') && g:jedi_pyversion#enable == 0
    finish
endif

if !exists('g:jedi_pyversion#debug')
    let g:jedi_pyversion#debug = 0
endif

if has("nvim")
    let jedi_pyversion#enable = 1
    let s:pyscript = resolve(expand('<sfile>:p:h:h')) . '/plugin/jedi_pyversion.py'

    if has('python3')
        execute 'py3file '. s:pyscript
        function! JediForcePythonVersion()
            python3 jedi_force_python_version()
        endfunction
    else
        execute 'pyfile '. s:pyscript
        function! JediForcePythonVersion()
            python jedi_force_python_version()
        endfunction
    endif

    autocmd BufEnter *.py call JediForcePythonVersion()
endif
