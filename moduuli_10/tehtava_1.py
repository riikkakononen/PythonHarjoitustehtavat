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
        print(f'Siirrytään kerrokseen {kohde_kerros}.')
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

# Pääohjelma

if __name__ == '__main__':
    h = Hissi(1,10)
    h.siirry_kerrokseen(7)
    h.siirry_kerrokseen(1)