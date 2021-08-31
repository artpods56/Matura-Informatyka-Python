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

#####################################################################

liczba_wierszy = 0
for i in range(len(tablica1)):
    if tablica1[i][-1] == tablica2[i][-1]:
        liczba_wierszy += 1

print(liczba_wierszy)