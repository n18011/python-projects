#!/usr/bin/python3

import os, sys
from datetime import datetime

day = datetime.now().strftime('%Y%m%d')
dirspath = '/home/n18011/work/memo'
filename = '{}/memo.{}'.format(dirspath, day)

if not os.path.isdir(dirspath):
    os.makedirs(dirspath)


if os.path.isfile(filename):
    memofile = open(filename, 'a')
else:
    memofile = open(filename, 'w')

for text in sys.argv[1:]:
    memofile.write(text + '\n')
memofile.close()
