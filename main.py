from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="5375306425:AAGOt8M2ZEFwBjdppkUVlZH6bVbRZQklgv0", parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("hi bro")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
