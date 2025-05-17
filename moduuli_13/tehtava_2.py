from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Luodaan tietokantayhteys

yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'riikka',
    password = 'koodar1',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
)

def hae_tiedot(icao):
    kursori = yhteys.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    kursori.close()

    if tulos:
        return {
            "ICAO": icao,
            "Name": tulos[0],
            "Municipality": tulos[1]
        }
    else:
        return None


# Flask-reitti
@app.route("/kenttä/<icao>", methods=["GET"])
def kenttä(icao):
    tiedot = hae_tiedot(icao.upper())
    if tiedot:
        return jsonify(tiedot)
    else:
        return jsonify({"error": "Lentokenttää ei löydy"}), 404

if __name__ == "__main__":
    app.run(port=3000)