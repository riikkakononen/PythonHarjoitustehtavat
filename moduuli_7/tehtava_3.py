# Luodaan sanakirja lentokentille

lentokentät = {}

while True:
    print('\nValitse toiminto: ')
    print('1 - Lisää uusi lentokenttä')
    print('2 - Hae lentokentän nimi ICAO-koodilla')
    print('3 - Lopeta')

    valinta = input('Anna valinta: ').strip()
    if valinta == '1':
        icao = input('Anna lentokentän ICAO-koodi: ').strip().upper()
        nimi = input('Anna lentokentän nimi: ').strip()
        lentokentät[icao] = nimi

        print(f'Lentokenttä {nimi} (ICAO: {icao}) lisätty: ')

    elif valinta == '2':
        icao = input('Anna ICAO-koodi: ').strip().upper()
        if icao in lentokentät:
            print(f'Lentokenttä: {lentokentät[icao]}')
        else:
            print('Lentokenttää ei löytynyt')

    elif valinta == '3':
        print('Ohjelma päättyy.')
        break
    else: print('Virheellinen valinta, yritä uudelleen.')