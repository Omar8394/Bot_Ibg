import telebot

BOT_TOKEN = "8410660377:AAHvGFZlmLQwhz7Z7_tEz0eQas52WcBdAJk"  # Reemplaza con tu token API
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, ¡bienvenido a mi bot!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
