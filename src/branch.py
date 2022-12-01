# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import pyexcel as p
import openpyxl
from PIL import Image, ImageDraw, ImageFont
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from socket import timeout
import datetime
counter = 108
counter2=0

def set(patch_name,font_family,font_size,x,y,text,image):
    im = Image.open(patch_name)
    font = ImageFont.truetype(font_family, size=font_size)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (x, y),
    str(text),
    font=font,
    fill='#fff')
    photo = im.save(image)
    global counter
    counter -= 1
    print(counter)

def center_bar():
    global counter2
    counter2 += 1
    now = datetime.datetime.now()
    g = now.strftime("%d-%m-%Y %H:%M")
    name = ('background/sample.png')
    im = Image.open('photo.png')
    font = ImageFont.truetype('font/1.ttf', size=30)
    draw_text = ImageDraw.Draw(im)
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
    str(str(counter2)),
    font=font,
    fill='#3A4046')
    photo = im.save('photo.png')
