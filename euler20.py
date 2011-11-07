def factorial(top_num):
	factorial_product = 1
	for x in range(2,top_num):
		factorial_product *= x
	return factorial_product

answer = factorial(100)
print answer

list_of_nums = [int(num) for num in str(answer)]
total_nums = 0
for x in list_of_nums:
	total_nums += x
print total_nums