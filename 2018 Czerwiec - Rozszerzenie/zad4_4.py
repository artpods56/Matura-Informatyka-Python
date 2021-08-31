plik1 = open("przyklad1.txt","r")
plik2 = open("przyklad2.txt","r")

tablica1 = []
tablica2 = []
for linia in plik1:
    linia = linia.strip()
    linia = linia.split()
    tab = []
    for liczba in linia:
        tab.append(int(liczba))
    tablica1.append(tab)


for linia in plik2:
    linia = linia.strip()
    linia = linia.split()
    tab = []
    for liczba in linia:
        tab.append(int(liczba))
    tablica2.append(tab)

print(tablica1)
#print(tablica2)

####################################################


"""
    x = 0
    j = 0
    while x <= len(tablica1[i]):
        if tablica1[i][x] == tablica1[i][j]:
            tablica.append(tablica1[i][x])
            x += 1
            continue
        if tablica1[i][x] > tablica1[i][j]:
            tablica.append(tablica1[i][x])
            x += 1
            continue
        if tablica1[i][x] < tablica1[i][j]:
            tablica.append(tablica1[i][j])
            j += 1
            continue
 """

for i in range(len(tablica1)):
    x = 0
    y = 0
    tab1 = tablica1[i]
    tab2 = tablica2[i]
    tablica = []
    while x < len(tab1) and y < len(tab2):
        if tab1[x] == tab2[y]:
            tablica.append(tab1[x])
            if x == len(tab1) - 1:
                tablica.extend(tab2[x:])
                break
            if y == len(tab2) - 1:
                tablica.extend(tab1[y:])
                break
            x += 1
            continue
        if tab1[x] > tab2[y]:
            tablica.append(tab2[y])
            if x == len(tab1) - 1:
                tablica.extend(tab2[x:])
                break
            if y == len(tab2) - 1:
                tablica.extend(tab1[y:])
                break
            y += 1
            continue
        if tab1[x] < tab2[y]:
            tablica.append(tab1[x])
            if x == len(tab1) - 1:
                tablica.extend(tab2[x:])
                break
            if y == len(tab2) - 1:
                tablica.extend(tab1[y:])
                break
            x += 1
            continue
    print(tablica)
    i += 1



