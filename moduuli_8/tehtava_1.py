import mysql.connector

def hae_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for tiedot in tulos:
            print(f'Lentokentän nimi: {tiedot[0]} ja kunta, jossa se sijaitsee: {tiedot[1]}.')
    return

# Pääohjelma

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'riikka',
    password = 'koodar1',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
)

icao = input('Anna lentoaseman ICAO-koodi: ').strip().upper()
hae_tiedot(icao)