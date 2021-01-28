import logging
import os

from dotenv import load_dotenv
from google.cloud import dialogflow
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logger = logging.getLogger(__name__)


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={'session': session, 'query_input': query_input})

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        return response.query_result.fulfillment_text


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('привет привет!!')


def help_command(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    project_id = os.environ['GOOGLE_PROJECT_ID']
    answer = detect_intent_texts(project_id, update.message.chat['id'], [update.message.text], 'ru')
    update.message.reply_text(answer)


def error_handler(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    updater = Updater(telegram_token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    dispatcher.add_error_handler(error_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
