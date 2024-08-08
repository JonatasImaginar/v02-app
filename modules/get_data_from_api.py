import json
import pandas as pd
from requests import Session, request

def get_data_from_api(config_api):
    
    # config_api
    # api_key = 'config_api.key'
    # api_url = 'config_api.url'
    # api_currency = 'config_api.currency'
    # start = config_api.start
    # limit = config_api.limit
    
    # Set limit of data from API
    parameters = {
    'start': config_api.start,
    'limit': config_api.limit,
    'convert': config_api.currency
    }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config_api.key
    }
    
    session = Session()
    session.headers.update(headers)
    
    name = []
    symbol = []
    data_added = []
    last_uptaded = []
    price = []
    volume_24h = []
    
    try:
        response = session.get(config_api.url, params=parameters)
        data = json.loads(response, text)
        
        for coin in data['data']:
            name.append(coin['name'])
            symbol.append(coin['symbol'])
            data_added.append(coin['data_added'])
            last_uptaded.append(coin['last_uptated'])
            price.append(coin['quote']['USD']['price'])
            volume_24h.append(coin['volume_24h'])
            
        # Create Dictionary
        coin_dict = {
            "name": name,
            "symbol": symbol,
            "data_added": data_added,
            "last_uptaded": last_uptaded,
            "price": price,
            "volume_24h": volume_24h
        }
        
        data = coin_dict
        
    except:
        print('Error to get data from API')
        exit(1)
        
    return data