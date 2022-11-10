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
