# Kysytään käyttäjältä kokonaisluku
kokonaisluku = int(input('Syötä kokonaisluku: '))

# Tarkistetaan onko luku pienempi tai yhtä suuri kuin 1 (alkuluku on suurempi kuin 1)

if kokonaisluku <= 1:
    print(f'{kokonaisluku} ei ole alkuluku.')
else:
    # Tarkistetaan, onko luku jaollinen jollain muulla luvulla kuin 1 ja itsellään
    is_prime = True
    for i in range(2,int(kokonaisluku ** 0.5) + 1):   # Käytetään neliöjuurta optimointiin
        if kokonaisluku % i == 0:
            is_prime = False
            break

    # Tulostetaan tulos
    if is_prime:
        print(f'{kokonaisluku} on alkuluku.')
    else:
        print(f'{kokonaisluku} ei ole alkuluku.')