#!/usr/bin/env python3


import sys
import os


dir_to_backup = sys.argv[1]
if not os.path.exists(dir_to_backup):
    print ('Oops')
else:
    print ('Found the directory!')
