file = open("gra.txt", "r")
table = []

import os

for wiersz in file:
    wiersz = wiersz.strip()
    row = []
    for letter in wiersz:
        row.append(letter)
    table.append(row)



def ile_sasiadow(x, y, table):
    status = ""
    if table[y][x] == "X":
        status = "alive"
    elif table[y][x] == ".":
        status = "dead"
    sasiedzi = 0
    for j in range(y - 1, y + 2):
        word = ""
        for i in range(x - 1, x + 2):
            if i == 20 and j == 12:
                word += table[0][0]
                continue
            if i == 20:
                word += table[j][0]
                continue
            if j == 12:
                word += table[0][i]
                continue

            if i != x or j != y:
                word += table[j][i]
        # print(word)
        for letter in word:
            if letter == "X":
                sasiedzi += 1
    return sasiedzi, status


def evolve(table):
    pass
    evolution = []
    for i in range(len(table)):
        evo_row = []
        for j in range(len(table[0])):
            # print(table[i][j])
            if ile_sasiadow(j, i, table)[1] == "alive" and ile_sasiadow(j, i, table)[0] in (2, 3):
                evo_row.append("X")
                continue
            elif ile_sasiadow(j, i, table)[1] == "dead" and ile_sasiadow(j, i, table)[0] == 3:
                evo_row.append("X")
                continue
            else:
                evo_row.append(".")
        evolution.append(evo_row)

    return evolution


for i in range(2, 100):
    print("Pokolenie", i)
    table = evolve(table)
    for row in table:
        print(row)
    clear_screen()

import sys, pygame

size = width, height = 401,401
black = 0,0,0
white = 200,200,200

screen = pygame.display.set_mode(size)
block_size = 2
gameLoop = True
tab = [["" for i in range(20)] for j in range(20)]
for x in tab:
    print(x)
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    j = 1
    for y in tab:
        i = 1
        for x in y:
            pygame.draw.rect(screen, white, [i, j, 19, 19])
            i += 20
        j +=20
    pygame.display.flip()


