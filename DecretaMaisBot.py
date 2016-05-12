import sys
import telebot
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('bot.conf')

TOKEN = config['NOMEIA']['TOKEN']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    Create_Image(message)

def Create_Image(message): 
    fonte = ImageFont.truetype('nimbus.ttf', 14)
    img = Image.open('DOU_alterado.png')
    draw = ImageDraw.Draw(img)
    draw.text((125,307), message.text, (0,0,0), font = fonte)
    draw = ImageDraw.Draw(img)
    img.save(str(message.from_user.id) + '.jpg')
    photo = open(str(message.from_user.id) + '.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo)

bot.polling(none_stop=True)
while True:
    time.sleep(2)
