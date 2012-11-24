from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
	# Year Month Predicted High Low
	( 2007, 8, 101, 104, 99	 ),
	( 2007, 9, 	102, 104, 100),
	( 2007, 10, 103, 104, 100	),
	( 2007, 11, 104,	105, 103),
	( 2007, 12, 109,	109, 107),
	( 2008, 1,	119, 110, 107)
]
drawing = Drawing( 200, 150 )
#data
pred = [ row[2]-40 for row in data ]
high = [ row[3]-40 for row in data ]
low = [ row[4]-40 for row in data ]
times = [ 200*((row[0] + row[1]/12.0) - 2007)-110 for row in data ]
#graphics
predLine = PolyLine( zip( times, pred ), strokeColor = colors.blue )
highLine = PolyLine( zip( times, high ), strokeColor = colors.red )
lowLine = PolyLine( zip( times, low ), strokeColor = colors.green )
title = String( 60, 110, 'Sunspots', fontsize=14, fillColor=colors.blue )
#add
drawing.add( predLine )
drawing.add( highLine )
drawing.add( lowLine )
drawing.add( title )
#save to file
renderPDF.drawToFile( drawing, 'prototype.pdf', 'Report of weater in \
	special aspect' )
