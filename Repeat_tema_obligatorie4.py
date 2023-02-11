# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
          'Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     print(f'Masina mea preferata este: {masina}' # for each

# for i in range(len(masini)):
#     print(f'Masina mea preferata este: {masini[i]}') # for


# i = 0
#
# while i < len(masini):
#
#     print(masini[i])
#
#     i = i+1

# 2 Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

# for i in range(len(masini)):
#     masini[i] = masini[i].upper()
# del masini[0]
# del masini[-1]
# print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

m = input('ce masina doriti: ')
for masina in masini:
    if masina == m:
        print('am gasit masina dorita')
    else:
        if masina == 'Mercedes':

            continue

        print(f' Am gasit masina {masina}')