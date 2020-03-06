"""
Factorial işlemleri

"""

def medyan (liste):
    liste.sort()
    print(liste[len(liste)//2])
    
def minimum(liste):
    minValue = liste[0]
    for i in liste:
        if i < minValue:
            minValue = i 
    print(i)

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    return fact

print (factorial(5))