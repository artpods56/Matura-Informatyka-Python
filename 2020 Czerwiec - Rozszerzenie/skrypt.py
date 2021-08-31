plik_pary = open("pary.txt", "r")
wyniki = open("wyniki4.txt", "w")
wyniki.truncate()

liczby = []
napisy = []
a = 0
for linijka in plik_pary:
    linijka = linijka.split()
    liczby.append(linijka[0])
    napisy.append(linijka[1])


# print(liczby)
# print(napisy)

def spr_pierwsza(a):
    if a < 2:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True


# liczby_pierwsze = []
# for x in range(100):
#    if spr_pierwsza(x):
#        liczby_pierwsze.append(x)


def suma_pierwszych(liczba):
    if liczba == 4:
        return 2
    k = 3
    while k <= liczba and spr_pierwsza(k) and not spr_pierwsza(liczba - k):
        k += 2
    return k


############### Zadanie 4.1 ###############
wyniki.write("Zadania 4.1:\n")
for liczba in liczby:
    liczba = int(liczba)
    if spr_pierwsza(liczba):
        #print(f"liczba jest pierwsza: {liczba}")
        pass
    elif liczba%2==0:
        #print(f"liczba jest parzysta: {liczba}")
        y = suma_pierwszych(liczba)
        print(f"{liczba} {y} {liczba-y}")
        wyniki.write(f"{liczba} {y} {liczba - y}\n")

############### Zadanie 4.2 ###############
wyniki.write("\nZadania 4.2:\n")
def najdluzszy(napis, pozycja):
    d = 0
    pozycja = 0
    i = 0
    while i < len(napis):
        j=i+1
        while j<len(napis) and napis[i] == napis[j]:
            j+=1
        if d < j-i:
            d = j-i
            pozycja = i
        i = j
    return d, pozycja

slowo = ""
for napis in napisy:
    pozycja = 0
    d = najdluzszy(napis, pozycja)[0]
    pozycja = najdluzszy(napis, pozycja)[1]
    slowo = napis[pozycja:pozycja+d]
    print(f"{slowo} {d}")
    wyniki.write(f"{slowo} {d}\n")

############### Zadanie 4.3 ###############
wyniki.write("\nZadanie 4.3: \n")
i = 0
para = [0,""]
for i in range(len(napisy)):
    if int(liczby[i]) == len(napisy[i]):
#        print(f"{liczby[i]} {napisy[i]}")
        if para[0] == 0 and para[1] == "" or int(liczby[i])<=int(para[0]) and napisy[i] < para[1]:
            para.clear()
            para.append(liczby[i])
            para.append(napisy[i])
    i += 1
wyniki.write(f"{para[0]} {para[1]}")
print(para)



