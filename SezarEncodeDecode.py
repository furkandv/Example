# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:55:58 2020

@author: FurkanDvv

"""
def ceasar(text, n):
     newText = ""
     for i in text:
          newChr = chr(ord(i) + n)
          newText += newChr
     return newText
     
text = input ("Enter a text: ")
n = int(input("Enter a number: "))

encodedText = ceasar(text,n)
print(encodedText)
decodedText = ceasar(encodedText, n * -1)
print(decodedText)
