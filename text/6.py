import operator
import re

pieces = ['hello', 'world', 'liudepeng']
#large = reduce( operator.add, pieces, ' ' )
large = ' '.join(pieces)
print large
#reverse = large[::-1]
#print reversea
rewords = re.split(r'(\s+)', large)
rewords.reverse()
restring = ''.join(rewords)
print restring
#print ' '.join(large.split()[::-1])
