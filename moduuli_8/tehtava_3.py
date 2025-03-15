import mysql.connector
import geopy
from geopy.distance import geodesic


def hae_tiedot(icao):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s'
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    return tulos # Palauttaa latitude, longitude tai None jos kenttää ei löydy

def laske_etäisyys(icao1, icao2):
    koord1 = hae_tiedot(icao1)
    koord2 = hae_tiedot(icao2)
    etäisyys = geodesic(koord1, koord2).kilometers
    print(f'\nLentokenttien {icao1} ja {icao2} välinen eitäisyys on {etäisyys:.2f} km.')




yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'riikka',
    password = 'koodar1',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
)

icao1 = input('Anna ensimmäisen lentokentän ICAO-koodi: ').strip().upper()
icao2 = input('Anna toisen lentokentän ICAO-koodi: ').strip().upper()

laske_etäisyys(icao1, icao2)