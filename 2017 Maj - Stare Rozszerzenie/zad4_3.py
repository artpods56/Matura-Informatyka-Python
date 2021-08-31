plik = open("binarne.txt","r")

tab = []
for linia in plik:
    linia = linia.strip()
    tab.append(linia)





def na_dziesietny(x):
    num = 0
    x = x[::-1]
    for i in range(len(x)):
        num += int(x[i])*pow(2,i)
    return num


c = 0
c_naj = 0
b_naj = ""
for liczba in tab:
    if na_dziesietny(liczba) < 65535:
        print(na_dziesietny(liczba))
        if na_dziesietny(liczba) > c_naj:
            c_naj = na_dziesietny(liczba)
            b_naj = liczba
        c += 1

print(c,c_naj,b_naj)