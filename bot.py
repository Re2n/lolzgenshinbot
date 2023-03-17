import asyncio
from aiogram import Bot, Dispatcher, executor, types
from main import get_fresh_accs
bot = Bot(token='Telegram API')
dp = Dispatcher(bot)
chat_id = 'chat id'


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('hi')


async def new_accounts():

    while True:
        new_accs = get_fresh_accs()

        if len(new_accs) >= 1:
            acc = f"{'Ссылка: ' + str(new_accs[0]['url'])}" \
                  f"\n{'Цена: ' + str(new_accs[0]['price']) + ' руб'}" \
                  f"\n{'AR: ' + str(new_accs[0]['ar'])}" \
                  f"\n{'Легендарок: ' + str(new_accs[0]['legendary'])}\n" \
                  f"{new_accs[0]['name_of_legendary']}"
            print(acc)

            await bot.send_message(chat_id, acc)

        await asyncio.sleep(20)


if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.create_task(new_accounts())
        executor.start_polling(dp)
