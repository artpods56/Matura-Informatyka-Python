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


def dl_odcinka(x1,y1,x2,y2):
    dl = sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    return dl


naj_dl = 0
dl = 0

for cord in punkty:
#    print(cord)
    for i in range(len(punkty)):
        if cord[0] != punkty[i][0] and cord[1] != punkty[i][1]:
            dl = dl_odcinka(cord[0],cord[1],punkty[i][0],punkty[i][1])
#            print(cord[0],cord[1],punkty[i][0],punkty[i][1])
        if dl > naj_dl:
            cord_x1 = cord[0]
            cord_x2 = punkty[i][0]
            cord_y1 = cord[1]
            cord_y2 = punkty[i][1]
            naj_dl = dl

print(int(naj_dl))
print(cord_x1,cord_y1, cord_x2, cord_y2)