for a in range(1, 1000):
	for b in range(a, 1000-a):
		c = 1000 - b - a
		if a**2 + b**2 == c**2:
			if a + b + c == 1000:
				print "A is: %d, B is: %d, C is: %d." % (a, b, c)
				print "The product of abc is: ", a*b*c