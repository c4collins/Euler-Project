count_primes = 0
prime_num =  1

def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
    
while count_primes < 10001:
	prime_num += 1
	if isprime(prime_num) == True:
		count_primes += 1

print count_primes, "  ", prime_num