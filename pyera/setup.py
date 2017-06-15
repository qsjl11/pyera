import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Program Files (x86)/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Program Files (x86)/Python36-32/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['./script','./data','C:/Program Files (x86)/Python36-32/DLLs/tcl86t.dll', 'C:/Program Files (x86)/Python36-32/DLLs/tk86t.dll'],
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None
base=None

executables = [
    Executable('pyera.py', base=base)
]

setup(name='pyera',
      version = '0.1',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)