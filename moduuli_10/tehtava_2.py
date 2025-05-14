class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi nousi kerrokseen {self.nykyinen_kerros}.')
        else:
            print('Hissi on ylimmässä kerroksessa.')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'Hissi laski kerrokseen {self.nykyinen_kerros}')
        else:
            print('Hissi on alimmassa kerroksessa.')

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range (hissien_lkm):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f'\nAjetaan hissiä {hissin_numero + 1} kerrokseen {kohde_kerros}.')
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else: print('Virheellinen hissin numero.')

# Pääohjelma

if __name__ == '__main__':
    talo = Talo(1,15,3)

    talo.aja_hissiä(0,5)
    talo.aja_hissiä(1,9)
    talo.aja_hissiä(2,14)

    talo.aja_hissiä(1,1)