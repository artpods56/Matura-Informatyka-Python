file = open("punkty.txt","r")
punkty = []
for linia in file:
    linia = linia.strip()
    linia = linia.split()
    linia[0] = int(linia[0])
    linia[1] = int(linia[1])
    punkty.append(linia)


print(punkty)

def czy_podobne(x,y):
    x_num = []
    y_num = []
    for i in range(len(str(x))):
        if x[i] not in x_num:
            x_num.append(x[i])
    for i in range(len(str(y))):
        if y[i] not in y_num:
            y_num.append(y[i])
    for i in range(len(x_num)):
        if x_num[i] not in y_num:
            return False
    for i in range(len(y_num)):
        if y_num[i] not in x_num:
            return False
    return True

for cord in punkty:
    if czy_podobne(str(cord[0]),str(cord[1])) == True:
        print(f"{cord[0]} oraz {cord[1]} sa cyfropodobne")