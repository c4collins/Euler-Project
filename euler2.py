def fibonacci(max_factor):
	# initialize variables
	num1 = 1
	num2 = 1
	even_total = 0
	while num1 < max_factor:
		# generate fibonacci series
		num_total = num1 + num2
		num2 = num1
		num1 = num_total
		if num2 % 2 == 0:
			# evaluate and add all even terms
			even_total += num2
	return even_total

print fibonacci(4000000)