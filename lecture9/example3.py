import sys

for line in sys.stdin:
	n1, n2 = line.split(',')
	print(int(n1)+int(n2))
