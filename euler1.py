total = 0 # initialize the total variable
for x in range(1,1000): 
    if x % 3 == 0 or x % 5 == 0: # if the number is evenly divisible by 3 or 5, add it to the total
        total += x
print total
