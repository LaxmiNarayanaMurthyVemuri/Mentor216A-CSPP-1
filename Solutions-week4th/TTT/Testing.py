import random
d = {1:'.', 2:'x', 3:'o'}

for j in range(100):
	l = []
	l.append('\r')
	for i in range(3):
		x = random.randint(1,3)
		y = random.randint(1,3)
		z = random.randint(1,3)
		l.append(d[x])
		l.append(d[y])
		l.append(d[z])
		l.append('\r')
	f = open("input" + str(j+14) + ".txt", "a")
	f.write(" ".join(l))
	print(" ".join(l))
	print('------------')
