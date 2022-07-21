from loader import dp
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard
from .sqlit import reg_user,obnova_status_all
obnova_status_all()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    reg_user(message.from_user.id)
