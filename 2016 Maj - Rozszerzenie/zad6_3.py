plik = open("dane_6_3.txt","r")


def encode(slowo,klucz):
    klucz = klucz%26
    decoded = ""
    for letter in slowo:
        if ord(letter) - klucz < 65:
            decoded += chr(ord(letter) - klucz + 26)
        else:
            decoded += chr(ord(letter) - klucz)

    return decoded

def decode(slowo,klucz):
    coded_word = ""
    for char in slowo:
        char = ord(char)
        char += klucz
        while char > 90:
#            print(char)
            char -= 90
            char += 64
        coded_word += chr(char)
        #print(chr(char))
    return coded_word

def find_keys(str1,str2):
    div = []
    for i in range(len(str1)):
        r = 0
        klucz1 = ord(str1[i])
        klucz2 = ord(str2[i])
        while klucz1 != klucz2:
            #print(klucz1,klucz2)
            klucz1 += 1
            if klucz1 > 90:
                klucz1 = 65
            r += 1
        if r not in div:
            div.append(r)
    if len(div) > 1:
        return str1,str2
    return  True

for linia in plik:
    linia = linia.strip().split()
    klucz = abs(ord(linia[0][0])-ord(linia[1][0]))
#   print(ord(linia[0][0]),ord(linia[1][0]))
    if find_keys(linia[0],linia[1]) != True:
        print(find_keys(linia[0],linia[1]))

