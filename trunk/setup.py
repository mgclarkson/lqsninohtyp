#!/usr/bin/env python

## Enables LINUX os to run py2 files when linked to python2.py

import os
import platform
if platform.system() == 'Windows':
  print 'Windows'
else:
  os.environ['python2.py']=os.getcwd()
