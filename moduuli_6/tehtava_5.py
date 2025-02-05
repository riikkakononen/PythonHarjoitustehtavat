def parilliset_luvut(numerot):
    return [luku for luku in numerot if luku % 2 == 0]

numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parilliset = parilliset_luvut(numerot)

print('Alkuperäinen lista:', numerot)
print('Karsittu lista:', parilliset)