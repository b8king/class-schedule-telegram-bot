from openpyxl import load_workbook
import pyexcel as p
import openpyxl
from PIL import Image, ImageDraw, ImageFont

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from socket import timeout
import datetime
import time
start_time = time.time()
counter = 0




def get_conversion():
    global counter

    counter += 1

    now = datetime.datetime.now()
    g = now.strftime("%d-%m-%Y %H:%M")
    name = ('background/sample.png')
    im = Image.open(name)
    font = ImageFont.truetype('font/1.ttf', size=30)
    draw_text = ImageDraw.Draw(im)
    res = "%s СЕК" % (time.time() - start_time)
    draw_text.text(
    (328, 791),
    str(g),
    font=font,
    fill='#3A4046')
    photo = im.save('photo.png')
        
    im = Image.open('photo.png')
    font = ImageFont.truetype('font/1.ttf', size=30)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (2338, 793),
    str(str(counter)),
    font=font,
    fill='#3A4046')
    photo = im.save('photo.png')

    im = Image.open('photo.png')
    font = ImageFont.truetype('font/1.ttf', size=30)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (1168, 794),
    str(res),
    font=font,
    fill='#3A4046')
    photo = im.save('photo.png')
    
get_conversion()