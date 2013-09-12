#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import walk
from os import getcwd
from os.path import join
from re import compile

def handler(error):
    print error

pattern=compile(r'(<title>)КИТ(</title>)')

modified = []

for root, dirs, files in walk(getcwd(), onerror=handler):
    for name in files:
        if(not name.endswith('html')):
            continue
        path = join(root, name)
        file = open(path, 'r+b')
        fulltext = file.read()
        file.seek(0)
        if pattern.search(fulltext):
            modified.append(path)
            fixed = pattern.sub(r'\1ШРИ\2', fulltext)
            file.write(fixed)
            file.truncate()
        file.close()

for i in modified:
    print i
print len(modified)
