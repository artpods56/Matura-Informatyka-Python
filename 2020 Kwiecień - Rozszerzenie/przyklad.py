plik = open("dane4.txt" , "r")

lista_ciagow = []
for ciag in plik:
    ciag = ciag.strip()
    lista_ciagow.append(ciag)


print(lista_ciagow)
i = 1
r_min = 1000000
r_max = 0
max_r_len = 0
end_max_r_len = 0
end_min_r_len = 0
prev_r = 0
start_r = 0
end_r = 0
try:
    for ciag in lista_ciagow:
        r = int(lista_ciagow[i]) - int(lista_ciagow[i-1])
        r = abs(r)

        print(f"{r} przy {lista_ciagow[i]} oraz {lista_ciagow[i-1]}")

        if r > r_max:
            r_max = r

        if r < r_min:
            r_min = r

        if r == prev_r:
            max_r_len += 1
 #           print(f"{r} i poprzednie {prev_r}")
        elif r != prev_r:
            if max_r_len>end_max_r_len:
                end_max_r_len = max_r_len
#                print(max_r_len)
                start_r = lista_ciagow[(i-1)-max_r_len+1]
                end_r = lista_ciagow[i-1]
            max_r_len = 0

        if max_r_len > end_max_r_len:
            end_max_r_len = max_r_len

        prev_r = r

        i += 1
except:
    pass

print(f"start: {start_r} koniec: {end_r} długość: {end_max_r_len}")