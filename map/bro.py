#question:how to find a brother word from a container
#goal:find it
#methods:1.
#result:1.ok
#choice:1

def getHash( myWord ):
	if not myWord:
		print 'word is empty'
		return
	hashValue = 0
	for c in myWord:
		hashValue += ord(c)
	return hashValue

def makeTable( myList ):
	if not myList:
		print 'words list is empty'
		return
	hashTable = {}
	for myWord in myList:
		hashTable[getHash( myWord )] = myWord
		print getHash( myWord )
	return hashTable

def myFind( myWord, hashTable ):
	if not myWord:
		print 'word is nothing'
		return False #0
	hashValue = getHash( myWord )
	print 'key:', hashValue
	try:
		hashTable[hashValue]
	except:
		return False
	else:
		if sorted(hashTable[hashValue])==sorted(myWord):
			return True
		else:
			return False

myList = ['liudepeng','fanyiwei','kangtiantian','liufangfang']
myWord = 'fwaneyjh'
hashTable = makeTable( myList )
bResult = myFind( myWord, hashTable )
if bResult:
	print 'Hi brother :)'
else:
	print 'Welcome again :('
