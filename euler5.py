#initialize variables
is_found = False
num_to_check = 2520

while is_found != True:
	num_to_check += 20
	# has to be a multiple of 20
	for x in range(1,20): # avoid div_by_zero
		# iterates until it finds a non-zero modulo
		if num_to_check % x != 0:
			is_found = False
			break
		else:
			# might be triggered, but will usually be overwritten
			is_found = True
	# when this loop finds a number that has no non-zero modulos
	# for divisors of 1-20, is_found returns True and exits the while

print num_to_check