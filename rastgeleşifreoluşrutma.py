import random 
def rastgele (kac):
        alfabe = "abcdefghijklmnoprstuvyzwx"
        alfabe = (alfabe.upper() + alfabe.lower())
        sayi = "0123456789"
        karakter = "!'^+%&/()=?_>£#$½6{[}\|<>"
        liste = list(alfabe + sayi + karakter)
        rand = (random.sample(liste, kac))
        print (*rand, sep ="")
        
rastgele(11)