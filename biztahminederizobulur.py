#Biz sayı tutuyoruz o bulmaya çalışıyor.

import random

cvp = " "
x = 0 
y = 1000
sayac = 0

while cvp != "doğru":
    sayac += 1
    tahmin = random.randint(x,y)
    print("Sallıyom Doğru Dimi : " , tahmin)
    cvp = input ("(küçük-büyük-doğru)?:")
    if cvp == "küçük":
        x = tahmin + 1
    elif cvp == "büyük":
        y = tahmin - 1
        
print ("Buldum la valla, görüşürüz gardaşım")
print ("deneme sayısı" , sayac)