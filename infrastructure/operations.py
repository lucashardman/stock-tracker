import yfinance as yf

def fetch_stock_price(symbol):
    try:
        stock = yf.Ticker(f'{symbol}.SA')
        return {
            'success': True,
            'name': str(symbol).upper(),
            'price': "%.4f" % stock.history().tail(1)['Close'].iloc[0]
        }
    except Exception as e:
        print(e)
        return {
            'success': False
        }


