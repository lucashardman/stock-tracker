from infrastructure.repositories.meilisearch import Meilisearch
from infrastructure.operations import send_email, fetch_stock_price
import datetime

def mailer():
    print("mailer")
    now = datetime.datetime.now()
    meili = Meilisearch()
    data = meili.search('')
    for dt in data:
        start_time = datetime.datetime.fromisoformat(
            dt.get("created_at_dt")
        )
        check_time = datetime.datetime.fromisoformat(
            dt.get("last_check_at_dt")
        )
        notification_time = check_time + datetime.timedelta(
            minutes=int(dt.get("timmer", 0))
        )
        notification_expire_time = start_time + datetime.timedelta(
            minutes=int(dt.get("track_time", 0))
        )

        stock_name = dt.get("name", "")
        user = dt.get("user", "")

        old_price = float(dt.get("price", 0))

        if notification_time < now:
            if notification_expire_time < now:
                meili.remove(dt.get("id"))
            else:
                print(f"Enviando email para {user} sobre {stock_name}")
                new_price = float(fetch_stock_price(stock_name).get("price", 0))

                if new_price > float(dt.get("max_val", old_price)):
                    send_email(
                        to=user,
                        subject=f"Aleração no preço da ação {stock_name}", 
                        body=f'O preço da ação {stock_name} subiu para {new_price}, atingindo o valor máximo de {dt.get("max_val")}.'
                    )
                elif new_price < float(dt.get("min_val", old_price)):
                    send_email(
                        to=user,
                        subject=f"Aleração no preço da ação {stock_name}", 
                        body=f'O preço da ação {stock_name} desceu para {new_price}, atingindo o valor mínimo de {dt.get("min_val")}.'
                    )
                meili.update(dt, {
                    "last_check_at_dt": datetime.datetime.now().isoformat(),
                    "price": new_price
                })
            

