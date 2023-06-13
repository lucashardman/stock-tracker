# Stock Tracker

Bem-vindo ao Stock Tracker! Este é um aplicativo web construído com o framework Django.

Este aplicativo permite consultar o valor de ativos listados na B3, e cadastrar um tracker para
acompanhar a sua variação de preço.

O Stock Tracker ainda permite configurar um cronjob que verifica a variação do preço e envia uma
notificação por e-mail caso o ativo atinja um valor estipulado.

## Pré-requisitos

Antes de executar o aplicativo, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.9 ou superior
- pipenv (gerenciador de pacotes Python)

Para rodar o cronjob é necessário:

- Uma conta de e-mail sem autenticação de 2 fatores ou uma conta no sendgrid

## Configuração do Ambiente

1. Clone o repositório do projeto para o seu computador:

```bash
git clone https://github.com/lucashardman/stock-tracker.git
```

2. Acesse o diretório do projeto:

```bash
cd <caminho_do_diretório>
```

3. Instalação das dependências e ativação do ambiente virtual:

```bash
pipenv install
pipenv shell
```

4. Adicione as variaveis de ambiente:

Crie um arquivo .env na raíz do projeto com o sequinte conteúdo.

- DJANGO_SECRET_KEY: secret_key do django. Pode ser gerado com o seguinte código:
```python
import secrets

secret_key = secrets.token_hex(32)
print(secret_key)
```

Qual método de disparo de e-mail:
- SEND_EMAIL_METHOD: "SENDGRID" ou "SMTPLIB"

Caso queira utilizar Sendgrid para o envio de e-mails:
- SENDGRID_API_KEY: api_key da sua conta do sendgrid
- SENDGRID_SENDER_EMAIL: um e-mail configurado com o sendgrid que será usado para disparar e-mails.

Caso queira utilizar smtplib para o envio de e-mails:
- SMTP_SENDER_EMAIL: um e-mail sem 2FA que será usado para disparar e-mails.
- SMTP_SERVER: o endereço do servidor SMTP que será utilizado para o envio dos e-mails. 
- SMTP_PORT: a porta do servidor SMTP que será utilizada para a conexão.
- SMTP_USERNAME: o nome de usuário ou identificação para autenticação no servidor SMTP.
- SMTP_PASSWORD: a senha associada ao nome de usuário para autenticação no servidor SMTP.

## Executando o Aplicativo

1. Carregue os arquivos estáticos:

```bash
python manage.py collectstatic
```

2. Realize as migrações do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

4. Inicie o cronjob:

Nesse caso há duas opções. A primeira é utilizando django-crontab.

```bash
python manage.py crontab add
```
No linux:
```bash
sudo service cron start
```

Para outros sistemas operacionais a forma de iniciar o serviço de cron é diferente.

A outra forma é utilizar script run_cronjobs.py, que simula o cronjob.

```bash
python run_cronjobs.py
```

5. Abra o navegador e acesse o seguinte URL: http://127.0.0.1:8000/


Agora você pode explorar o Stock Tracker localmente!



