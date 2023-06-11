import yfinance as yf
from dotenv import load_dotenv
import os
import meilisearch

def fetch_stock_price(symbol):
    try:
        stock = yf.Ticker(f'{symbol}.SA')
        return {
            'success': True,
            'name': str(symbol).upper(),
            'price': "%.4f" % stock.history().tail(1)['Close'].iloc[0]
        }
    except:
        return {
            'success': False
        }



def write_dict_to_meilisearch(data):

    load_dotenv()

    api_key = str(os.getenv("MEILISEARCH_API_KEY"))
    base_url = f'https://{str(os.getenv("MEILISEARCH_INSTANCE"))}.meilisearch.io'
    index = str(os.getenv("MEILISEARCH_INDEX"))
    client = meilisearch.Client(base_url, api_key)
    client.index(index).add_documents([data])


def get_meilisearch(field):

    load_dotenv()

    api_key = str(os.getenv("MEILISEARCH_API_KEY"))
    base_url = f'https://{str(os.getenv("MEILISEARCH_INSTANCE"))}.meilisearch.io'
    index = str(os.getenv("MEILISEARCH_INDEX"))
    client = meilisearch.Client(base_url, api_key)
    return client.index(index).search(field)['hits']