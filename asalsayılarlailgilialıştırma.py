"""
10.000 asal sayı bulma işlemi

"""

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    return fact

def isPrime (n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
for i in range (1000000,1010000):
    if isPrime(i):
        print (i)