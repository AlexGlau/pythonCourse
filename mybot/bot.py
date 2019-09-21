from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5h://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater('854780013:AAFlSL13uIjGvutGeoKA4XpIlpy53dL4_nY', request_kwargs=PROXY)

    def greet_user(bot, update):
        text = '/start called'
        update.message.reply_text(text)

    def talk_to_me(bot, update):
        user_text = update.message.text
        print(f'user msg: {user_text}')
        update.message.reply_text(user_text)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
