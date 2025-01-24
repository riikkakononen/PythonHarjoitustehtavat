sukupuoli = input('Anna biologinen sukupuolesi: ')
hemoglobiini = float(input('Anna hemoglobiiniarvosi: '))

if sukupuoli == 'Nainen':
    if 117 <= hemoglobiini <= 175:
        print('Hemoglobiiniarvosi on normaali.')
    elif hemoglobiini < 117 :
        print('Hemoglobiiniarvosi on alhainen.')
    else :
        print('Hemoglobiiniarvosi on korkea.')

if sukupuoli == 'Mies' :
    if 134 <= hemoglobiini <= 195:
        print('Hemoglobiiniarvosi on normaali.')
    elif hemoglobiini < 134:
        print('Hemoglobiiniarvosi on alhainen.')
    else:
        print('Hemoglobiiniarvosi on korkea.')