# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:07:53 2020

@author: FurkanDvv
Ceasar Şifre Hakkında
"""

def ceasar(text, n):
     newText = ""
     for i in text:
          newChr = chr(ord(i) + n)
          newText += newChr
     print(newText)
     
ceasar("merhaba dünya", 1)
ceasar("merhaba dünya", 2)
ceasar("merhaba dünya", 3)
