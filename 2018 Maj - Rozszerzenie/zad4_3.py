plik = open("sygnaly.txt","r")
strings = []
for linia in plik:
    linia = linia.strip()
    strings.append(linia)


wynik = []
for string in strings:
    for letter in string:
        ver = True
        for i in range(len(string)):
            diff = abs(ord(letter) - ord(string[i]))
            #print(f"{diff} to roznica miedzy {letter} a {string[i]}")
            if diff > 10:
                ver = False
                break
    if ver == True:
        wynik.append(string)
print(wynik)
