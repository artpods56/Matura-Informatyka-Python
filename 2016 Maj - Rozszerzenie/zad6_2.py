file = open("dane_6_2.txt","r")

def encode(slowo,klucz):
    klucz = klucz%26
    decoded = ""
    for letter in slowo:
        if ord(letter) - klucz < 65:
            decoded += chr(ord(letter) - klucz + 26)
        else:
            decoded += chr(ord(letter) - klucz)

    return decoded

try:
    for wiersz in file:
        wiersz = wiersz.split()
        print(encode(wiersz[0],int(wiersz[1])))
except IndexError:
    print(wiersz)