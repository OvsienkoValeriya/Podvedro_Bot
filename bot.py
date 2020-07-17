import telebot

token = "1170884194:AAF00_nt4txFB9Lp5jPWHA0QIfY2IypNNa4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["/start"])
def send_hello(message):
    chat_id = message.chat.id;
    bot.send_message(chat_id, "Привет! Прикрепи свой мем сюда")
    picture_handler(message)
    bot.send_message(chat_id, "Спасибо! Твой мем получен")

@bot.message_handler(content_types = ['photo'])
def picture_handler(message):
    picture = message.picture

bot.polling()