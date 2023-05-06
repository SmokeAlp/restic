import telebot
from telebot import types

bot = telebot.TeleBot("6187992700:AAGPNPX75KOtdQ5UkMuJ237Jv-oFxuCX9d0")


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'bebe')


@bot.message_handler(commands=['getInlineButtons'])
def inline_buttons(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='odin', callback_data=1))
    bot.send_message(message.from_user.id, 'BEBBE', reply_markup=markup)


@bot.message_handler(commands=['getReplyButtons'])
def keyline_button(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    bebe = types.KeyboardButton('bebe')
    bebe2 = types.KeyboardButton('bebe2')
    markup.add(bebe,bebe2)
    bot.send_message(message.from_user.id, 'BEBE', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def bebe_but(call: types.CallbackQuery):
    bot.send_message(call.from_user.id, call.data)


@bot.message_handler(content_types=['text', 'photo','sticker'])
def send_text(message: telebot.types.Message):
    bot.send_message(message.from_user.id, message.text)
    photo = open('restic_site/main/static/images/Beef.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)





bot.polling(none_stop=True)
