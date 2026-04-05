import asyncio
import logging
import wikipedia
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
wikipedia.set_lang("uz")

async def menu_commands():
    commands = [
        BotCommand(command='start', description="Run the bot")
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

@dp.message(Command('start'))
async def start_cmd(message: Message):
    await message.reply(f"""
Assalomu alaykum {message.from_user.full_name}
Qidiriuv uchun biron so'z yozing, men wikipediadan ma'lumot topib beraman
    """)

@dp.message(F.text)
async def wiki_cmd(message: Message):
    await message.answer("🔍Qidirilmoqda...")
    try:
        search_text = message.text
        wiki_answer = wikipedia.summary(search_text, sentences=5)
        await message.answer(f"Wikipeadiadan javob: \n\n{wiki_answer}")

    except Exception as error:
        await message.answer(f"Botda xatolik bo'ldi: {error}")
    


async def main():
    await menu_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


