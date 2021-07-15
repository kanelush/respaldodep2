import requests
from coinpaprika import client as Coinpaprika
import time

client = Coinpaprika.Client()

a = client.tickers()

def extras(request):
    responses = a
    response = requests.get('https://static.coinpaper.io/api/coins.json').json()
    while True:
        responses
        time.sleep(15)
    context = { 
        'responses': responses,
        'response': response, 
                }
    return context


