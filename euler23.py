def isAbundant(num):
    divisorSum = 1
    
    for x in range(2,int(num**0.5)+1):
        if num % x == 0:
            divisorSum += x
           
    if divisorSum == num:
        print "Perfect"
        return False
    elif divisorSum < num:
        print "Deficient"
        return False
    else:
        print "Abundant"
        return True
    
    
twoAbundant = []

for i in range(1,28):
    res = isAbundant(i)
    print res


#if isAbundant(i):
 #       for j in range(i,28123-i):
  #          if isAbundant(j):
   #             twoAbundant.append(i+j)
                
print twoAbundant