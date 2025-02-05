# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten
# pääohjelma, jossa luot listan, kutsut funktioita ja tulostat sen palauttaman summan.


def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa


luvut = (3,7,12,4,6)

summa = laske_summa(luvut)

print('Summa on ' + str(summa))