def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    return a


file = open("przyklad.txt", "r")
lines = file.read().splitlines()
file.close()

print(lines)
pom = []
dzielnik = int(lines[0])
pierwszaMax = 0
dlugoscMax = 0
dzielnikMax = 1

for i in range(1, 500):
    num = int(lines[i])
    nwd = NWD(dzielnik, num)
    if nwd != 1:
        if len(pom) == 0: #sprawdzamy najpierw czy pomocniczy zbior liczb jest pusty (co oznaczałoby, ze w n jest przechowana liczba, a nie dzielnik)
            pom.append(dzielnik) #jezeli tak to od razu dodajemy ta liczbe do zbioru (aby jej nie pominac)
        pom.append(num) #nastepnie dodajemy liczbe z aktualnego wiersza
        dzielnik = nwd #i przypisujemy za n nowy dzielnik
        print(pom)
    else:
        if len(pom) > dlugoscMax:#w przeciwnym wypadku sprawdzamy czy pomocniczy zbior jest dluzszy, niz przechowana dlugosc
            dlugoscMax = len(pom) #jezeli tak to zapisujemy jego dlugosc
            dzielnikMax = dzielnik #dzielnik
            pierwszaMax = pom[0] #oraz pierwszy wyraz
        if len(pom) != 0: #jezeli zas pomocniczy zbior nie jest pusty (co oznacza, że wlasnie znalezlismy koniec ciagu)
            if NWD(pom[len(pom)-1], num) > 1: #musimy sprawdzic ostatni wyraz i pierwszy nastepnego ciagu
                a = pom[len(pom)-1] #jezeli liczby maja wspolny dzielnik
                pom.clear() #czyscimy zbior pomocniczy
                pom.append(a) #a nastepnie dodajemy do niego od razu dwie liczby
                pom.append(num) #ktore spelniaja warunki zadania
            else:
                pom.clear() #w innym razie po prostu czyscimy zbior pomocniczy
        dzielnik = num #na koniec za dzielnik przypisujemy aktualna liczbe (aby na poczatku petli mozna bylo policzyc nowy NWD)


print("Pierwsza liczba z ciagu: " + str(pierwszaMax) + ", dzielnik " + str(dzielnikMax) + ", dlugosc ciagu: " + str(dlugoscMax))