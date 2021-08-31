plik = open("binarne.txt","r")

tab = []
for linia in plik:
    linia = linia.strip()
    l = len(linia)//2
    tab.append([linia[i:i+4] for i in range(0, len(linia), 4)])




def na_dziesietny(x):
    num = 0
    x = x[::-1]
    for i in range(len(x)):
        num += int(x[i])*pow(2,i)
    return num

n = 0
n_ciag = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
dl_n_ciag = 10000
for wiersz in tab:
    ver = True
    ciag = "".join(wiersz)
    for liczba in wiersz:
        if na_dziesietny(liczba) > 9:
            ver = False
            if len(ciag) < dl_n_ciag:
                dl_n_ciag = len(ciag)
                n_ciag = ciag
            break
    if ver == False:
        n += 1

print(n,n_ciag,dl_n_ciag)

