import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
from .sqlit import reg_user,cheak_traf
from loader import dp, bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard
import asyncio

content = -1001523076616



@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    ans = reg_user(update.from_user.id)

    try:
        await update.approve()
    except:
        pass

    if int(ans) == 1: #Человек первый раз заходит в бота
        await asyncio.sleep(60)
        await bot.copy_message(from_chat_id=content, message_id=24,chat_id=update.from_user.id,caption="""
<b>Спасибо за подписку❤️
    
Возможно тебе понравятся наши другие проекты 👑</b>
    
<i>Вписки 👉🏻 <a href = 'https://t.me/+P7jD70-86bA5Mzky'>t.me/vpiski_channel</a>
Сливы 👉🏻 <a href = 'https://t.me/+d3wAvpMBCaoyYzgy'>t.me/Sliv_channel</a>
Миленькие 👉🏻 <a href = 'https://t.me/+JtDy7OrqctszOTAy'>t.me/Girls_channel</a></i>""")