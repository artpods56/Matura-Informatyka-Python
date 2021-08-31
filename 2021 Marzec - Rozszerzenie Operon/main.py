file = open("dane.txt","r")

tablica = []
for linia in file:
    linia = int(linia.strip())
    tablica.append(linia)


lucky_tab = []

for i in range(1,10001):
    if i % 2 != 0:
        lucky_tab.append(i)

print(lucky_tab)

lucky_num = 0
i = 1
lucky_tab2 = l
