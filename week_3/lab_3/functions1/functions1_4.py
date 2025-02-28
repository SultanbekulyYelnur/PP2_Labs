def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def filter_prime(prime_list):
    result = []
    for i in prime_list:
        if(isPrime(i)):
            result.append(i)
    return result

