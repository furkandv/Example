# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:57:24 2020

@author: FurkanDvv

Binary Search : İkili Arama, sıralı bir dizide, 
belirli değerin bulunmasına yönelik bir algoritmadır. 
Bu teknikteki her bir adımda, aranan değerin, 
dizinin orta değerine eşit olup olmadığı kontrol edilir.

Önce sıralanıp sonra binary search yapılır.
"""
def binarySearch(arr, x):
     
     if len(arr) == 1:
          return arr[0] == x
     
     if arr[len(arr) // 2 ] == x:
          return True
     
     if arr[len(arr) // 2] > x:
          return binarySearch(arr[:len(arr) // 2], x)
     else:
          return binarySearch(arr[len(arr) // 2:], x)
liste = [1,2,3,4,5,6,7,8,11,13,54,56,71,72]

print(binarySearch(liste, 5))