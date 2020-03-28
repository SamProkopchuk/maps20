import math as m

for i in range(int(input())):
	n, l, d, g = list(map(int, input().split()))
	# n = sides
	# l = side length
	# d = expansion distance
	# g = land grabs
	apothem = l/2*m.tan(m.pi*(n-2)/(2*n))
	area = 0.5*n * l *apothem
	ds = g*d
	area += (ds)**2*m.pi
	area += n * l * ds
	print(area)
