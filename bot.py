from datetime import datetime, date, time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)

today = datetime.now()

def greet_user(update, context): 
    print('/start just used')
    update.message.reply_text("Hello! You just run my first learn bot! Try it and enjoy!\nYou can use /planet command. Type /planet and planet what you want. For example /planet Mars")
    #print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_func(update, context): 
    print("/planet just used")
    get_planet = update.message.text.split()
    planet = get_planet[1].capitalize()
    print("User choose", planet)
    if planet:
        try: 
            current_constellation = ephem.constellation(getattr(ephem, planet)(today))[1]
            update.message.reply_text(f"Corrent constellation of {planet} is {current_constellation}")
        except AttributeError: 
            update.message.reply_text("Please enter a correct planet")


def main(): 
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_func))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot starts')
    
    
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()