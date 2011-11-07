import time
start = time.time()
 
def countFactors(n=3, c=2):
    #loop to square root, test with modulus, check for squares
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            if i != int(n**0.5)+1:
                c+=2
            else:
                c+=1
    return c
 
def triangleNumbers(i=1):
    #generate triangle numbers with 0.5*n*n1
    while True:
        yield int(0.5*i*(i+1))
        i+=1
 
#loop and a half, generate triangle numbers and count factors
triNums = triangleNumbers()
while True:
    n = triNums.next()
    if countFactors(n) > 500:
        print n
        break
 
print time.time()-start