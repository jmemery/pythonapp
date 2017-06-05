maxCols = 50
maxRows = 15

cols = int(raw_input("Number of columns?"))
rows = int(raw_input("Number of rows?"))

colScale = maxCols / cols
rowScale = maxRows / rows

#colors
g = '\033[47m '
b = '\033[40m '
r = '\033[41m '
e = '\033[0m'

#print top border
print g*(cols*colScale+2) + e

for rNum in range(rows):
	#print row
	for i in range(rowScale):
		row = g
		if  rNum % 2 == 0:
			even = r*colScale
			odd = b*colScale
		else:
			even = b*colScale
			odd = r*colScale
		for j in range(cols):
			if j %2 == 0:
				row += even
			else:
				row += odd
		row += g + e
		print row

#print bottom border
print g*(cols*colScale+2) + e
