list_of_nums = [int(num) for num in str(2**1000)]
total_nums = 0
for x in list_of_nums:
	total_nums += x
print total_nums