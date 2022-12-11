from datetime import datetime, date, time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 
import ephem
from random import randint

logging.basicConfig(filename='bot.log', level=logging.INFO)

today = datetime.now()

def greet_user(update, context): 
    print('/start just used')
    update.message.reply_text("""Hello! You just run my first learn bot! Try it and enjoy!
You can use /planet command. Type /planet and planet what you want. For example /planet Mars.
Now bot can play with you in a simple game try it! use /guess 10 (where 10 is your number)""")


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
            update.message.reply_text(f"Current constellation of {planet} is {current_constellation}")
        except AttributeError: 
            update.message.reply_text("Please enter a correct planet")


def game_func(update, context):
    if context.args:
        try: 
            user_number = int(context.args[0])
            message = play_numbers(user_number)
        except (TypeError, ValueError): 
            message = "Please enter a correct number!"
    else:
        message = "You don't put number!"
    update.message.reply_text(message)


def play_numbers(user_number): 
    bot_number = randint(user_number-10, user_number+10)
    if bot_number > user_number: 
        message = f"Your numbers is {user_number}, bot number is {bot_number}. Bot wins!"
    elif bot_number == user_number:
        message = f"Your number is {user_number}, bot number is {bot_number}. Draw!"
    else: 
        message = f"Your numbers is {user_number}, bot number is {bot_number}. You win!"
    return message


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_func))
    dp.add_handler(CommandHandler('guess', game_func))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot starts')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
