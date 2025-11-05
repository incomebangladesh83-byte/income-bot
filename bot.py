import telebot

# তোমার BotFather থেকে নেওয়া API Token
TOKEN = "8594604204:AAF9Np7O5xDIK9yB6l9TVe_NXemx7y1Sigs"
bot = telebot.TeleBot(TOKEN)

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 স্বাগতম ইনকাম বাংলাদেশ বটে!\n\n👉 প্রথমে আমাদের চ্যানেলগুলো জয়েন করো।")

# সাধারণ টেক্সট মেসেজ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "✅ ধন্যবাদ! তোমার মেসেজ পাওয়া গেছে।")

# বট চালু রাখা
bot.infinity_polling()
