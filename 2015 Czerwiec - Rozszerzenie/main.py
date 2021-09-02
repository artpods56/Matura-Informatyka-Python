def main():

    plik1 = open("cyfra_kodkreskowy.txt","r")
    plik2 = open("kody.txt","r")

    kody = []
    cyfry_kodow = {}

    for row in plik1:
        row = row.strip().split()
        if row != ['Cyfra', 'Kod', 'kreskowy']:
            cyfry_kodow[row[0]] = row[1]

    for row in plik2:
        row = row.strip()
        kody.append(row)


    plik_kody1 = open("kody1.txt","w")
    plik_kody1.truncate()

    for liczba in kody:
        suma_n = 0
        suma_p = 0
        for cyfra in liczba:
            if int(cyfra)%2 != 0:
                suma_n += int(cyfra)
            elif int(cyfra)%2 == 0:
                suma_p += int(cyfra)
        plik_kody1.write(f"{suma_n} {suma_p} {liczba} \n")


    def kontrolna(num):
        suma_n = 0
        suma_p = 0
        suma = 0
        for i in num:
            if int(i)%2 != 0:
                suma_n += int(i)
            elif int(i)%2 == 0:
                suma_p += int(i)
        suma_p*=3
        suma = suma_p + suma_n
        r = suma%10
        mod = 10 - r
        r = mod%10
        return r

    plik_kody2 = open("kody2.txt","w")
    plik_kody2.truncate()
    for liczba in kody:
        plik_kody2.write(f"{kontrolna(liczba)} {cyfry_kodow[str(kontrolna(liczba))]} \n")



    plik_kody3 = open("kody3.txt","w")
    plik_kody3.truncate()
    for liczba in kody:
        kod = "11011010"
        for l in liczba:
            kod += cyfry_kodow[str(l)]
        kod += cyfry_kodow[str(kontrolna(liczba))]
        kod += "11010110"
        plik_kody3.write(f"{kod} \n")

if __name__ == '__main__':
    main()
