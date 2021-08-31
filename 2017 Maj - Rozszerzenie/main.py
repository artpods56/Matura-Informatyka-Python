
file = open("przyklad.txt", "r").read().split('\n')
min = 0
for line in file:
    if len(line.split(" ")) < 2 or len(line.split(" ")[1]) < 1:
        continue
    points = line.split(" ")
    for i in range(320):
        print(points[i],points[319 - i])
        if points[i] != points[319 - i]:
            min += 1
            break
print("Min do usunięcia: " + str(min))