import math

# n - number of elements
# k - number of distinct elements
# combination(number of elements, number of distinct elements)

# n! / k!(n - k)!
# if k <= n; when k > n, the answer is 0

n = 40
k = 20 # per Project Euler #15
answer = 0

if k <= n:
	answer = math.factorial(n) / ( math.factorial(k) * math.factorial(n-k) )

print "The answer is: ", answer	
