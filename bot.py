# coding: utf-8
# In[ ]:

from RandomSentence import random_sentence, random_verse
from RealSentence import real_sentence
from CunadoSentence import cunado_sentence

from config import TOKEN
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import logging

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)

#Token:
updater = Updater(token = TOKEN)

#dispatcher
dispatcher = updater.dispatcher

#Mensajes de información del programa
help_file = './data/help.txt'
help_txt = open(help_file).read()

info_file = './data/info.txt'
info_txt = open(info_file).read()

##Comandos:

def help(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = help_txt)
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def start(bot, update):
    help(bot, update)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def info(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = info_txt)
info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)

def frase(bot, update, args):
    bot.send_message(chat_id = update.message.chat_id, text = random_sentence(' '.join(args)))
frase_handler = CommandHandler('frase', frase, pass_args = True)
dispatcher.add_handler(frase_handler)

def estrofa(bot, update, args):
    bot.send_message(chat_id = update.message.chat_id, text = random_verse(' '.join(args)))
estrofa_handler = CommandHandler('estrofa', estrofa, pass_args = True)
dispatcher.add_handler(estrofa_handler)

def real(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = real_sentence())
real_handler = CommandHandler('real', real)
dispatcher.add_handler(real_handler)

def cunado(bot, update, args):
    bot.send_message(chat_id = update.message.chat_id, text = cunado_sentence(' '.join(args)))
cunado_handler = CommandHandler('cunado', cunado, pass_args = True)
dispatcher.add_handler(cunado_handler)


#Poner en funcionamiento el programa
updater.start_polling()
updater.idle()
