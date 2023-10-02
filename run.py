import asyncio

from aiogram import Dispatcher, Bot, F

from app.handlers import router


async def main():
    print("I`M ALIVE!!")
    bot = Bot(token='6495424464:AAHxmm-wC9xHgZRUdGiM3BnHX1Lut-M3wWg')
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("SHUTDOWN!!!")

