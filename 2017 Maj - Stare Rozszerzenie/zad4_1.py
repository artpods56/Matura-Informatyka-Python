plik = open("binarne.txt","r")

tab = []
j = 0
for linia in plik:
    linia = linia.strip()
    l = len(linia)//2
    tab.append([linia[i:i+l] for i in range(0, len(linia), l)])
c = 0
dl_c_max = 0
c_max = ""
ciag = ""
for wiersz in tab:
#    print(wiersz)
    if wiersz[0] == wiersz[1]:
#        print(wiersz[0],wiersz[0])
        ciag = wiersz[0]+wiersz[1]
        if len(ciag) > dl_c_max:
            c_max = ciag
            dl_c_max = len(ciag)
        c += 1
print(c,c_max,dl_c_max)






