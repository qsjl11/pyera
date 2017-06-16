import os
import shutil

import zipfile

#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)     #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

build_bat_str = \
    r'rd /s/q dist'+'\n' \
    r'rd /s/q pyera_debug'+'\n' \
    r'rd /s/q pyera_release'+'\n' \
    r''+'\n' \
    r'md pyera_debug'+'\n' \
    r'md pyera_release'+'\n' \
    r'cd pyera'+'\n' \
    r'python setupDebug.py build'+'\n' \
    r'xcopy build ..\pyera_debug /e'+'\n' \
    r''+'\n' \
    r'python setupRelease.py build'+'\n' \
    r'xcopy build ..\pyera_release /e'+'\n' \
    r''+'\n' \
    r'rd /s/q build'+'\n' \
    r'cd ..\pyera_debug'+'\n' \
    r'if exist .\exe.win32-3.6 ren .\exe.win32-3.6 pyera'+'\n' \
    r'if exist .\exe.win32-3.5 ren .\exe.win32-3.5 pyera'+'\n' \
    r''+'\n' \
    r''+'\n' \
    r'cd ..\pyera_release'+'\n' \
    r'if exist .\exe.win32-3.6 ren .\exe.win32-3.6 pyera'+'\n' \
    r'if exist .\exe.win32-3.5 ren .\exe.win32-3.5 pyera'+'\n' \
    r''+'\n' \
    r'cd ..'+'\n' \
    r'md .\pyera_debug\data'+'\n' \
    r'xcopy data .\pyera_debug\data /e'+'\n' \
    r'md .\pyera_debug\script'+'\n' \
    r'xcopy script .\pyera_debug\script /e'+'\n' \
    r'copy pyeraDebug.bat .\pyera_debug\pyeraDebug.bat'+'\n' \
    r''+'\n' \
    r''+'\n' \
    r'md .\pyera_release\data'+'\n' \
    r'xcopy data .\pyera_release\data /e'+'\n' \
    r'md .\pyera_release\script'+'\n' \
    r'xcopy script .\pyera_release\script /e'+'\n' \
    r'copy pyeraRelease.bat .\pyera_release\pyera.bat'+'\n' \
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

os.mkdir('dist')
shutil.move('pyera_debug','.\dist')
shutil.move('pyera_release','.\dist')

make_zip('.\dist\pyera_debug','.\dist\pyera_debug.zip')
make_zip('.\dist\pyera_release','.\dist\pyera_release.zip')