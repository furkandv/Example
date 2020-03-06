"""
digital root 
n=4593
4 + 5 + 8 + 9 + 3 = 29
2 + 9 = 11
1 + 1 = 2 

metod n sayısını alıp rootu return etmeli.
"""
 


"""           
def digitalRoot(n):
    n = str(n)
    counter = 0
    while len(n) != 1: # bir olduğunda durmasını istiyoruz
        for i in n:
            counter += int (i)
        n = str(counter)
        counter = 0
    return int(n)

print(digitalRoot(1234255355485))
"""

"""
daha okunaklı yazmak için

"""

def sumofDigits(n):
    count = 0
    n = str(n)
    for i in n:
        count += int(i)
    return str(count)
def digitalRoot(n):
    n = str(n)
    while len(n) != 1: # bir olduğunda durmasını istiyoruz
         n = sumofDigits(n)
    return int(n)
print(digitalRoot(45983))