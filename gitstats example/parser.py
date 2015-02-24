from lxml.html import parse
import time

doc = parse("authors.html")
rows = doc.xpath("body/table")[0].findall("tr")
data = list()
f = open("authordata.dat", "w")

#parses table data
for row in rows:
	data.append([c.text for c in row.getchildren()])

#writes the time the programmer joined and the LoC at that point onto the new file
for row in data[1:]: 
	n = int(time.mktime(time.strptime(row[4] + " 12:00:00", "%Y-%m-%d %H:%M:%S")))
	n = str(n)
	f.write(n + " ")
	g = 87884
	g = str(g)
	f.write(g + "\n")
