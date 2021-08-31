plik = open("sygnaly.txt","r")
strings = []
for linia in plik:
    linia = linia.strip()
    strings.append(linia)

naj_dl = 0
naj_string = ""

def ile_roznych(string):
    litery = []
    for letter in string:
        if letter not in litery:
            litery.append(letter)
    len_litery = len(litery)
    return string, len_litery

for string in strings:
#    print(f"{string} oraz ilosc roznych liter {ile_roznych(string)[1]}")
    if ile_roznych(string)[1] > naj_dl:
        naj_dl = ile_roznych(string)[1]
        naj_string = string

print(f"wyraz o najwiekszej ilosci roznych liter w liczbie {naj_dl} to {naj_string}")



