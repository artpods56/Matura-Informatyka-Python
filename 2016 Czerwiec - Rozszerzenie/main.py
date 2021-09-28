plik = open("liczby.txt","r")

def na_sysx(x,sys):
    x = x[::-1]
    l = 0
    for i in range(len(x)):
        l += int(x[i])*pow(sys,i)
    return l


def czy_parzysta(x):
    if x % 2 == 0:
        return True
    return False

osemkowy = 0
czworkowe_bez_zer = 0
dwojkowe_parzyste = 0
suma_osemkowych = 0

kod_najwiekszej = ""
kod_najmniejszej = ""
najwieksza = 0
najmniejsza = 10000000000000


for wiersz in plik:
    wiersz = wiersz.strip()
    sys = wiersz[-1]
    liczba = wiersz[:len(wiersz) - 1]
    if sys == "8":
        osemkowy += 1
    if sys == "4":
        if "0" not in liczba:
            czworkowe_bez_zer += 1
    if sys == "2" and czy_parzysta(na_sysx(liczba,int(sys))) == True:
        #print((na_sysx(liczba,int(sys))))
        dwojkowe_parzyste += 1
    if sys == "8":
        suma_osemkowych += na_sysx(liczba,int(sys))

    if na_sysx(liczba,int(sys)) > najwieksza:
        najwieksza = na_sysx(liczba,int(sys))
        kod_najwiekszej = liczba

    if na_sysx(liczba, int(sys)) < najmniejsza:
        najmniejsza = na_sysx(liczba, int(sys))
        kod_najmniejszej = liczba+sys

    #print(na_sysx(liczba,int(sys)))

print("Zad 6.1")
print(osemkowy)
print("")


print("Zad 6.2")
print(czworkowe_bez_zer)
print("")

print("Zad 6.3")
print(dwojkowe_parzyste)
print("")

print("Zad 6.4")
print(suma_osemkowych)
print("")

print("Zad 6.5")
print(kod_najmniejszej,"",najmniejsza)
print(kod_najwiekszej,"",najwieksza)

