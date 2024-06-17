import telebot

from config.settings import env_keys


def send_telegram_message(message):
    """ Отправляем сообщение в чат бота """
    bot_token = env_keys.get('BOT_TOKEN')
    chat_id = env_keys.get('BOT_CHAT_ID')
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
