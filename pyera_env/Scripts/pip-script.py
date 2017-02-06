#!D:\pyera\pyera_env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==7.1.0','console_scripts','pip'
__requires__ = 'pip==7.1.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==7.1.0', 'console_scripts', 'pip')()
    )
