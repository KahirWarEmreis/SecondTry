import telebot
bot = telebot.TeleBot('891721503:AAE784YcJaxoQih6XLVSruOQjdGIFz01AeI')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(0)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
