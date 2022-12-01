#!venv/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from src import get
from src import convert
from src import branch
import sqlite3
import sqlite3 as lite
import logging
from aiogram.types import Message
from aiogram.types import file
from aiogram.types import File
from aiogram.types import InputFile
from aiogram.types import input_file
from aiogram.types import CallbackQuery
from aiogram.types import InputFile,InputMedia
from aiogram import Bot, Dispatcher, executor, types
from datetime import date
'''
───────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████████─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████████─
─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────
─██░░██████████─██░░██████████─██░░██─────────██░░██████░░██─██░░██████░░██─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██████████░░██─██░░██─────────██░░██████░░██─██░░██████████─██░░██████████─
─██░░██─────────────────██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██████████─██████████░░██─██░░██████████─██░░██──██░░██─██░░██─────────██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─
─██████████████─██████████████─██████████████─██████──██████─██████─────────██████████████─
───────────────────────────────────────────────────────────────────────────────────────────
'''
bot = Bot(token="token")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
owner_id = 1455767363

async def chek(message: types.Message):
    try:
        file = "data/document/xls.xls" 
        BLOCK_SIZE = 65536 
        file_hash = hashlib.sha256() 
        with open(file, 'rb') as f: 
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0: 
                file_hash.update(fb) 
                fb = f.read(BLOCK_SIZE) 
        print (file_hash.hexdigest()) 
        key = file_hash.hexdigest()
        connect = sqlite3.connect('data/base/hash.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS key(
        hash TEXT)""")
        connect.commit()
        cursor.execute(f"SELECT hash FROM key WHERE hash = '{key}'")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO key VALUES(?)", [key])
            connect.commit()
        return replay(message)
    except:
        
        await chek(message)


@dp.message_handler(commands="up")
async def replay(message: types.Message):
    await message.delete()
    try:  
        while True:
            get.download()
            file = "data/document/xls.xls" 
            BLOCK_SIZE = 65536 
            file_hash = hashlib.sha256() 
            with open(file, 'rb') as f: 
                fb = f.read(BLOCK_SIZE)
                while len(fb) > 0: 
                    file_hash.update(fb) 
                    fb = f.read(BLOCK_SIZE) 
            key = file_hash.hexdigest()
            con = lite.connect('data/base/hash.db')
            with con:
                cur = con.cursor()    
                cur.execute("SELECT hash FROM key")
                while True:
                    row = cur.fetchone()
                            
                    if row == None:
                        break
                    key_data = str(row[0])
        
            if key == key_data:
                print('-')
            else:
                print('+')

                current_date = date.today()
                doc = open('data/document/xls.xls','rb')
                await message.answer_document(doc,caption=current_date)
                convert.get_conversion()
                file = InputFile(f'photo.png')
                await bot.send_photo(
                message.chat.id,
                photo=file)

                file = "data/document/xls.xls" 
                BLOCK_SIZE = 65536 
                file_hash = hashlib.sha256() 
                with open(file, 'rb') as f: 
                    fb = f.read(BLOCK_SIZE)
                    while len(fb) > 0: 
                        file_hash.update(fb) 
                        fb = f.read(BLOCK_SIZE) 
                print (file_hash.hexdigest()) 
                key = file_hash.hexdigest()
                try:
                    connect = sqlite3.connect('data/base/hash.db')
                    cursor = connect.cursor()
                    cursor.execute(f"Update key set hash = (?)",(key,))
                    connect.commit()
                    print("Запись успешно обновлена")
                    cursor.close()            
                except:
                    await bot.send_message(owner_id, "@keeptelegram 112")
                    return replay(message)
                    
    except:
        await bot.send_message(owner_id, "@keeptelegram 116")
        return replay(message)

      
if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True) 


#-->upd:2022-09-21 
#-->upd:2022-09-23
#-->upd:2022-09-29
#-->upd:2022-10-18 [130 сек]
#-->upd:2022-12-1 [33 сек]
