# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
import random

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
# print(numere_pare)
#
# for i in alte_numere:

#     if i % 2 != 0:
#         numere_impare.append(i)
# print(numere_impare)
#
# for i in alte_numere:
#     if i > 0:
#         numere_pozitive.append(i)
# print(numere_pozitive)
#
# for i in alte_numere:
#     if i < 0:
#         numere_negative.append(i)
# print(numere_negative)

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.

# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#         print(i, j)
#
#
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
#
# print(alte_numere)

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

# numar_secret = random.randint(0,30)
#
# numar_ghicit = input('Introduceti un numar: ')
# print(numar_secret)
# print(numar_ghicit)
#
# while numar_ghicit != numar_secret:
#     if int(numar_ghicit) < int(numar_secret):
#         print('Nr secret e mai mare')
#     else:
#         print('Nr secret e mai mic')
#     break
#
# else:
#     print('Felicitari! Ati ghicit!')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

# numar_tastat = int(input('Numar: '))
# randuri = numar_tastat
# for i in range(randuri+1):
#     for j in range(i):
#         print(i, end='')
#     print('')

# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for numar in tastatura_telefon:
    print(numar)
    for i in range(len(numar)):

        for numar_dorit in numar:
            print(f'Cifra curenta este: {numar_dorit}')
        break
