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

TOKEN = config['EXONERA']['TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "<b>Bem vindo ao NomeiaBot!</b>\n\nEnvie no formato:\n<i>nome, cargo</i>",parse_mode='HTML')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    Create_Image(message)

def Create_Image(message):
    try:
        nome, cargo = message.text.split(',')
    except ValueError:
        nome = message.text
        cargo = 'Secretário-Executivo da Casa Civil da Presidência da República'

    nome = nome.lower().title()
    cargo = cargo.title()

    text = ('{} do cargo de {}, '
            'sem prejuízo das atribuições do que '
            'atualmente ocupa.')
    text = text.format(nome, cargo)
    text_wrap = textwrap.fill(text, 69)

    fonte = ImageFont.truetype('nimbus.ttf', 14)
    img = Image.open('DOU_alterado2.png')
    draw = ImageDraw.Draw(img)
    draw.text((125,307), text_wrap, (0,0,0), font = fonte)
    draw = ImageDraw.Draw(img)
    img.save(str(message.from_user.id) + '.jpg')
    photo = open(str(message.from_user.id) + '.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)
    bot.send_message(message.from_user.id, 'Quer nomear alguém? @NomeiaBot\n\nConheça mais bots do Telegram no @BemVindo!')

bot.polling(none_stop=True)
while True:
    time.sleep(2)
