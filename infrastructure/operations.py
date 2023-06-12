import yfinance as yf
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

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


def send_email(subject, body):
    try:
        load_dotenv()
        sg = SendGridAPIClient(str(os.getenv("SENDGRID_API_KEY")))
        sg.send(
            Mail(
                from_email=str(os.getenv("EMAIL_SENDER")),
                to_emails=str(os.getenv("EMAIL_SENDER")),
                subject=subject,
                plain_text_content=body
            )
        )
        print('Email sent successfully!')
    except Exception as e:
        print('Error sending email:', str(e))