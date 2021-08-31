kody = open("cyfra_kodkreskowy.txt","r")
liczby = open("kody.txt","r")
nums = []
tab = []

for row in liczby:
    row = row.strip()
    nums.append(row)

for row in kody:
    row = row.strip().split()
    tab.append(row)
start = "11011010"
stop = "1010110"
codes = []

for num in nums:
    suma_n = 0
    suma_p = 0
    for i in range(len(num)):
        if (i+1)%2 != 0:
            suma_n += int(num[i])
        elif (i+1)%2 == 0:
            suma_p += int(num[i])
    print(suma_n, suma_p, num)


print("################")

def kontrolna(num):
    suma_n = 0
    suma_p = 0
    suma = 0
    for i in range(len(num)):
        if (i+1)%2 != 0:
            suma_n += int(num[i])
        elif (i+1)%2 == 0:
            suma_p += int(num[i])
    suma_p*=3
    suma = suma_p + suma_n
    r = suma%10
    mod = 10 - r
    r = mod%10
    return r

kontrolna("764321")

codes = {
    "1":"11101010101110",
    "2":"10111010101110",
    "3":"11101110101010",
    "4":"10101110101110",
    "6":"10111011101010",
    "7":"10101011101110"
}

def code(num):
    for key in codes:
        if key == num:
            return codes[num]


for num in nums:
    kod = "11011010"
    control_num = kontrolna(num)
    for l in num:
        kod += code(l)
    kod += code(str(control_num))
    kod += "11010110"
    print(kod)



