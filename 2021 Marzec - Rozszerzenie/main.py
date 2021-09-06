def main():
    plik = open("galerie.txt","r")
    dane = []
    for linia in plik:
        linia = linia.strip()
        linia = linia.split()
        dane.append(linia)

    liczba_miast = []

    for kraj in dane:
        if [kraj[0],0] not in liczba_miast:
            liczba_miast.append([kraj[0],0])

    for kraj in dane:
        for miasto in liczba_miast:
            if kraj[0] == miasto[0]:
                miasto[1] += 1


    miasto_powierzchnia_lokale = []

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
        if len(pola_lokali) > max_lokale[1]:
            max_lokale[0] = miasto[1]
            max_lokale[1] = len(pola_lokali)
        if len(pola_lokali) < min_lokale[1]:
            min_lokale[0] = miasto[1]
            min_lokale[1] = len(pola_lokali)
        miasto_powierzchnia_lokale.append([miasto[1],suma_p,liczba_lokali])


    plik4_1 = open("wynik4_1.txt","w")
    plik4_1.truncate()
    for miasto in liczba_miast:
        plik4_1.write(f"{miasto} \n")

    plik4_2a = open("wynik4_2a.txt","w")
    plik4_2a.truncate()
    for miasto in miasto_powierzchnia_lokale:
        plik4_2a.write(f"{miasto} \n")

    plik4_2b = open("wynik4_2b.txt","w")
    plik4_2b.truncate()
    plik4_2b.write(f"Miasto o najmniejszej powierzchni całkowitej lokali: {min} \nMiasto o największej powierzchni całkowitej lokali: {max}")

    plik4_3 = open("wynik4_3.txt","w")
    plik4_3.truncate()
    plik4_3.write(f"Miasto o największej ilości różnych lokali: {max_lokale} \nMiasto o najmnijeszej ilości różnych lokali: {min_lokale}")
    print("gowno")
if __name__ == "__main__":
    main()