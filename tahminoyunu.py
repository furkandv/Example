"""
Bilgisayar sayı tutuyor
Biz bilmeye çalışıyoruz
Tahmin küçük ya da büyük olduğunu söylüyor

"""

import random
sayi = random.randint(0,1000)
cvp = -1
denemeSayisi = 0
while sayi != cvp:
    denemeSayisi += 1
    cvp = int(input("Tahmin et: "))
    
    if cvp < sayi:
        print("çok küçük")
    elif cvp > sayi:
        print("çok dedin")
    
print("Aferin la kereta")
print("Deneme sayısı : " , denemeSayisi)