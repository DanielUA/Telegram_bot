import telebot
from telebot import types

bot = telebot.TeleBot("5633349657:AAHvXGphY7k4i-TSoGE23RMInvkYlnUxhYg")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет!, <b>{message.from_user.first_name} <u>{message.from_user.username}.</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


# @bot.message_handler(content_types=["text"])
# def get_user_text(message):
#     if message.text == "Hello" or message.text == "Hi":
#         bot.send_message(message.chat.id, "Welcome to chatbot", parse_mode="html")
#     elif message.text == "photo":
#         photo = open("lamp.jpg", "rb")
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your ID:{message.from_user.id}""Welcome to chatbot", parse_mode="html")
#     else:
#         bot.send_message(message.chat.id, "I no understand you", parse_mode="html")


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "nice foto")

@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to site:", url = "http://habr.com"))
    bot.send_message(message.chat.id, "visit this site", reply_markup=markup)

bot.polling(none_stop=True)

if __name__ == "__main__":
    start()
