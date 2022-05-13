from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import webbrowser
import pyautogui

updater = Updater(f"{apikey}",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
		/signin")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/sport5gold - ספורט5גולד
	/sport5live - ספורט5לייב
	/sport5plus - ספורט5פלוס
	/sport5 - ספורט5
	/sport4 - ספורט4
	/sport3 - ספורט3
	/sport2 - ספורט2 
	/sport1 - ספורט1""")




def sport5(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport5.html")
    update.message.reply_text("sport 5 open in computer")

def sport1(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport1.html")
    update.message.reply_text("sport 1 open in computer")

def sport2(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport2.html")
    update.message.reply_text("sport 2 open in computer")

def sport3(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport3.html")
    update.message.reply_text("sport 3 open in computer")

def sport4(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport4.html")
    update.message.reply_text("sport 4 open in computer")

def sport5plus(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport5plus.html")
    update.message.reply_text("sport 5 plus open in computer")

def sport5gold(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport5gold.html")
    update.message.reply_text("sport 5 gold open in computer")

def sport5live(update: Update, context: CallbackContext):
    webbrowser.open("https://www.crackapps.online/iptv/sport5live.html")
    update.message.reply_text("sport 5 live open in computer")

def close(update: Update, context: CallbackContext):
    pyautogui.hotkey('ctrl', 'f4')
    update.message.reply_text("close chanel")
def showfunc(update: Update, context: CallbackContext):
    update.message.reply_text("/help")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('sport1', sport1))
updater.dispatcher.add_handler(CommandHandler('sport2', sport2))
updater.dispatcher.add_handler(CommandHandler('sport3', sport3))
updater.dispatcher.add_handler(CommandHandler('sport4', sport4))
updater.dispatcher.add_handler(CommandHandler('sport5', sport5))
updater.dispatcher.add_handler(CommandHandler('sport5plus', sport5plus))
updater.dispatcher.add_handler(CommandHandler('sport5gold', sport5gold))
updater.dispatcher.add_handler(CommandHandler('sport5live', sport5live))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('close', close))
updater.dispatcher.add_handler(CommandHandler('apikey', showfunc))



# Filters out unknown messages.

updater.start_polling()
