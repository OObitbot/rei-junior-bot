import asyncio from aiogram import Bot, Dispatcher, types

TOKEN = "7871258952:AAGUFy9JyQxzNo8DrVwgg-xnuvsjAYhysmc"  # Replace with your actual bot token
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer("Hello! I'm Rei Junior. How can I assist you today?")
    else:
        await message.answer("Thank you for your message! Our support team will respond soon.")

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        dp.include_router(dp)  # Required for aiogram 3
        await dp.start_polling(bot)
    finally:
        await bot.session.close()  # This prevents the "Unclosed client session" error

if __name__ == "__main__":
    asyncio.run(main())  # This is the last line, do not add anything after it

