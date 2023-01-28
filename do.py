''' Run a function by ado <func_name> '''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import callback_query
import requests,user_agent,json,os,sys,secrets,names,urllib
import random, datetime
from faker import Faker 
from time import sleep
from user_agent import generate_user_agent

def set_hook():
    import asyncio
    from bot.settings import HEROKU_APP_NAME, WEBHOOK_URL, BOT_TOKEN
    from aiogram import Bot
    bot = Bot(token=BOT_TOKEN)

    async def hook_set():
        if not HEROKU_APP_NAME:
            print('You have forgot to set HEROKU_APP_NAME')
            quit()
        await bot.set_webhook(WEBHOOK_URL)
        print(await bot.get_webhook_info())
    

    asyncio.run(hook_set())
    bot.close()


def start():
    from bot.bot import main
    main()
