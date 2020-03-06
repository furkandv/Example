# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:50:27 2020

@author: FurkanDvv

Lineer Search : Bilgisayar bilimlerinde, doğrusal arama 
 veya sıralı arama, listedeki bir öğeyi bulma yöntemidir.
 Bir eşleşme bulunana veya listenin tamamı aranana kadar
 listenin her bir öğesini sırayla kontrol eder. 
 Doğrusal bir arama en kötü doğrusal zamanda yapılır 
 ve en çok n karşılaştırması yapar, burada n listenin uzunluğudur.

"""

def lineerSearch(arr, elm): # Listede x elemanı var mı ?
     for i in arr:
          if i == elm:
               return True
     return False
def countElement(arr, elm): # listede kaç defa aynı eleman var ?
     counter = 0
     for i in arr:
          if i == elm:
               counter += 1
     return counter
def search(arr, elm):
     return countElement(arr, elm) != 0

liste = [5,4,6,78,41,54,54,65,98,72,4,6,4]
print(lineerSearch(liste, 41)) 
print(countElement(liste, 54))    
print(search(liste,99)) 
    

