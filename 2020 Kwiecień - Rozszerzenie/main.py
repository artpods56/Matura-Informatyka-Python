def main():
    plik = open("dane4.txt","r")
    ciagi = []
    luki = []
    for ciag in plik:
        ciag = ciag.strip()
        ciagi.append(ciag)


    for i in range(1,len(ciagi)):
        r = int(ciagi[i])-int(ciagi[i-1])
        r = abs(r)
        luki.append(r)

    
    max_luka = 0
    min_luka = 100
    dl_luki = 1
    naj_dl_luki = 0
    start_luki = 0
    end_luki = 0
    for i in range(1,len(luki)):

        if luki[i-1] > max_luka:
            max_luka = luki[i-1]
        if luki[i-1] < min_luka:
            min_luka = luki[i-1]

        if luki[i] == luki[i-1]:
            dl_luki += 1

        if luki[i] != luki[i-1] or luki[i] == luki[-1] :

            if dl_luki > naj_dl_luki:
                end_luki = ciagi[i]
                start_luki = ciagi[i-dl_luki]
                naj_dl_luki = dl_luki+1
            dl_luki = 1
        i += 1 

        r_occurances = max(luki, key=luki.count)
        r_count = luki.count(r_occurances)


    plik4_1 = open("wynik4_1.txt","w")
    plik4_1.truncate()


    plik4_1.write(f"Zadanie 4.1 \nnajdłuższa luka: {max_luka} \n najkrótsza luka {min_luka}\n")
    plik4_1.write(f"Zadanie 4.2 \nnajdłuższy ciąg regularny: {naj_dl_luki} \npoczątek: {start_luki}\nkoniec luki: {end_luki}\n")
    plik4_1.write(f"Zadanie 4.3 \nnajczęstsza wartość luki: {r_occurances}\nnajczęstsza krotność luki: {r_count}")


if __name__ == "__main__":
    main()