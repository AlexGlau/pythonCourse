from telegram.ext import Updater

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater('854780013:AAFlSL13uIjGvutGeoKA4XpIlpy53dL4_nY', request_kwargs=PROXY)
    mybot.start_polling()
    mybot.idle()

main()
