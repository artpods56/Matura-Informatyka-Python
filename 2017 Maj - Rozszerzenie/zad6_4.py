plik = open("dane.txt","r")

tab = []

for dane in plik:
    dane = dane.strip().split()
    dane = list(map(int,dane))

    tab.append(dane)

print(tab)
c = 0
c_max = 0
for i in range(320):
    for j in range(1,200):
        if tab[j][i] == tab[j-1][i]:
            c+=1
        elif tab[j][i] != tab[j-1][i]:
            if c > c_max:
                c_max = c + 1
            c = 0
    if c > c_max:
        c_max = c + 1
    c = 0

print(c_max)
