plik1 = open("przyklad1.txt","r")
plik2 = open("przyklad2.txt","r")

tablica1 = []
tablica2 = []
for linia in plik1:
    linia = linia.strip()
    linia = linia.split()
    tablica1.append(linia)

for linia in plik2:
    linia = linia.strip()
    linia = linia.split()
    tablica2.append(linia)

print(tablica1)
print(tablica2)

#####################################################

licznik = 0
wiersze = []

for i in range(len(tablica1)):
    cyfry_tab1 = []
    cyfry_tab2 = []
    ver = True
    for liczba in tablica1[i]:
        for cyfra in liczba:
            print(cyfra)
            if cyfra not in cyfry_tab1:
                cyfry_tab1.append(cyfra)
    for liczba in tablica2[i]:
        for cyfra in liczba:
            if cyfra not in cyfry_tab2:
                cyfry_tab2.append(cyfra)

    for liczba in cyfry_tab1:
        if liczba not in cyfry_tab2:
            ver = False
    for liczba in cyfry_tab2:
        if liczba not in cyfry_tab1:
            ver = False
    if ver == True:
        licznik += 1
        wiersze.append(i+1)

print(wiersze,licznik)