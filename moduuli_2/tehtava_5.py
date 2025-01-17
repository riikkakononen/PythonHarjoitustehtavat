leiviskat = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

LUODIT_GR = 13.3
NAULAT_GR = 32 * LUODIT_GR
LEIVISKAT_GR = 20 * NAULAT_GR

massa_grammoina = LEIVISKAT_GR * leiviskat + NAULAT_GR * naulat + LUODIT_GR * luodit

massa_kg = massa_grammoina // 1000
grammat = massa_grammoina % 1000

print(f'Massa nykymittojen mukaan on: \n{massa_kg:2.0f} kilogrammaa ja {grammat:.2f} grammaa.')