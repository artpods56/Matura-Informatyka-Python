plik = open("liczby.txt","r")

nums = []

for liczba in plik:
    liczba = liczba.strip()
    nums.append(liczba)

def dziesietny(b):
    ver = "nie"
    zera = 0
    jedynki = 0
    b = b[::-1]
    d = 0
    for i in range(len(b)):
        d += int(b[i])*pow(2,i)
        if b[i] == "1":
            jedynki += 1
        elif b[i] == "0":
            zera += 1
    if zera > jedynki:
        ver = "tak"
    return d, ver


c = 0
podzielne2 = 0
podzielne8 = 0
max = 0
max_nr = 0
min_nr = 0
min = 10000000000000000000000000000000000000000000000000000
nr_rzedu = 0
for num in nums:
    nr_rzedu += 1
    if dziesietny(num)[1] == "tak":
        c += 1
    if dziesietny(num)[0]%2 == 0:
        podzielne2 += 1
    if dziesietny(num)[0]%8 == 0:
        podzielne8 += 1
    if dziesietny(num)[0] > max:
        max = dziesietny(num)[0]
        max_nr = nr_rzedu
    if dziesietny(num)[0] < min:
        min = dziesietny(num)[0]
        min_nr = nr_rzedu


print("zad1")
print(c)
print("\n")

print("zad2")
print(podzielne2)
print(podzielne8)
print("\n")

print("zad3")
print(max,max_nr)
print(min,min_nr)
