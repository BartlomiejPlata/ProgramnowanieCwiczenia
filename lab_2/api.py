import requests

zmienna = request.get('https://api.openbrewerydb.org/breweries')

if (zmienna.status_code != requests.codes.ok):
    print("coś poszło nie tak")
else:
    print(zmienna.json())