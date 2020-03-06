"""
Artık Yıl Hesaplama
Artık yıl true çıkaracak artık değilse false çıkaracak.
"""


def isLeapYear(year):
    if year % 4 == 0: # 4 e bölünebiliyorsa...
        if year % 400 == 0: #400 e tam bölünebiliyorsa
            return True
        else:
            return year % 100 != 0
    else:
        return False

print(isLeapYear(2000))
print(isLeapYear(1900))
print(isLeapYear(2100))
print(isLeapYear(2120))
print(isLeapYear(2004))
print(isLeapYear(2003))
print(isLeapYear(2023))
print(isLeapYear(2024))
