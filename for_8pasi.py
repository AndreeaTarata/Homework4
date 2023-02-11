# # 101 dalmatieni
# i = 0
# for i in range(0,101):
#     i = i + 1
#  #   print(f'Dalmatianul cu nr {i}')
#
#
#
# numere = [3, 7, 10, 20, 30]
#
# for i in range(0, len(numere)):
#     print(i)
#     print(numere[i])


def suma(numere):
    s = 0
    for numar in (numere):
        s = s + numar
    return s
numere = [3, 7, 10, 20, 30]
print(suma(numere))

def numaratoare(lista, numarul):
    count = 0
    for numar in lista:
        if numar == numarul:
            count += 1
    return count

lista = [3, 5, 3, 4]
numarul = 3
print(numaratoare(lista, numarul))