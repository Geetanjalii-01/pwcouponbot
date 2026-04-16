import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    users[message.chat.id] = {"step": "name"}
    bot.send_message(message.chat.id, "🎓 Welcome to PW COUPON CODE\n\nApna naam bhejo:")

@bot.message_handler(func=lambda m: True)
def all_messages(message):
    cid = message.chat.id

    if cid not in users:
        users[cid] = {"step": "name"}

    step = users[cid]["step"]

    if step == "name":
        users[cid]["name"] = message.text
        users[cid]["step"] = "phone"
        bot.send_message(cid, "📱 Mobile Number bhejo:")

    elif step == "phone":
        users[cid]["phone"] = message.text
        users[cid]["step"] = "class"
        bot.send_message(cid, "📚 Class / Exam bhejo:")

    elif step == "class":
        bot.send_message(cid, "🎉 Offer Unlocked 🔥\nhttps://www.pw.live/")
        users[cid]["step"] = "done"

bot.infinity_polling(skip_pending=True)
