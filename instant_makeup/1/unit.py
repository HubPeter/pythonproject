#
#
#
#

def fLines( file ):
	"Get lines from file and append \n"
	for line in file:
		yield line
	yield '\n'

def fBloc( file ):
	"Get blocks array"
	block = []
	for line in fLine( file ):
		if line.strip():
			block.append()
		elif block:
			''.join(block).strip()
		block = []
