plik = open("galerie.txt","r")
dane = []
for linia in plik:
    linia = linia.strip()
    linia = linia.split()
    dane.append(linia)

#print(dane)
licznik = []

def p_powierzchni(x,y):
    p = x*y
    return p

i = 0
max = ["",0]
min = ["",100000]
min_lokale = ["",100]
max_lokale = ["",0]

for miasto in dane:
    suma_p = 0
    liczba_lokali = 0
    pola_lokali = []
#    print(miasto)
    for i in range(2,len(miasto),2):
        if int(miasto[i]) != 0 and int(miasto[i+1]) != 0:
            suma_p += p_powierzchni(int(miasto[i]),int(miasto[i+1]))
            liczba_lokali += 1
            p = p_powierzchni(int(miasto[i]),int(miasto[i+1]))
            if p not in pola_lokali:
                pola_lokali.append(p)
    if suma_p > max[1]:
        max[0] = miasto[1]
        max[1] = suma_p
    if suma_p < min[1]:
        min[0] = miasto[1]
        min[1] = suma_p
#            print(miasto[i],miasto[i+1])
    if len(pola_lokali) > max_lokale[1]:
        max_lokale[0] = miasto[1]
        max_lokale[1] = len(pola_lokali)
    if len(pola_lokali) < min_lokale[1]:
        min_lokale[0] = miasto[1]
        min_lokale[1] = len(pola_lokali)
#    print(len(pola_lokali))
    licznik.append([miasto[1],suma_p,liczba_lokali])


print(licznik)
print(min_lokale,max_lokale)
