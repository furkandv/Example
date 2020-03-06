"""

Bir zar atıldığı zaman toplamının iki gelme olasılığı 
Bir zar atıldığı zaman toplamının üç gelme olasılığı 
Bir zar atıldığı zaman toplamının dört gelme olasılığı 
Deneysel olasılık ile hesaplıyoruz.
Bunun için 10 bin defa 2 adet zar atıp
Gelen sonuçları bir listeye yazarak olasılığı hesaplayacağız.

"""
import random
sonuclar = [0] * 11 

for i in range(10000):
    sonuc = random.randint(1,6) + random.randint(1,6)
    sonuclar[sonuc - 2] += 1 #en son indeksi 1 arttırdık
    
for i in range(len(sonuclar)):
    print(str(i+2) + " Gelme olasılığı = " + str(sonuclar[i] / 100))