from datetime import datetime
import pandas as pd
import requests


BASE_URL = "https://api.coingecko.com/api/v3/"

def get_coin_market_chart(token_name):
    url = BASE_URL+"coins/{}/market_chart?vs_currency=usd&days=max&interval=daily".format(token_name)
    resp = requests.get(url)
    if resp.status_code == 200:
        result = resp.json()
    else:
        print('Request Error: {}: invalid token name'.format(resp.status_code))
        result = {}
    return result

def get_coin_market_cap(token_name):
    market_chart = get_coin_market_chart(token_name)
    market_caps = [{
        'date':datetime.utcfromtimestamp(int(item[0]/1000)),
        'mcap':item[1]
        } for item in market_chart['market_caps']]
    df = pd.DataFrame(market_caps)
    return df