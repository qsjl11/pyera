import os

build_bat_str = \
    r'rd /s/q DEBUG'+'\n' \
    r'rd /s/q RELEASE'+'\n' \
    r''+'\n' \
    r'md DEBUG'+'\n' \
    r'md RELEASE'+'\n' \
    r'cd pyera'+'\n' \
    r'python setupDebug.py build'+'\n' \
    r'xcopy build ..\DEBUG /e'+'\n' \
    r''+'\n' \
    r'python setupRelease.py build'+'\n' \
    r'xcopy build ..\RELEASE /e'+'\n' \
    r''+'\n' \
    r'rd /s/q build'+'\n' \
    r'cd ..\DEBUG'+'\n' \
    r'if exist .\exe.win32-3.6 ren .\exe.win32-3.6 pyera'+'\n' \
    r'if exist .\exe.win32-3.5 ren .\exe.win32-3.5 pyera'+'\n' \
    r''+'\n' \
    r''+'\n' \
    r'cd ..\RELEASE'+'\n' \
    r'if exist .\exe.win32-3.6 ren .\exe.win32-3.6 pyera'+'\n' \
    r'if exist .\exe.win32-3.5 ren .\exe.win32-3.5 pyera'+'\n' \
    r''+'\n' \
    r'cd ..'+'\n' \
    r'md .\DEBUG\data'+'\n' \
    r'xcopy data .\DEBUG\data /e'+'\n' \
    r'md .\DEBUG\script'+'\n' \
    r'xcopy script .\DEBUG\script /e'+'\n' \
    r'copy pyeraDebug.bat .\DEBUG\pyeraDebug.bat'+'\n' \
    r''+'\n' \
    r''+'\n' \
    r'md .\RELEASE\data'+'\n' \
    r'xcopy data .\RELEASE\data /e'+'\n' \
    r'md .\RELEASE\script'+'\n' \
    r'xcopy script .\RELEASE\script /e'+'\n' \
    r'copy pyeraRelease.bat .\RELEASE\pyera.bat'+'\n' \
    r''+'\n'

pyeraRelease_bat_str=\
    r'if "%1"=="h" goto begin'+'\n' \
    r'    start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit'+'\n' \
    r':begin'+'\n' \
    r''+'\n' \
    r'@echo off'+'\n' \
    r'pyera\pyera.exe'+'\n' \
    r'exit'+'\n'

pyeraDebug_bat_str=\
    r'pyera\pyera.exe'+'\n' \
    r'exit'+'\n'

with open('pyeraDebug.bat', 'wt') as f:
    f.write(pyeraDebug_bat_str)

with open('pyeraRelease.bat', 'wt') as f:
    f.write(pyeraRelease_bat_str)

with open('build.bat', 'wt') as f:
    f.write(build_bat_str)

os.system('build.bat')
os.remove('build.bat')
os.remove('pyeraDebug.bat')
os.remove('pyeraRelease.bat')
