"""
Kullanıcıdan isim alınıyor ve 1000 adet parola üretiyoruz.
ismin karakterleri veya sayılarından üretiyor.

"""
import random

def createPassword(name):       #Bir isim alsın ve şifre döndürsün.
    password = ""
    name = name.lower()
    name = name.upper()
    name += "0123456789"
    print (name)
    uzunluk = random.randint(6,10)
    for i in range(uzunluk)
        password += random.choice(name)
        
    return password

name = input("İsminizi giriniz: ")
for i in range(1000)
    print(createPassword(name))