def main():

    plik = open("instrukcje.txt","r")

    instrukcje = []

    for linia in plik:
        instrukcje.append(linia)


    napis = ""   

    def Dopisz(napis, litera):
        napis = napis + litera
        return napis

    def Zmien(napis, litera):
        napis = list(napis)
        napis[-1] = litera
        napis = "".join(napis)
        return napis

    def Przesun(napis,litera):
        index = napis.find(litera)
        napis = list(napis)
        num_litera = ord(litera)
        if num_litera == 90:
            num_litera = 65
        else:
            num_litera += 1
        litera = chr(num_litera)
        napis[index] = litera
        napis = "".join(napis)
        return napis

    def Usun(napis):
        napis = list(napis)
        napis.pop()
        napis = "".join(napis)
        return napis



    najdl_ciag_instrukcji = 0
    ciag_instrukcji = 1
    rodzaj_najdl_instrukcji = ""
    poprzednia_instrukcja = ""

    for instrukcja in instrukcje:
        instrukcja = instrukcja.split()

        if instrukcja[0] == "DOPISZ":
            napis = Dopisz(napis,instrukcja[1])
        elif instrukcja[0] == "ZMIEN":
            napis = Zmien(napis,instrukcja[1])
        elif instrukcja[0] == "PRZESUN":
            napis = Przesun(napis,instrukcja[1])
        elif instrukcja[0] == "USUN":
            napis = Usun(napis)

        if poprzednia_instrukcja == instrukcja[0]:
            ciag_instrukcji += 1
        elif poprzednia_instrukcja != instrukcja[0]:
            if ciag_instrukcji > najdl_ciag_instrukcji:
                najdl_ciag_instrukcji = ciag_instrukcji
                rodzaj_najdl_instrukcji = poprzednia_instrukcja
            ciag_instrukcji = 1

        poprzednia_instrukcja = instrukcja[0]
 



    licznik_liter = []

    for instrukcja in instrukcje:
        instrukcja = instrukcja.split()
        if instrukcja[0] == "DOPISZ":
            if [instrukcja[1],0] not in licznik_liter:
                licznik_liter.append([instrukcja[1],0])

    for instrukcja in instrukcje:
        instrukcja = instrukcja.split()
        if instrukcja[0] == "DOPISZ":
            for l in licznik_liter:
                if l[0] == instrukcja[1]:
                    l[1] += 1


    najczestsza_litera = max(l[0] for l in licznik_liter)
    ilosc_wystapien_litery = max(l[1] for l in licznik_liter)

    print("Zad 4.1 Całkowita długość napisu: ",len(napis))
    print("Zad 4.2 Najdłuższy ciąg występujących po sobie instrukcji tego samego rodzaju oraz jego długość: ",rodzaj_najdl_instrukcji, najdl_ciag_instrukcji)
    print("Zad 4.3 Litera która jest najczęściej dopisywana oraz ilość jej wystąpień: ", najczestsza_litera,ilosc_wystapien_litery)
    print("Zad 4.4 Napis który powstaje po wykonaniu wszystkich instrukcji: ", napis)


if __name__ == '__main__':
    main()



