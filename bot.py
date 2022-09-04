
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context): 
    print('/start just used')
    update.message.reply_text('Hello! You just run my first learn bot! Try it and enjoy!')
    # print(update)


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main(): 
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot stars')
    
    
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()