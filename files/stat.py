#!/usr/bin/env python
#coding  = utf-8
import os
isost = os.stat('/media/ADATA UFD/debian.iso')
print 'mode',isost.st_mode
print 'dev',isost.st_dev
print 'uid',isost.st_uid
print 'gid',isost.st_gid
print 'size',isost.st_size
print 'atime',isost.st_atime
print 'mtime',isost.st_mtime
print 'ctime',isost.st_ctime

