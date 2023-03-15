import telegram
from telegram import Update, ForceReply
from telegram.ext import CallbackContext, MessageHandler, filters, Application, CommandHandler

import configRedirect as conf
import mysite.Malphite.logManager as log
import output_handler

api_key = conf.get_apiKey()
if api_key.__len__() < 8:
    log.logCritical('Key Telegram Bot non trovata :(')
    exit(0)
application = Application.builder().token(api_key).build()


def __userValido(user: str) -> bool:
    return user == conf.get_userId()


# TODO: non funziona
async def invia_audio(filename: str, testo: str):
    global application
    user_id = conf.get_userId()
    if len(user_id) < 9:
        log.logError("ID utente Telegram < 9, errore di inserimento?")
        return
    await telegram.Bot(api_key).sendMessage(chat_id=user_id, text="Richiesta non gestita")
    #await application.bot.sendMessage(chat_id=user_id, text="Richiesta non gestita")
    #await application.bot.send_audio(chat_id=user_id, audio=open(filename, 'rb'))
    #await application.bot.send_message(chat_id=user_id, text="Testo compreso: "+testo)
    log.logInfo(f"Inviato audio {filename} non gestito, testo compreso = {testo}")


async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    log.logInfo("Bot Telegram start da utente con id = {" + str(user.id) + "}")
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Your id is: {str(user.id)}",
        reply_markup=ForceReply(selective=True),
    )


async def showid(update: Update, context: CallbackContext) -> None:
    await update.message.reply_html(
        rf"Your id is: {str(update.effective_user.id)}",
        reply_markup=ForceReply(selective=True),
    )


async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_html(
        rf"Commands are: /myid /help /richieste",
        reply_markup=ForceReply(selective=True),
    )


async def echo(update: Update, context: CallbackContext) -> None:
    global application
    if __userValido(str(update.effective_user.id)):
        await update.message.reply_text("hey! ciao " + conf.get_userId())
    else:
        await update.message.reply_text("Non sei collegato :< --" + conf.get_userId())
        try:
            percorso = 'tmp.wav'
            file = await application.Bot.get_file(update.message.audio.file_id)
            await telegram.File.download(custom_path=percorso)
            #file = await context.bot.get_file(update.message.voice.file_id)
            # await file.download(custom_path=percorso)
            #id_messaggio = await application.bot.get_updates().message.voice.file_id
            # output_handler.riproduci_audio(percorso)
            # fh.elimina_audio(percorso) todo: re-inserire
        except RuntimeError:
            pass
        """Documentazione @ https://docs.python-telegram-bot.org/en/v20.0a4/telegram.file.html#telegram.File """


async def audioh(update: Update, context: CallbackContext) -> None:
    global application
    if __userValido(str(update.effective_user.id)):
        await update.message.reply_text("collegato!")
        percorso = 'tmp.wav'
        file = await context.bot.get_file(update.message.voice.file_id)
        await file.download(custom_path=percorso)
    else:
        await update.message.reply_text("Non sei collegato :< --" + conf.get_userId())


async def richieste(update: Update, context: CallbackContext) -> None:
    user = str(update.effective_user)
    if __userValido(user):
        file = open('Registrazione.m4a', 'rb')
        await update.message.reply_audio(file)

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("myid", showid))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("richieste", richieste))

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
application.add_handler(MessageHandler(filters.VOICE & ~filters.VOICE, audioh))
application.add_handler(MessageHandler(filters.INVOICE & ~filters.INVOICE, audioh))
application.run_polling(stop_signals=None)

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

"""
