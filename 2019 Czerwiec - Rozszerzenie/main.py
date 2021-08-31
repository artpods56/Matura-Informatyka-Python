plik = open("liczby.txt", "r")

# print(plik.read())
liczby = []
for liczba in plik:
    liczba = liczba.strip()
    liczby.append(int(liczba))
    # print(liczba)
liczby = sorted(liczby)


# print(liczby)

def czy_pierwsza(liczba):
    i = 2
    if liczba < 2:
        #        print("liczba nie jest pierwsza #1")
        return False
    while i * i <= liczba:
        if liczba % i == 0:
            #           print("liczba nie jest pierwsza #2")
            return False
        i += 1
    return True


# Zadanie 4.1
plik4_1 = open("zadanie4_1.txt", "a")
plik4_1.truncate(0)

for liczba in liczby:
    if czy_pierwsza(liczba) == True and liczba >= 100 and liczba <= 5000:
        plik4_1.write(f"{liczba} ")
plik.close()
plik4_1.close()

# Zadanie 4.2
plik = open("pierwsze.txt", "r")

plik4_2 = open("zadanie4_2.txt", "a")
plik4_2.truncate(0)
pierwsze = []
for liczba in plik:
    liczba_rev = liczba[::-1]
    liczba_rev = int(liczba_rev)
    if czy_pierwsza(liczba_rev) == True:
        plik4_2.write(f"{liczba}")
        print(liczba)

plik.close()
plik4_2.close()

# Zadanie 4.2

plik = open("pierwsze.txt", "r")


def przyklad(liczba):
    n = 0
    for i in liczba:
        n += int(i)
    # print(n)
    if len(str(n)) != 1:
        return przyklad(str(n))
    elif len(str(n)) == 1:
        #        print(f"waga to: {n}")
        return n


count = 0
for liczba in plik:
    liczba = liczba.strip()
    x = przyklad(liczba)
    if x == 1:
        count += 1

print(f"ilosc liczb o wadze 1: {count}")

plik.close()
plik4_3 = open("zadanie4_3.txt", "w")
plik4_3.write(f"ilosc liczb o wadze 1: {count}")
plik4_3.close()
