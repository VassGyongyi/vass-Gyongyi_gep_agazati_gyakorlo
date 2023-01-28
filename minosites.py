
def ertekel():
    nev = input('Múzeum neve: ')
    latogato = input('Latogató neve: ')
    ertekeles = int(input('Értékelés (1-20): '))
    if ertekeles <= 0:
        print('Az értékelés nem lehet negatív vagy 0!')
    elif ertekeles > 20:
        print('20 pont feletti értékelés nem elfogadható!')
    else:
        print('Köszönjük az értékelést!')
