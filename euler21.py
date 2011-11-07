total_sum = 0
number_list = []

def number_list_create(number):
	for x in range(1, number):
		number_list.append(x)

def divisor_sum(num):
	sum_total = 0
	for x in range(1, num):
		if num % x == 0:
			sum_total += x
	return sum_total

number_list_create(10000)

for x in range(1, int(len(number_list)*0.9)):
	num = number_list[x]
	dnum = divisor_sum(num)
	ddnum = divisor_sum(dnum)
	if num == ddnum and dnum == divisor_sum(ddnum) and dnum < 10000:
		number_list.remove(num)
		#number_list.remove(divisor_sum(num))
		total_sum += num + divisor_sum(num)


"""print "num:",num
print "divisor_sum(num):",divisor_sum(num)
print "divisor_sum(divisor_sum(num)):",divisor_sum(divisor_sum(num))"""


	
print "total_sum:",total_sum