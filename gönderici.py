"""
Aynı ağda olan bilgisayarla mesajlaşma
gönderici

"""

import socket

senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    mesaj = input("Mesaj: ")
    byteMesaj = bytes(mesaj, "utf-8")
    senderSocket.sendto(byteMesaj, ('localhost' , 12000))