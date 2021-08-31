file = open("punkty.txt","r")
from math import sqrt
punkty = []
for linia in file:
    linia = linia.strip()
    linia = linia.split()
    linia[0] = int(linia[0])
    linia[1] = int(linia[1])
    punkty.append(linia)

print(punkty)


granica = (5000,5000)
def position(x,y):
    if x == granica[0] and y == granica[1]:
#        print(f"punkt lezy na granicy")
        return "na boku"
    if  x == granica[0] or y == granica[1]:
#        print(f"punkt lezy na boku")
        return "na boku"
    if  x < granica[0] and y < granica[1]:
#       print(f"punkt lezy wewnatrz kwadratu")
        return "wewnatrz"
    if  x > granica[0] or y > granica[1]:
#        print(f"punkt lezy poza kwadratem")
        return "poza"



na_boku = 0
wewnatrz = 0
poza = 0
for cord in punkty:
    if position(cord[0],cord[1]) == "na boku":
        na_boku += 1
    elif position(cord[0],cord[1]) == "wewnatrz":
        wewnatrz += 1
    elif position(cord[0],cord[1]) == "poza":
        poza += 1

print(wewnatrz,na_boku,poza)
