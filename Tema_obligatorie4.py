#  1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

# for i in range(len(masini)):
#     print(f'Masina mea preferată este:', masini[i])


# for masina in masini: # for else
#     print(f'Masina mea preferata este: {masina}')

# i = 0
# x = len(masini)
# print(x)
# while i <= 9:
#     print('Masina mea preferata este:', masini[i])
#     i = i + 1


#  2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.


# for masina in masini:
#     masina.upper()
#
#     print(list(map(lambda masina: masina.upper(), masini[1:-1])))
#     break
# else:
#     print(masini)

#  3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# masina_cautata = input('Ce masina cautati?: ')
# for masina in masini:
#     masina = masina_cautata
#     if masina == 'Mercedes':
#         print(f'Am gasit masina dorita de dvstra: {masina}')
#         break
# else:
#     for masina in masini:
#         if masina == 'Mercedes':
#             continue
#         print(f'Am gasit masina {masina}. Mai cautam')


# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
           'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     if masina == 'Trabant':
#         continue
#     elif masina == 'Lastun':
#         continue
#     print(masina)

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# ● Printează Modele vechi: x.
# ● Modele noi: x.

# masini_vechi = []
# for masinax in masini:
#     if masinax == 'Trabant':
#         masini_vechi = [masinax]
#
#         break
# for masinay in masini:
#     if masinay == 'Lastun':
#         masini_vechi = [masinax] + [masinay]
#         print(masini_vechi)
#
# print(masini)
# for i in range(len(masini)):
#     if masini[i] == 'Lastun':
#         masini[i] = 'Tesla'
#     if masini[i] == 'Trabant':
#         masini[i] = 'Tesla'
#
# print(masini)

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
# for k, v in pret_masini.items():
#     if v <= buget:
#         print('Pentru un buget de sub 15.000 euro puteti alege masina:', k, v)

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar = 0
# for i in numere:
#     if i == 3:
#         numar = numar + 1
# print(numar)

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# for i in numere:
#     numar = numar + i
# print(numar)

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# max_number = None
# for i in numere:
#     if max_number is None or i > max_number:
#         max_number = i
# print(max_number)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.


# for i in numere:
#     print(-i)

# max_number = 0
# for i in numere:
#     max_number = -i
#     print(max_number)


for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)