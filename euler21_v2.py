amicable_sum = 0

def divisor_sum(num):
	div_sum = -num
	for x in range(1, int(num**0.5)+1):
		if num % x == 0 :
			div_sum += x
			div_sum += num/x
	return div_sum

for x in range(1,10000):
	d_sum = divisor_sum(x)
	print x, " d_sum: ", d_sum
	print x, " divisor_sum(d_sum): ", divisor_sum(d_sum)
	if divisor_sum(d_sum) == x and d_sum < 10000 and d_sum != x:
		print "AMICABLE!"
		amicable_sum += x


print amicable_sum