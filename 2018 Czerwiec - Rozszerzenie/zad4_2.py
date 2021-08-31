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


def czy_parzysta(num):
    if num%2==0:
        return True
    return False

licznik = 0
for i in range(len(tablica1)):
    parzyste_tab1 = 0
    nieparzyste_tab1 = 0
    parzyste_tab2 = 0
    nieparzyste_tab2 = 0
    for liczba in tablica1[i]:
        if czy_parzysta(int(liczba)) == True:
            parzyste_tab1 += 1
        elif czy_parzysta(int(liczba)) == False:
            nieparzyste_tab1 += 1
    for liczba in tablica2[i]:
        if czy_parzysta(int(liczba)) == True:
            parzyste_tab2 += 1
        elif czy_parzysta(int(liczba)) == False:
            nieparzyste_tab2 += 1
    if parzyste_tab1==5 and nieparzyste_tab1==5 and parzyste_tab2==5 and nieparzyste_tab2 ==5:
        licznik += 1

print(licznik)