"""
Recursive fonksiyon
Not : Durdurma işlemine basecase  denir.

"""
def fonk(n):
    if n==0: #basecase
        return
    print(n)
    fonk(n-1)

def faktoriyel(n):
    if n == 1:
        return 1
    return n * faktoriyel(n-1)
print(faktoriyel(5))