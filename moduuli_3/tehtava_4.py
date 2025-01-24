vuosiluku = int(input('Anna vuosiluku: '))

if vuosiluku % 4 == 0 and not vuosiluku % 100 == 0:
    print('Vuosi on karkausvuosi.')
elif vuosiluku % 400 == 0:
    print('Vuosi on karkausvuosi.')