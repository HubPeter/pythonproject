#!/usr/bin/env python
#coding=utf-8
import linecache
#linecache.checkcachecache('input')
theline = linecache.getline( 'input', 2 )
#print thelinea

def getline( filename, linenum ):
	for curlinenum, line in enumerate( open(filename, 'rU') ):
		if curlinenum == linenum-1:
			return line
	return ''

line = getline('input', 2)
print line

#count = len( open('input', 'rU').readlines() )
#print count

count = -1
for count, line in enumerate(open('input', 'rU')):
	pass
count += 1
#print count
count = 0
isofile = open('/media/本地磁盘_/software/OS and tools/系统/linux/debian-6.0.6-i386-netinst.iso', 'rb')
isoout = open('/media/ADATA UFD/debian.iso','wb')
while True:
	buffer = isofile.read(8192*1024)
	isoout.write(buffer)
	if not buffer:
		break
	count += buffer.count('\n')
print count
isoout.close()
isofile.close()
