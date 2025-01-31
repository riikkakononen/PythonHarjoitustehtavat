# Luodaan tyhjä lista kaupunkien tallentamista varten
kaupungit = []

# Kysytään käyttäjältä viisi kaupungin nimeä
print('Anna viiden kaupungin nimet.')
for i in range(5):
    kaupunki = input(f'Anna {i+1}. kaupungin nimi: ')
    kaupungit.append(kaupunki)

# Tulostetaan kaupungit allekkain
print('\nSyöttämäsi kaupungit:')
for kaupunki in kaupungit:
    print(kaupunki)