"""
Bir method yazın, çağrıldığı zaman yediye bölünebilen fakat beşin katı olmayan
tüm 2000-3000 arasındaki sayıları ekrana basın

"""
def a():
    for i in range(2000,3000):
        if i %7 == 0 and i % 5 != 0:
            print(i)
a()