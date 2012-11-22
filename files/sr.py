#!/usr/bin/env python
#open
fInput = open( 'input', 'r' )
fOutput = open( 'output', 'w' )

nNumOfLine = 0
for line in fInput:
	#fOutput.write( line.replace( 'facebook', 'FACEBOOK' ) )
	nNumOfLine +=1
print nNumOfLine

fInput.close()
fOutput.close()
#read
#write
