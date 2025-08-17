# bot/main.py
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# === Настройка ===
API_TOKEN = '8268556497:AAEM7bCL2PWkX3jH4kxK3JZ1KAOMVoUSO0M'
WEB_APP_URL = 'https://kiborg80.github.io/space/'  # Ссылка на Mini App

# === Бот ===
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# === Клавиатура с Mini App ===
def get_mini_app_keyboard():
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(
            text="🚀 Открыть игру",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    return keyboard

# === Обработчик команды /start ===
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎮 Добро пожаловать в <b>Космическую Игру</b>!\n\n"
        "Нажми кнопку ниже, чтобы начать играть прямо в Telegram.",
        parse_mode="HTML",
        reply_markup=get_mini_app_keyboard()
    )

# === Запуск бота ===
async def main():
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())