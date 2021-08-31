plik = open("galerie.txt","r")
dane = []
for linia in plik:
    linia = linia.strip()
    linia = linia.split()
    dane.append(linia)

#print(dane)
licznik = []

for kraj in dane:
    if [kraj[0],0] not in licznik:
        licznik.append([kraj[0],0])

for kraj in dane:
    for i in range(len(licznik)):
        if kraj[0] == licznik[i][0]:
            licznik[i][1] += 1

print(licznik)