#initialize variables
square_total = 0
sum_total = 0

for x in range(1,101):
	# evaluate the range for sum and squares
	sum_total += x
	square_total += x**2

print "Sum Total Squared is: ", sum_total**2
print "Square Total is: ", square_total
print "Difference is ", sum_total**2 - square_total