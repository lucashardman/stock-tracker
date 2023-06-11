import yfinance as yf
import time

def fetch_stock_price(symbol):
    try:
        stock = yf.Ticker(f'{symbol}.SA')
        return {
            'success': True,
            'name': symbol,
            'price': stock.history().tail(1)['Close'].iloc[0]
        }
    except:
        return {
            'success': False
        }
