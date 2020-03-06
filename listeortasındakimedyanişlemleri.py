"""
Listenin ortasındaki değer medyan.
"""

def medyan (liste):
    liste.sort()
    print(liste[len(liste)//2])
    
def minimum(liste):
    minValue = liste[0]
    for i in liste:
        if i < minValue:
            minValue = i 
    print(i)
dizi = [13,14,15,16,221,45,856,147,54,5,25,3]
minimum(dizi)
medyan(dizi)
print(dizi)
    