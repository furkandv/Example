# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:43:56 2020

@author: FurkanDvv

Metindeki karakter sayısını recursive fonksiyon ile bulmak.

"""

def countChar(metin, karakter):
    if len(metin) == 0:
        return 0
    if metin[0] == karakter:
        return 1 + countChar(metin[1:], karakter)
    else: 
        return 0 + countChar(metin[1:], karakter)
metin = "Merhaba Dünya"
print(countChar(metin, 'a')) #metinde kaç tane a harfi var diye sorguladık.

