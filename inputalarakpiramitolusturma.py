# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:05:10 2020

@author: FurkanDvv

"""
sayi = int(input("Bir sayi giriniz: "))

for i in range(sayi):
    print ("* " * (i+1))
    
    
"""
tersten basma

"""
print("Tersten basma")
sayi = int(input("Bir sayi giriniz: "))

for i in range(sayi):
    
    print ("* " * (sayi - i))
    
