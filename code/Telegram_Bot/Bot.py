import telegram

from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from telegram import Update


def get_voice(update: Update, context: CallbackContext) -> None:
    # get basic info about the voice note file and prepare it for downloading
    new_file = context.bot.get_file(update.message.voice.file_id)
    # download the voice note as a file
    new_file.download(f"voice_note.ogg")

def main():
    api_key = '5404455233:AAG5W7T5MOqyLNo3wEii_2JKtzTpAkdsw5k'
    user_id = '409080949'


    updater = Updater("5404455233:AAG5W7T5MOqyLNo3wEii_2JKtzTpAkdsw5k", use_context=True)
    bot = telegram.Bot(token=api_key)


    bot.sendAudio(chat_id=user_id, audio=open('TelegramBot\\brobob.mp3','rb'))

# Enable logging



if __name__ == '__main__':
    main()