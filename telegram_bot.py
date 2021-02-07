import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from utils import TelegramBotHandler, detect_intent_texts

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Здравствуйте! Чем можем помочь?')


def help_command(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Бот постарается ответить на ваш вопрос. Если он не знает ответа - ответит оператор.')


def detect_intent_and_send_answer(bot, update):
    """Echo the user message."""
    project_id = os.environ['GOOGLE_PROJECT_ID']
    answer = detect_intent_texts(project_id, update.message.chat['id'], [update.message.text], 'ru')
    if answer is not None:
        update.message.reply_text(answer)


def error_handler(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

    logger_handler = TelegramBotHandler(telegram_token, telegram_chat_id)
    logger_handler.setLevel(logging.WARNING)
    logger_handler.formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger.addHandler(logger_handler)

    updater = Updater(telegram_token)
    updater.logger.addHandler(logger_handler)
    dispatcher = updater.dispatcher
    dispatcher.logger.addHandler(logger_handler)
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, detect_intent_and_send_answer))
    dispatcher.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
