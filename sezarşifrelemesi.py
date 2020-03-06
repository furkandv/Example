"""
parametreden bir text ve key alan, encoded text'i
return eden bir sezar şifreleme metodu yazın.

"""
def ceasar(text, key):
    encodedText = ""
    for i in text:
        encodedText += chr(ord(i) + key)
        
    return(encodedText)

text = "merhaba"
key = 10000

encodedText = ceasar(text,key)
print(encodedText)

decodedText = ceasar(encodedText, key*-1)
print(decodedText)

    