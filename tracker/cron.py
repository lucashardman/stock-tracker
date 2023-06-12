from infrastructure.repositories.meilisearch import Meilisearch
import datetime

def mailer():
    print("mailer")
    now = datetime.datetime.now()
    meili = Meilisearch()
    data = meili.search('')
    # meili.reset_index()
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
        if notification_time < now:
            print(notification_time, now)
            print("Enviando email para:")
            print(dt)
            meili.update(dt, {"last_check_at_dt": datetime.datetime.now().isoformat()})
            if notification_expire_time < now:
                meili.remove(dt.get("id"))

