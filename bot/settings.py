import os


BOT_TOKEN = '5734388256:AAHFS1seyZNDE3Lxr_R28v6qCaijrN1tyw8' 
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

HEROKU_APP_NAME = 'onclikk'


# webhook settings
WEBHOOK_HOST = f'https://onclikk.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT',5000))
