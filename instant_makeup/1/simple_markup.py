#!/usr/bin/python

import sys, re
from unit import *
print "<html><head>Simple_Markup</head><body>"

title = True
for block in Blocks( sys.stdin ):
	block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block  );
	if title:
		print "<h1>"
		print block
		print "</h1>"
		title = False
	else:
		print "<p>"
		print block
		print "</p>"

print "</body></html>"
