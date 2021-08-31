def main():

    plik = open("instrukcje.txt","r")   #wczytanie pliku instrukcje.txt w trybie odczytu

    instrukcje = []                     #zdefiniowanie tablicy w której umieścimy instrukcje

    for linia in plik:                  #pętla która przechodzi przez każdą linie pliku tekstowego
        instrukcje.append(linia)        #dodajemy instrukcje do wcześniej utworzonej tabeli


    napis = ""                          #definiujemy zmienna tekstową w której będziemy przechowywać nasz napis

    def Dopisz(napis, litera):          #tworzymy funkcje "Dopisz" której zadaniem będzie dopisanie do napisu danej litery
        napis = napis + litera          #dodajemy do siebie aktualnie przechowywany napis oraz litere | "ABC" + "D" = "ABCD"
        return napis                    #zwracamy otrzymany napis

    def Zmien(napis, litera):           #tworzymy funkcje "Zmien" która zamieni ostatnią litere napisu na daną literę
        napis = list(napis)             #zamieniamy nasz napis w listę | "ABCD" ---> ["A","B","C","D"]
        napis[-1] = litera              #w miejsce ostatniej pozycji ([-1]) naszej listy wstawiamy dana litere
        napis = "".join(napis)          #zamieniamy nasza listę w napis
        return napis                    #zwracamy otrzymany napis

    def Przesun(napis,litera):          #tworzymy funkcje "Przesun" która w miejscu pierwszego wystapienia danej litery, zamieni ją na następną literę w alfabecie 
        index = napis.find(litera)      #znajdujemy index pierwszego wystąpienia naszej litery
        napis = list(napis)             #zamieniamy nasz napis w listę
        num_litera = ord(litera)        #do zmiennej "num_litera" zapisujemy wartość naszej litery w kodzie ASCII | "A" = 65, "Z" = 90
        if num_litera == 90:            #jeśli naszą literą jest "Z" (90 w kodzie ASCII) to zamiast inkrementować wartość "num_litera"                            
            num_litera = 65             #ustawiamy ją na 65 co odpowiada literze "A"
        else:                           #w przeciwnym wypadku
            num_litera += 1             #zwiekszamy wartość zmiennej "num_litera" o jeden
        litera = chr(num_litera)        #zamieniamy "num_litera" z postaci liczbowej w tekstową | 90 ---> "Z"
        napis[index] = litera           #używając wcześniej zapisanego indexu wstawiamy naszą przekształconą litere
        napis = "".join(napis)          #zamieniamy listę w napis
        return napis                    #zwracamy napis

    def Usun(napis):                    #tworzymy funckję "Usun"
        napis = list(napis)             #zamieniamy napis w listę
        napis.pop()                     #usuwamy ostatni element z naszej listy
        napis = "".join(napis)          #zamieniamy nasza listę w napis
        return napis                    #zwracamy napis



    najdl_ciag_instrukcji = 0                                   #definiujemy zmienną w której przechowywać będziemy najdłuższy ciąg instrukcji
    ciag_instrukcji = 1                                         #definiujemy zmienną w która będzie służyć jako licznik
    rodzaj_najdl_instrukcji = ""                                #definiujemy zmienną w której przechowywać będziemy rodzaj instrukcji która tworzyła najdłuższy ciąg
    poprzednia_instrukcja = ""                                  #definiujemy zmienną w której będziemy zapisywać instrukcje z ostatnie iteracji

    for instrukcja in instrukcje:                               #pętla którą będziemy iterować po wszystkich instrukcjach
        instrukcja = instrukcja.split()                         #rozdzielamy string na listę o dwóch wartościach | np: "ZMIEN B" ---> ["ZMIEN","B"]

        if instrukcja[0] == "DOPISZ":                           #jeśli instrukcja to "DOPISZ"
            napis = Dopisz(napis,instrukcja[1])                 #przekazujemy funkcji "Dopisz" nasz napis np. "ABCD" i literę np. "B" ---> funckja zwraca "ABCDB" które zapisujemy do zmiennej napis
        elif instrukcja[0] == "ZMIEN":                          #jeśli instrukcja to "ZMIEN"
            napis = Zmien(napis,instrukcja[1])                  #przekazujemy funkcji "Zmien" nasz napis np. "ABCD" i literę np. "B" ---> funkcja zwraca "ABCB" które zapisujemy do zmiennej napis
        elif instrukcja[0] == "PRZESUN":                        #jeśli instrukcja to "PRZESUN"
            napis = Przesun(napis,instrukcja[1])                #przekazujemy funkcji "Przesun" nasz napis np. "ABCD" i literę np. "C" ---> funkcja zwraca "ABDD" które zapisujemy do zmiennej napis 
        elif instrukcja[0] == "USUN":                           #jeśli instrukcja to "USUN"
            napis = Usun(napis)                                 #przekazujemy funkcji "Usun" nasz napis np. "ABCD" ---> funkcja zwraca "ABC" które zapisujemy do zmiennej

        if poprzednia_instrukcja == instrukcja[0]:              #jeśli poprzednia instrukcja jest taka sama jak bieżąca 
            ciag_instrukcji += 1                                #inkrementujemy zmienną "ciąg_instrukcji" o jeden
        elif poprzednia_instrukcja != instrukcja[0]:            #jeśli poprzednia instrukcja nie jest taka sama jak bieżąca to przerywamy liczenie
            if ciag_instrukcji > najdl_ciag_instrukcji:         #jeśli nasz licznik "ciag_instrukcji" jest wiekszy od naszej zmiennej "najdl_ciag_instrukcji" to
                najdl_ciag_instrukcji = ciag_instrukcji         #do zmiennej "najdl_ciag_instrukcji" zapisujemy nasz licznik ze zmiennej "ciag_instrukcji"
                rodzaj_najdl_instrukcji = poprzednia_instrukcja #do zmiennej "rodzaj_najdl_instrukcji" zapisujemy jaka instrukcja byla w danym ciagu
            ciag_instrukcji = 1                                 #ustawiamy zmienna "ciag_instrukcji" na 1 aby móc zacząć liczyć długość ciągu od nowa

        poprzednia_instrukcja = instrukcja[0]                   #na sam koniec do zmiennej "poprzednia_instrukcja" wrzucamy bieżącą instrukcje którą wykorzystamy w następnej iteracji
 



    licznik_liter = []                                          #definiujemy tablice "licznik_liter" | nazwa mówi sama za siebie

    for instrukcja in instrukcje:                               #iterujemy po tablicy "instrukcje"
        instrukcja = instrukcja.split()                         #rozdzielamy string na listę o dwóch wartościach | np: "ZMIEN B" ---> ["ZMIEN","B"]                      
        if instrukcja[0] == "DOPISZ":                           #jeśli instrukcja to "DOPISZ"
            if [instrukcja[1],0] not in licznik_liter:          #jeśli np. ["A",0] nie ma w liczniku liter
                licznik_liter.append([instrukcja[1],0])         #to ją do niego dodajemy | licznik po kilku iteracjach wygląda tak: [["A",0],["B",0],["C",0]]

    for instrukcja in instrukcje:                               #dokładnie to samo co zrobiliśmy z poprzednią pętlą
        instrukcja = instrukcja.split()                         # -\\-
        if instrukcja[0] == "DOPISZ":                           # -\\-
            for l in licznik_liter:                             #iterujemy po tablicy licznik_liter
                if l[0] == instrukcja[1]:                       #jeśli litera z naszej instrukcji zgadza się z literą w liczniku liter | "B" == "B"
                    l[1] += 1                                   #to inkrementujemy wartość przy danej literze w liczniku liter | ["B",0] ---> ["B",1]


    najczestsza_litera = max(l[0] for l in licznik_liter)       #szukamy najczęściej występującą litere i przypisujemy ją do zmiennej
    ilosc_wystapien_litery = max(l[1] for l in licznik_liter)   #zapisujemy także ilość jej wystąpień

    print("Zad 4.1 Całkowita długość napisu: ",len(napis))
    print("Zad 4.2 Najdłuższy ciąg występujących po sobie instrukcji tego samego rodzaju oraz jego długość: ",rodzaj_najdl_instrukcji, najdl_ciag_instrukcji)
    print("Zad 4.3 Litera która jest najczęściej dopisywana oraz ilość jej wystąpień: ", najczestsza_litera,ilosc_wystapien_litery)
    print("Zad 4.4 Napis który powstaje po wykonaniu wszystkich instrukcji: ", napis)

                                                                #wyświetlamy nasze wyniki

if __name__ == '__main__':
    main()



