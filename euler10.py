def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
    
prime_total = 0
    
for the_number in range(1,2000000):
	if isprime(the_number):
		prime_total += the_number

print prime_total