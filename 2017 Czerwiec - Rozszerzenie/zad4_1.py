file = open("punkty.txt","r")
punkty = []
for linia in file:
    linia = linia.strip()
    linia = linia.split()
    linia[0] = int(linia[0])
    linia[1] = int(linia[1])
    punkty.append(linia)


print(punkty)

def czy_pierwsza(num):
    i = 2
    if num < 2:
        return False
    while i*i <= num:
        if num%i==0:
            return False
        i += 1
    return True


i = 0
for cord in punkty:
    if czy_pierwsza(int(cord[0])) == True and czy_pierwsza(int(cord[1])) == True:
        print("liczby sa pierwsze")
        print(cord[0],cord[1])
        i += 1

print(i)


