import telegram
from telegram import Update, ForceReply
from telegram.ext import CallbackContext, MessageHandler, filters, Application, CommandHandler, Updater

import configRedirect as conf
import logManager as log

api_key = conf.get_apiKey()
if api_key.__len__() < 8:
    log.logCritical('Key Telegram Bot non trovata :(')
    exit(0)
application = Application.builder().token(api_key).build()


def __userValido(user: str) -> bool:
    return user == conf.get_userId()


async def invia_audio(filename: str, testo: str):
    user_id = conf.get_userId()
    if len(user_id) < 9:
        log.logError("ID utente Telegram < 9, errore di inserimento?")
        return
    b = telegram.Bot(api_key)
    await b.send_message(chat_id=user_id, text=testo)
    f = open(filename, 'rb')
    await b.send_document(chat_id=user_id, document=f)


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
        try:
            percorso = 'ricevutiTelegram/temporaneo.wav'
            audio = update.message.audio
            voice = update.message.voice
            if audio is not None:
                tmp = await audio.get_file()
                path = await tmp.download(custom_path=percorso)
                await update.message.reply_text(str(path))
            elif voice is not None:
                tmp = await voice.get_file()
                path = await tmp.download(custom_path=percorso)
                await update.message.reply_text(str(path))
            else:
                await update.message.reply_text("Non audio o voice")
        except Exception as e:
            await update.message.reply_text(str(e))
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

application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))
application.run_polling(stop_signals=None)
