"""
Mesajlaşma alıcı kişi
"""
import socket

receiverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiverSocket.bind(('', 12000))

while 1:
    byteMesaj, ipAddress = receiverSocket.recvfrom(2048)
    mesaj = byteMesaj.decode("utf-8")
    print(mesaj)