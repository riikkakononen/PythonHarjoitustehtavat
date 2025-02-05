# Tämä funktio muuntaa gallonat litroiksi.
def bensiinin_maara(nestegallonat):
    return nestegallonat * 3.785

while True:
    # Pyydetään käyttäjältä gallonamäärä.
    gallonat = float(input('Anna bensiinin määrä Yhdysvaltain nestegallonoina: '))

    # Jos syöte on negatiivinen, lopetetaan ohjelma.
    if gallonat < 0:
        break

    # Lasketaan gallonamäärä litroina ja tulostetaan tulos.
    bensiini = bensiinin_maara(gallonat)
    print('Bensiinin määrä litroina on: ' + str(bensiini) + '.')