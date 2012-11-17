myStr = 'Liudepeng'
#for c in myStr:
#	print ord(c),
#print map( ord, myStr )
def isString(obj):
	return isinstance(obj, basestring)

def isString2(obj):
	try:
		obj+' '
	except:
		return false
	else:
		return true

if isString2(myStr):
	print "Yes"
else:
	print "No"
