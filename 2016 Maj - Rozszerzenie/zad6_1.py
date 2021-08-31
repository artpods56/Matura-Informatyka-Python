plik = open("dane_6_1.txt","r")

dane = []

for linia in plik:
    linia = linia.strip()
    dane.append(linia)

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

### ZAD 6.1 ###
for slowo in dane:
    print(decode(slowo,107))


