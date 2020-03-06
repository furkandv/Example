"""
Kullanıcıdan input alarak random parola oluşturma +++

"""
import random


isim = input ("isminizi giriniz: ")
parola = " " 

for i in range (random.randint(5,8)):
    parola += random.choice(isim)
    
for i in range (random.randint(3,5)):
    parola += str(random.randint(0,9))
    
print ("Parolanız: ",parola)