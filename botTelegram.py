from telegram import Update, ForceReply
from telegram.ext import CallbackContext, MessageHandler, filters, Application, CommandHandler

import configManager as conf
import logManager as log

api_key = conf.get_apiKey()
if api_key.__len__() < 8:
    log.logCritical('Key Telegram Bot non trovata :(')
    exit(0)
application = Application.builder().token(api_key).build()


def invia_audio(filename: str, testo: str):
    global application
    user_id = conf.get_userId()
    application.Bot.send_message(chat_id=user_id, text="Richiesta non gestita")
    application.Bot.send_audio(chat_id=user_id, audio=open(filename, 'rb'))
    application.Bot.send_message(chat_id=user_id, text="Testo compreso: "+testo)
    log.logInfo(f"Inviato audio {filename} non compreso, testo compreso = {testo}")

    # TODO: fare il loop "while true" per la risposta audio
    id_messaggio = application.Bot.get_updates().message.voice.file_id
    application.Bot.get_file(id_messaggio).download('/ricevuti_da_telegram')
    """DOCS @ https://docs.python-telegram-bot.org/en/v20.0a4/telegram.file.html#telegram.File """
    # todo: controllare l'output.


async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    log.logInfo("Bot Telegram start da utente con id = {" + str(user.id) + "}")
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Your id is: {str(user.id)}",
        reply_markup=ForceReply(selective=True),
    )

# NOTA:: Questo meccanismo va nella web gui
"""def __aggiorna_user_id(userid: int):
    global config
    global user_id
    user_id = str(userid)
    config['user_id'] = user_id
    fh.scrivi_config(config)"""


async def showid(update: Update, context: CallbackContext) -> None:
    await update.message.reply_html(
        rf"Your id is: {str(update.effective_user.id)}",
        reply_markup=ForceReply(selective=True),
    )


async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_html(
        rf"Commands are:"
        rf"/myid"
        rf"/help",
        reply_markup=ForceReply(selective=True),
    )


async def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if update.effective_user.id != conf.get_userId():
        await update.message.reply_text("Non sei collegato :<")
    else:
        await update.message.reply_text("ok")


# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("myid", showid))
application.add_handler(CommandHandler("help", help))

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
application.run_polling()


# todo check se funziona
def spegni():
    global application
    application.shutdown()
    log.logInfo("segnale spegnimento bot")


""" 
import telegram

from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from telegram import Update


def get_voice(update: Update, context: CallbackContext) -> None:
    # get basic info about the voice note file and prepare it for downloading
    new_file = context.bot.get_file(update.message.voice.file_id)
    # download the voice note as a file
    new_file.download(f"voice_note.ogg")


def main():
    api_key = ''
    user_id = ''

    updater = Updater("", use_context=True)
    bot = telegram.Bot(token=api_key)

    bot.sendAudio(chat_id=user_id, audio=open('TelegramBot\\brobob.mp3', 'rb'))


# Enable logging


if __name__ == '__main__':
    main()
"""
