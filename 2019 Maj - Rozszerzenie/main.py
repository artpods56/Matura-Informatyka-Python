""""
plik = open("przyklad.txt","r")

def czy_potega3(liczba):
    x = 0
    i = 0
    while x <= liczba:
        x = pow(3,i)
#        print(f"{x} and {liczba}")
        if x == liczba:
            return True
        else:
            i += 1
    return False

for liczba in plik:
    liczba = int(liczba)
    if czy_potega3(liczba) == True:
        print(liczba)

plik.close()

####################################################################
plik = open("liczby.txt","r")

def silnia(liczba):
    i = 1
    x = 1
    while i <= liczba:
        x *= i
#        print(i)
        i += 1
    return x
for liczba in plik:
    suma = 0
    liczba = liczba.strip()
    for char in liczba:
        char = int(char)
        suma += silnia(char)
#    print(f"{suma} i {liczba}")
    liczba = int(liczba)
    if suma == liczba:
        print(f"{suma} to suma siln cyft liczby {liczba}")
        
"""""

def nwd(a, b):
    a = int(a)
    b = int(b)
    if b > 0:
#        print(a, b, a%b)
        return nwd(b, a%b)
    return a

liczby = []
dzielniki = []
plik = open("przyklad.txt","r")
for liczba in plik:
    liczba = int(liczba.strip())
    liczby.append(liczba)

#print(liczby)


try:
    i = 1
    for liczba in liczby:
        dzielniki.append(nwd(liczby[i - 1], liczby[i]))
#        print(f"{nwd(liczby[i - 1], liczby[i])} to najwiekszy dzielnik liczb {liczby[i - 1]} i {liczby[i]}")
        i += 1
except IndexError:
    pass

print(dzielniki)

i = 1
dl_ciag = 0
naj_dl_ciag = 0
start_ciag = 0
try:
    for i in range(1,500)

    #    print(f"{dzielniki[i-1]} to dzielnik liczb {liczby[i-1]} oraz {liczby[i]}")
        if i > 1:
            if d == dzielniki[i] and dzielniki[i] > 1:
                print(dzielniki[i])
                dl_ciag += 1
            elif d != dzielniki[i]:
                if dl_ciag > naj_dl_ciag:
                    naj_dl_ciag = dl_ciag
                dl_ciag = 0
                start_ciag = liczby[i-dl_ciag]
        d = dzielniki[i]
        i += 1
except IndexError:
    pass

print(naj_dl_ciag)