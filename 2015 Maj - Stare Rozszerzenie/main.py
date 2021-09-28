
def main():
    plik = open("slowa.txt","r")
    
    def czyWiecejZer(slowo):
        jedynki = slowo.count("1")
        zera = slowo.count("0")
        if zera > jedynki:
            return True
        else:
            return False

    def czyDwaNiepusteZbiory(slowo):
        lista = []
        temp = slowo[0]
        for i in range(1,len(slowo)):
            if slowo[i] == slowo[i-1]:
                temp += slowo[i]
            else:
                lista.append(temp)
                temp = slowo[i]
            if i == len(slowo)-1:
                lista.append(temp)

        if len(lista) == 2:
            if "1" not in lista[0] and "0" not in lista[1]:
                return True
            else:
                return False
        else:
            return False



    def najdlBlokZer(slowo):
        lista = []
        temp = slowo[0]
        for i in range(1,len(slowo)):
            if slowo[i] == slowo[i-1]:
                temp += slowo[i]
            else:
                lista.append(temp)
                temp = slowo[i]
            if i == len(slowo)-1:
                lista.append(temp)

        for blok in lista:
            if "1" in blok:
                lista.remove(blok)
        if len(lista) != 0:
            najdl_blok = max(lista,key=len)
            return najdl_blok
        return "0"

    licznik4_1 = 0
    licznik4_2 = 0    
    maxnajdlblok = ""
    lista2 = []
    for linia in plik:
        linia = linia.strip()
        lista2.append(linia)
        ### Zad 4.1 ###
        if czyWiecejZer(linia) == True:
            licznik4_1 += 1

        ### Zad 4.2 ###
        if czyDwaNiepusteZbiory(linia) == True:
            licznik4_2 += 1

        ### Zad 4.3 ###
        najdlblok = najdlBlokZer(linia)
        if len(najdlblok) > len(maxnajdlblok):
            maxnajdlblok = najdlblok

    lista4_3 = []
    for linia in lista2:
        if maxnajdlblok == najdlBlokZer(linia):
            tablica.append(linia)

    ### odpowiedzi ###
    print(licznik4_1,licznik4_2,lista4_3)
if __name__ == '__main__':
    main()