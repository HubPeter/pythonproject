import itertools

def checkInter1(aset, atext):
	for c in atext:
		if c in aset:
			return True
	return False
def checkInter2(aset, atext):
	if bool(set(aset).intersection(atext)):
		return True
	return False
def checkInter3(aset, atext):
	for item in itertools.ifilter(aset.__contains__, atext):
		return True
	return False
def checkInter4(aset, atext):
	if not set(atext).difference(aset):
		return False
	return True

aset = 'abcd'
atext = 'abcdefthigklmn'
if checkInter4(aset, atext):
	print 'yes'

