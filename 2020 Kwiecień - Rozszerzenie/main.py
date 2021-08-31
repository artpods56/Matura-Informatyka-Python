plik = open("dane4.txt","r")
ciagi = []
luki = []
for ciag in plik:
    ciag = ciag.strip()
    ciagi.append(ciag)
#utworzenie tablicy ciagi

try:
    i = 1
    while i <= len(ciagi):
        r = int(ciagi[i])-int(ciagi[i-1])
        r = abs(r)
        luki.append(r)
#        print(f"luka: {r} miedzy: {ciagi[i]} oraz: {ciagi[i-1]}")
        i += 1
except IndexError:
    pass
#utworzenie tablicy luk

try:
    i = 1
    max_luka = 0
    min_luka = 100
    dl_luki = 1
    naj_dl_luki = 0
    start_luki = 0
    end_luki = 0
    while i <= len(ciagi):
#        print(f"luka: {luki[i-1]}  miedzy: {ciagi[i-1]} oraz: {ciagi[i]}")

#       najdluzsza i najkrotsza luka ciagow
        if luki[i-1] > max_luka:
            max_luka = luki[i-1]
        if luki[i-1] < min_luka:
            min_luka = luki[i-1]

        if luki[i] == luki[i-1]:
            dl_luki += 1

        if luki[i] != luki[i-1] or luki[i] == luki[-1] :
#           print(f' koniec i start: {ciagi[i]} {ciagi[i - dl_luki]}')
            if dl_luki > naj_dl_luki:
                end_luki = ciagi[i]
                start_luki = ciagi[i-dl_luki]
                naj_dl_luki = dl_luki+1


            dl_luki = 1

        i += 1 #inkrementacja o +1

        r_occurances = max(luki, key=luki.count)
        r_count = luki.count(r_occurances)

except IndexError:
    pass
print("\nZadanie 4.1")
print(f"najdluzsza luka: {max_luka}")
print(f"najkrotsza luka: {min_luka}")

print("\nZadanie 4.2")
print(f"najdluzszy ciag regularny: {naj_dl_luki}")
print(f"poczatek: {start_luki} koniec: {end_luki}")

print("\nZadanie 4.3")
print(f"najczestsza wartosc luki: {r_occurances}")
print(f"najczestsza krotność luki: {r_count}")
