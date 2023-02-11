# lista = [1, 2, 3, 4, True]
# for i in lista:
#     print(i)
#
# for i in range(len(lista)):
#     print(i, lista[i])
#
# for i in lista:
#     if isinstance(i, int):
#           print(i)

lista = ['name', 2, 3, 4, True, dict(name = 'john'), set(), 5, {'key1' : 1, 'key2' : 2, 'key3' : 3}]
# for i in lista:
#     if isinstance(i, str):
#         print(i)
#     elif isinstance(i, int):
#         print(i)
#     elif isinstance(i, dict):
#         print(i)
#     else:
#        print('print other')

# for i, v in enumerate (lista):
#     print(i, v)
#     print(lista[i])

# for i in range (len(lista)):
#     print(lista[i])

for i in range (len(lista)):
    if isinstance(lista[i], dict):
        for k, v in lista[i].items():
            if k == 'key3' and v == 3:
                print(k, v)

# for i in range(100, 1, -1):
#     print(i)
# TODO declaram o lista ce contine doar numere si vrem sa facem suma tuturor elementelor din lista prin 4 metode (for cu while cu count etc)
# TODO sa gasim duplicatele dintr-o lista ion john petre pop si iarasi ion , ne gaseste elementele care sunt de mai multe ori - ne afiseaza doar pe Ion (loop )
tema_lista = ['ion', 'ion', 'mihai', 'mihai', 'radu']
# TODO o lista cu diverse numer sa obtinem cel mai mare numar par