import time

t0 = time.time()

def isAbundant(num):
    # Returns true if num is an Abundant number
    divisorSum = 1
    
    for x in range(2,num):
        if num % x == 0:
            divisorSum += x
           
    if divisorSum == num:
        #print "Perfect"
        return False
    elif divisorSum < num:
        #print "Deficient"
        return False
    else:
        #print "Abundant"
        return True
    
  
    
abundants = set()
total = 0
minNum = 1
maxNum = 28123


for i in range(minNum, maxNum):
    if isAbundant(i):
        abundants.add(i)
    if not any((i-a in abundants) for a in abundants):
        total += i
                
print total
print time.time() - t0