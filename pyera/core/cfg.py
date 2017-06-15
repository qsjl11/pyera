# -*- coding: UTF-8 -*-
import os
import sys

if getattr(sys, 'frozen', False):
    # frozen
    dir_ = os.path.dirname(sys.executable)
else:
    # unfrozen
    dir_ = os.path.dirname(os.path.realpath(__file__))
print(dir_)
gamepath = dir_[:-10]
print(gamepath)
sys.path.append(gamepath)
print(gamepath)


platform = None
