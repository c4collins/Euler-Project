answer = -1

for x in range(999,100,-1):
	for y in range(999,x,-1):
		product = str(x * y)
		if int(product) > 100000:
			pro_ = product[:len(product)/2]
			_duct = product[-(len(product)/2):]
			_duct = _duct[::-1]
			if pro_ == _duct and product > answer:
				print product, " ", pro_, " ", _duct, " ", x, " ", y
				answer = product

print "The answer is: ", answer