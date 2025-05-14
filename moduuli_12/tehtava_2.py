import requests

def hae_saa(api_key, kaupunki):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": kaupunki,
        "appid": api_key,
        "units": "metric", # Muutetaan Kelvinit Celsiuksiksi
        "lang": "fi" # Saadaan tiedot suomeksi
    }

    try:
        vastaus = requests.get(url, params=params)
        vastaus.raise_for_status()
        data = vastaus.json()

        lampotila = data["main"]["temp"]
        kuvaus = data["weather"][0]["description"]

        print(f'\nSää kohteessa {kaupunki}:')
        print(f'{kuvaus.capitalize()}, lämpötila {lampotila:.1f} °C')
    except requests.RequestException as e:
        print('Virhe API-pyynnössä.')
    except KeyError:
        print('Virheellinen paikkakunta tai datan muoto muuttunut.')

if __name__ == '__main__':
    api_avain = 'tähän oma avain'
    anna_kaupunki = input('Anna paikkakunta: ')
    hae_saa(api_avain, anna_kaupunki)