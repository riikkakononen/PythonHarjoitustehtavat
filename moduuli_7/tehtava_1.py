# Määritellään vuodenajat

vuodenajat = {
    "talvi": (12, 1, 2),
    "kevät": (3, 4, 5),
    "kesä": (6, 7, 8),
    "syksy": (9, 10, 11),
}

# Kysytään kuukauden numero

kuukausi = int(input('Anna kuukauden numero: '))

# Etsitään vuodenajan nimi

for vuodenaika, kuukaudet in vuodenajat.items():
    if kuukausi in kuukaudet:
        print(f'Kuukausi {kuukausi} kuuluu vuodenaikaan {vuodenaika}.')
        break

