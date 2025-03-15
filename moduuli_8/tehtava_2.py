import mysql.connector

def hae_tiedot(maakoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()

    for tyyppi, määrä in tulos:
        print(f'\n- {tyyppi}: {määrä} kpl')

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'riikka',
    password = 'koodar1',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
)

# Pääohjelma

maakoodi = input('Anna maakoodi: ').strip().upper()
hae_tiedot(maakoodi)
