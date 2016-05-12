import sys
import configparser
import textwrap

import telebot
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

TOKEN = config['NOMEIA']['TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Me envie um nome para ser nomeado!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    Create_Image(message)

def Create_Image(message):
    text = ('{}, para exercer interinamente, o cargo de Secretário-Executivo '
            'da Casa Civil da Presidência da República, sem prejuízo das '
            'atribuições do que atualmente ocupa.')
    text = text.format(message.text.lower().title())
    text_wrap = textwrap.fill(text, 69)

    fonte = ImageFont.truetype('nimbus.ttf', 14)
    img = Image.open('DOU_alterado.png')
    draw = ImageDraw.Draw(img)
    draw.text((125,307), text_wrap, (0,0,0), font = fonte)
    draw = ImageDraw.Draw(img)
    img.save(str(message.from_user.id) + '.jpg')
    photo = open(str(message.from_user.id) + '.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)

bot.polling(none_stop=True)
while True:
    time.sleep(2)
