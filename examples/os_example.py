#!/usr/bin/env python3

import os

print (os.popen('ls').readlines())

print (os.getcwd())

os.chdir('/var/lib/postgresql')
print (os.getcwd())
print (os.listdir('/usr/local'))
os.mkdir('/root/foo')
os.chdir('/usr/local')
print (os.path.basename(os.getcwd()))

