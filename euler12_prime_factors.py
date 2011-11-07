# euler12_prime_factors.py


def prime_factors(num):
	list_of_prime_factors = [num]
	
	while num > 1:
		num_check = num
		factor = 1
		while num_check == num:
			if num % factor == 0: #and is_prime(factor) == True:
				num /= factor
				list_of_prime_factors.append(factor)
			factor += 1
	
	return list_of_prime_factors
	
def is_prime(factor):
	for x in range(2, int(factor**0.5)+1):
		if factor % x == 0:
			return False
		return True
	return False
	
def all_factors(list):
	set_of_all_factors = set()
	num = list[0]
	for x in range(0, len(list)):
		print list[x]," x:",x
		for y in range(0, len(list)):
			print list[y]," y:",y
			if x != y and list[x] * list[y] <= num:
				print "x:",list[x],"y:",list[y]
				set_of_all_factors.add(list[x] * list[y])
	
	return set_of_all_factors
	
print prime_factors(28)
print all_factors(prime_factors(28))
print is_prime(66666667)