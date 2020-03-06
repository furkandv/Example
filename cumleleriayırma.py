"""
Cümleler nasıl ayrılır ? 
"""


def ayir(cumle):
    kelimeler = []
    
    kelime = " "
    for i in cumle:
        if i == " ":
            kelimeler.append(kelime)
            kelime = ""
        else: 
            kelime += i
    kelimeler.append(kelime)
    return kelimeler

metin = "Your registration is confirmed, and your virtual seat awaits! Please be sure you've got the time blocked on your calendar to join us: there's a handy link below to add the webinar to your calendar, as well as a link to join when the time rolls around."

print (ayir(metin))
print ()
print(metin.split(" "))