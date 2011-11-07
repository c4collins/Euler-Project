# Initialize variables
import time
start = time.time()
failures = 0 # for counting how many numbers fail the is_triangle check
winner = False
iteration = 1

def is_triangle(num):
	"""Determines whether a number is a triangle number through subtraction"""
	x = 1 # Initialize variables
	while num > 0:
		num -= x	# subtract in sequence
		x +=1	# increment the subtrahend
	if num == 0:	# if it's a triangle number, it will eventually be 0
		return True
	else:
		return False


def prime_factors(num):
	list_of_prime_factors = [num]
	
	while num > 1:
		num_check = num
		factor = 2
		while num_check == num:
			if num % factor == 0:
				num /= factor
				list_of_prime_factors.append(factor)
			factor += 1
	return list_of_prime_factors
	
	
def all_factors(list):
	set_of_all_factors = set(list)
	set_of_all_factors.add(list[0])
	set_of_all_factors.add(1) #adds a one to every set, so it allows you to change what you consider a factor
	for x in range(1, len(list)):
		for y in range(x+1, len(list)):
			if x != y and list[x] * list[y] <= iteration:
				set_of_all_factors.add(list[x] * list[y])
	# print set_of_all_factors
	return len(set_of_all_factors)
	

def is_prime(factor):
	for x in range(2, int(factor**0.5)+1):
		if factor % x == 0:
			return False
		return True
	return False
	

while winner != True:
	if is_triangle(iteration) == True:
		if all_factors(prime_factors(iteration)) >= 500:
			print
			print "The winning number is: ", iteration, "with %d factors." % all_factors(prime_factors(iteration))
			winner = True
		#else:
		#	print  "Working...", iteration
	iteration +=1

print time.time() - start