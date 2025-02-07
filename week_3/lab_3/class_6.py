def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

f= filter(isPrime, [1,3,4,5,7,11])
for i in f:
    print(i)