from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello Liudepeng', textAnchor='middle')

data = [
	# year month predicted high low
	(2007, 12,	4.8,	5.0,	4.7),
	(2008, 1,	4.3,	4,4,	4,2)
	]

d.add(s)

renderPDF.drawToFile( d, 'hello.pdf', 'Hello Document' )

