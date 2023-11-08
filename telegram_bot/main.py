import logging
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Router, types, F, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from telegram_bot.handlers.callbacks import router as callbacks_router
from telegram_bot.handlers.callbacks import Menu, Report, report_fivem


bot_token = '6308064091:AAH1U3grSp3rGRQG-47KbBFublyg4WI_B-o'
bot = Bot(token=bot_token)
router = Router()
router.include_router(callbacks_router)
dispatcher = Dispatcher()
dispatcher.include_router(router)

logging.basicConfig(level=logging.INFO)


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    main_btns = InlineKeyboardBuilder()
    main_btns.add(types.InlineKeyboardButton(
        text="Задания",
        callback_data="home"
    ),
    types.InlineKeyboardButton(
        text="Мои создатели",
        callback_data="authors"
    )
    )
    await message.answer(
        "Привет, я бот, который поможет тебе со скучными докладами, рефератами и тд",
        reply_markup=main_btns.as_markup()
    )


@router.message(Command("home"))
async def report_tm(message: types.Message):
    await message.answer(
        report_fivem.report_theme
    )


async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
