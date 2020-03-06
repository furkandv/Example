"""
Telefon rehberi uygulaması

"""

rehber =  {}

while True:
    print("\n--------")
    print("kayıt için 1")
    print("arama için 2")
    print("kayıt silme için 3")
    cvp = input("çıkmak için 4: ")
    if cvp == "4":
        break
    elif cvp == "1":
        isim = input("İsim Giriniz: ")
        tel = input ("Telefon Numarası Giriniz: ")
        rehber[isim] = tel
        print ("Telefon numarası eklenmiştir.")
    elif cvp == "2":
        isim = input("Aradığınız Kişi: ")
        if rehber.get(isim) != None:
            print (rehber.get(isim))
        else:
            print("Kişi bulunamadı.")
    elif cvp == "3":
        isim = input("Silmek İstediğiniz İsim ? : ")
        if rehber.get(isim) != None:
            del rehber[isim]
            print("İsim Başarı ile Silindi.")
        else:
            print("İsim Bulunamadı")
    else:
        print("Yanlış Giriş Yaptınız.")
print("Program Bitti.")
for x,y in rehber.items():
    print(x,y)
          