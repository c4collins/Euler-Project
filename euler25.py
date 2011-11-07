def fibonacci(length):
	# initialize variables
	num1 = 1
	num2 = 1
	even_total = 0
	term = 2
	while len(str(num1)) < length:
		# generate fibonacci series
		num_total = num1 + num2
		num2 = num1
		num1 = num_total
		term += 1
	return term

print fibonacci(1000)