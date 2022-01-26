import config
import telebot


token = "5093935580:AAGLpMwaKPBwXZx9I8RrgPQg2sNVWGgt228"
APP_URL = f'https://echo-bot-418.herokuapp.com/'
bot = telebot.TeleBot("5093935580:AAGLpMwaKPBwXZx9I8RrgPQg2sNVWGgt228")



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
