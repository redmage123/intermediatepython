#!/usr/bin/env python3
import os
import subprocess


x = subprocess.Popen(['ls','/etc'])
print (x.stdout.read())
