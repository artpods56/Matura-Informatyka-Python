plik = open("sygnaly.txt","r")
strings = []
for linia in plik:
    linia = linia.strip()
    strings.append(linia)

slowo = ""

for i in range(39,len(strings),40):
    linia = strings[i]
    slowo += linia[9]

print(slowo)