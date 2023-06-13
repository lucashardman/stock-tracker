import django
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from tracker.cron import mailer
import time

# Caso o cronjob não funcione, use o código abaixo com um loop infinito que
# substitui o cronjob. Para isso, abra o terminal na raíz do projeto, ative
# o pyenv e digite: python3 tracker/cron.py
if __name__ == "__main__":
    while True:
        mailer()
        time.sleep(60)  