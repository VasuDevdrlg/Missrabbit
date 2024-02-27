import telebot
from dictionary import dict
from transalator import gtranslator
from quoty import quotemaker
from spellcheck import bee
bot_token = '1864130526:AAFShQTgpSHrlWI9elGlsttnEYK9i2CJh_Q'
bot = telebot.TeleBot(bot_token)

# Define a command handler
@bot.message_handler(commands=['start'])
def handle_st(message):
    welcome=f"Welcome To \n🌟[Rabbit - your Language Companion!](https://graph.org/file/0ffec7be1d9bcb7fb0c63.jpg)🐇💬\n\n📚 Ready to Explore the world of Languages?\n\n✍Need a translation? Just ask! Seeking the meaning of a word? We've got your back! \n\n🚀Plus, spice up your day with some randomly generated quotes for that extra inspiration!⚡,\n\nTap /help To Know how to Use Me🐰"
    bot.reply_to(message, welcome,parse_mode='Markdown')
@bot.message_handler(commands=['help'])
def handle_st(message):
  help_message = (
    "📚 Rabbit is here to assist you with a variety of language-related commands. Here's how you can use Rabbit to enhance your linguistic journey:\n\n"
    
    "1. Define a Word:🔍\n"
    "   Usage: `/define [word]`\n"
    "   Example: `/define Dignity`\n"
    "   Description: Get the meaning of a word.\n\n"
    
    "2. Spell Check:🔡\n"
    "   Usage: `/spell [word]`\n"
    "   Example: `/spell Wrte`\n"
    "   Description: Get suggestions for correcting a misspelled word.\n\n"
    
    "3. Generate a Quote:📖\n"
    "   Usage: `/quote [topic ]`\n"
    "   Example: `/quote nature`\n"
    "   Description: Get an inspiring random quote.\n\n"
    
    "4. Language Translator:👨‍🎓\n"
    "   Usage: `/(target language name) [text]`\n"
    "   Example: `/telugu how are you`\n"
    "   Example: `/hindi Iam eating`\n"
    "   Example: `/english  ഏയ് സഹോദരൻ`\n"
    "   Description: Translate text to Target language.\n\n"
    "Happy chatting with Rabbit! 🌟🐰")
  bot.reply_to(message,help_message,parse_mode='Markdown')

# Define a message handler
@bot.message_handler(func=lambda message: True)
# Define a message handler
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        text = message.text
        if text.startswith('/'):
            command = text.split(maxsplit=1)
            cname = command[0]
            ctext = command[1] if len(command) > 1 else None
            if cname == "/define":
                try:
                    key = dict(ctext)
                    bot.reply_to(message, f"Meaning of {ctext}🔍:\n\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"Check Spelling For your Word")
            elif cname == "/spell":
                try:
                    key = bee(ctext)
                    bot.reply_to(message, f"Did you Mean 🤔?\n {key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == "/quote":
                try:
                    key = quotemaker(ctext)
                    bot.reply_to(message, key)
                except Exception as e:
                    bot.reply_to(message, f"Check Your Query")
            elif cname == "/telugu":
                try:
                    key = gtranslator(ctext, "telugu")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn Telugu📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == "/tamil":
                try:
                    key = gtranslator(ctext, "tamil")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn Tamil📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == "/kannada":
                try:
                    key = gtranslator(ctext, "kannada")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn Kannada📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == "/hindi":
                try:
                    key = gtranslator(ctext, "hindi")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn Hindi📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == '/english':
                try:
                    key = gtranslator(ctext, "english")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn English📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            elif cname == "/malayalam":
                try:
                    key = gtranslator(ctext, "malayalam")
                    bot.reply_to(message, f"Orginal✍:\n{ctext}\n\nIn Malayalam📝:\n{key}")
                except Exception as e:
                    bot.reply_to(message, f"An error occurred: {e}")
            else:
                bot.reply_to(message, "Unexpected error🙁\n Check Your Command /help")
        else:
            bot.reply_to(message, "Unexpected error🙁\nCheck Your Command /help")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

bot.polling()
