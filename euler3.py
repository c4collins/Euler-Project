def factors_from_composite(composite):
	# initialize variables
	factors_of_composite = []
	x = 1
	while x < composite / 2:
		if isprime(x) == True and composite % x == 0:
			# if x is prime and an even divisor of the composite number
			largest_factor = x # x is the largest prime even factor
			print "The largest factor is: ", largest_factor
		x += 1
	return largest_factor
	
def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
 

largest_prime_factor = factors_from_composite(600851475143)
print largest_prime_factor