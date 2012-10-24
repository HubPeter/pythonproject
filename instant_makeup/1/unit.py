def Lines( file ):
	for line in file:
		yield line
	yield '\n'

def Blocks( file ):
	block = [];
	for line in Lines( file ):
		if line.strip():
			block.append(line);
		else:
			yield ''.join(block).strip()
			block = [];
