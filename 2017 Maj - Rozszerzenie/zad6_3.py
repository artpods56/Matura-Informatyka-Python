plik = open("dane.txt","r")

tab = []
p_max = 0
p_min = 1000
for dane in plik:
    dane = dane.strip().split()
    dane = list(map(int,dane))
    if max(dane) > p_max:
        p_max = max(dane)
    if min(dane) < p_min:
        p_min = min(dane)
    tab.append(dane)

print(tab)

def czy_kontrast(x,y,tab):
    if x != 0:
#        print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
        if abs(tab[x][y]-tab[x-1][y]) > 128:
            print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
            return True
    if x != 199:
#        print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
        if abs(tab[x][y] - tab[x+1][y]) > 128:
            print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
            return True
    if y != 0:
#        print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
        if abs(tab[x][y] - tab[x][y-1]) > 128:
            print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
            return True
    if y != 319:
#        print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
        if abs(tab[x][y] - tab[x][y+1]) > 128:
            print(f"{tab[x][y]} dla wspolrzednych: {y} oraz {x}")
            return True
    return False






licznik = 0

for i in range(len(tab)):
    for j in range(len(tab[i])):
#       print(tab[i][j])
        if czy_kontrast(i,j,tab) == True:
            licznik += 1
print(licznik)
