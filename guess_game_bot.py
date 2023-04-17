import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, timedelta

# set up the bot
TOKEN = "6167877840:AAEw-BDBQoXhyS3017XBOa70GQxPnUoFVyQ"
bot = telegram.Bot(token=6167877840:AAEw-BDBQoXhyS3017XBOa70GQxPnUoFVyQ)

# define the start function
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Type /fun to start the game.')

# define the fun function
def fun(update, context):
    """Start a game and let users guess a number within one minute."""

    # generate a random number from 1 to 100
    answer = random.randint(1, 100)
    
    # send the game instruction message
    message = "Very 'FUN' game has been started\n\nRules are simple, I have a number from 1 to 100 and you have to guess it.\n\nIf your answer will be close enough to my number you will win, if not, you are fucking loser.\n\nYou have one minute.\n\nNow please type your number in chat."
    update.message.reply_text(message)

    # set the game end time
    end_time = datetime.now() + timedelta(minutes=1)

    # store the user's guess
    user_guesses = {}

    # loop until time runs out
    while datetime.now() < end_time:
        try:
            # get the user's guess
            guess = int(update.message.text)

            # store the user's guess with their username
            user_guesses[update.message.from_user.username] = guess

            # give feedback to the user
            if guess == answer:
                update.message.reply_text("Congratulations! You've guessed it!")
                return
            elif abs(guess - answer) <= 10:
                update.message.reply_text("Close enough! You're almost there!")
            else:
                update.message.reply_text("Sorry, that's not the right answer.")
        except ValueError:
            # user didn't enter a number, ignore and continue
            pass

    # send the result message after the game ends
    message = "Time's up! The correct answer was {}.\n\nHere are the results:\n\n".format(answer)
    for user, guess in user_guesses.items():
        message += "{} guessed {}\n".format(user, guess)
    update.message.reply_text(message)

# create the handlers and add them to the dispatcher
updater = Updater(6167877840:AAEw-BDBQoXhyS3017XBOa70GQxPnUoFVyQ, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("fun", fun))

# start the bot
updater.start_polling()
updater.idle()
