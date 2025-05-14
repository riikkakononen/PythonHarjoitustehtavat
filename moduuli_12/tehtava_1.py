import requests

def hae_chuck_norris_vitsi():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        vastaus = requests.get(url)
        vastaus.raise_for_status()
        data = vastaus.json()
        print('\nChuck Norris -vitsi:')
        print(data['value'])
    except requests.RequestException as e:
        print('Virhe API-pyynnössä:', e)

if __name__ == "__main__":
    hae_chuck_norris_vitsi()