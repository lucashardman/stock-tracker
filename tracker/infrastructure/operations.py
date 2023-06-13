from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from email.message import EmailMessage
from dotenv import load_dotenv
import yfinance
import smtplib
import os


def fetch_stock_price(symbol):
    try:
        stock = yfinance.Ticker(f'{symbol}.SA')
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


def send_email(to, subject, body):

    load_dotenv()
    print(str(os.getenv("SEND_EMAIL_METHOD", "")))
    if os.getenv("SEND_EMAIL_METHOD", "") == "SMTP":
        print("aquiiiii")
        try:
            sender_email = str(os.getenv("SENDER_EMAIL", ""))
            smtp_server = str(os.getenv("SMTP_SERVER", ""))
            smtp_port = int(os.getenv("SMTP_PORT", 0))
            smtp_username = str(os.getenv("SMTP_USERNAME", ""))
            smtp_password = str(os.getenv("SMTP_PASSWORD", ""))

            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = to

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)

            print('Email sent successfully!')
        except Exception as e:
            print('Error sending email:', str(e))
    elif str(os.getenv("SEND_EMAIL_METHOD", "") == "SENDGRID"):
        try:
            sg = SendGridAPIClient(str(os.getenv("SENDGRID_API_KEY")))
            sg.send(
                Mail(
                    from_email=str(os.getenv("EMAIL_SENDER")),
                    to_emails=to,
                    subject=subject,
                    plain_text_content=body
                )
            )
            print('Email sent successfully!')
        except Exception as e:
            print('Error sending email:', str(e))
    else:
        print("Set SEND_EMAIL_METHOD to SMTP or SENDGRID in .env file")
