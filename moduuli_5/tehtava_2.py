# Lista luvuista

numerot = []

# Kysytään käyttäjältä lukuja kunnes syötetään tyhjä merkkijono
while True:
    syote = input('Syötä luku (tai paina Enter lopettaaksesi): ')

    # Jos syöte on tyhjä, lopetetaan syöttö
    if syote == '':
        break

    # Yritetään muuntaa syöte luvuksi

    try:
        numero = float(syote)
        numerot.append(numero)
    except ValueError:
        print('Syötä kelvollinen luku!')

# Lajitellaan numerot suuruusjärjestykseen (suurimmat ensin)
numerot.sort(reverse=True)

# Tulostetaan viisi suurinta lukua
print('Viisi suurinta lukua suurimmasta alkaen: ')
for num in numerot[:5]:
    print(num)