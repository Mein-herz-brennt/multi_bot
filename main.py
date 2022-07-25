from aiogram import Bot, Dispatcher, executor, types
from db import DateBase
bot = Bot(token="5375306425:AAGOt8M2ZEFwBjdppkUVlZH6bVbRZQklgv0", parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("hi bro")


@dp.message_handler(commands="admin", commands_prefix="!")
async def admin(message: types.Message):
    if message.from_user.id in DateBase().get_all_admins_id():
        await message.answer("hi bos")
    else:
        await message.answer("hi bitch")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
