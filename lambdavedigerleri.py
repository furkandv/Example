# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:17:50 2020

@author: FurkanDvv

"""
#---------------------------------------
"""
lambda
 
ciftMi4 = lambda n : n % 2 == 0

"""
#--------------------------------------

"""
bir fonksiyon yazalım 
sayı asal ise true değilse false dönsün


def isPrime(n):
    counter = 0
    for i in range (2,n):
        if n % i == 0:
            counter += 1
    return counter == 0
#print(isPrime(5)) // tek sayıyı sorgular.
"""
    
"""

100 ile 200 arasındaki asal sayılar

for i in range (100,200):
    print (i , isPrime(i))
    
"""

"""
1m ile 2 m arasındaki asal sayıları bulun. (hızlı)

"""

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:  # eğer sayı tam bölünmüyor ise false dönsün
            return False
    return True

for i in range (1000000,2000000):
    if isPrime(i):
        print(i)

