import math

def laske_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala_m2 = math.pi * (sade / 100) ** 2
    return hinta / pinta_ala_m2

print('Anna ensimmäisen pizzan tiedot:')
halkaisija1 = float(input('Halkaisija (cm): '))
hinta1 = float(input('Hinta (€): '))

print('\nAnna toisen pizzan tiedot: ')
halkaisija2 = float(input('Halkaisija (cm): '))
hinta2 = float(input('Hinta (€): '))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2,hinta2)

print(f'\nEnsimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²')
print(f'Toisen pizzan yksikköhinta: {yksikkohinta2: .2f} €/m²')

if yksikkohinta1 < yksikkohinta2:
    print('Ensimmäinen pizza tarjoaa paremman vastineen rahalle.')
elif yksikkohinta1 > yksikkohinta2:
    print('Toinen pizza tarjoaa paremman vastineen rahalle.')
else:
    print('Molemmat pizzat ovat yhtä kannattavia.')