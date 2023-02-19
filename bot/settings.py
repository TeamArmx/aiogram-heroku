import os


BOT_TOKEN = '6262738056:AAEfRm1yPP5vc9aZ3I_a7g1RWKPgPqcHuDA' 
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

HEROKU_APP_NAME = 'heroic-credit'


# webhook settings
WEBHOOK_HOST = f'https://aiogram-heroku-production.up.railway.app'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT',5000))
