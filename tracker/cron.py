from infrastructure.repositories.meilisearch import Meilisearch
import datetime

def mailer():
    now = datetime.datetime.now()
    meili = Meilisearch()
    data = meili.search('')
    for dt in data:
        notification_time = datetime.datetime.fromisoformat(
            dt.get("created_at_dt")
        ) + datetime.timedelta(minutes=int(dt.get("timmer", 0)))
        if notification_time < now:
            print(f"Enviando email para {dt.get('email')}")

