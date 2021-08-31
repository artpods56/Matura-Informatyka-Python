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

print(p_max,p_min)
#print(*tab,sep="\n")


min_rmv = 0

for line in tab:
    j = -1
    for i in range(len(line)//2):
#        print(line[i],line[j])
        if line[i] != line[j]:
            min_rmv += 1
            break

        j -= 1

print(min_rmv)