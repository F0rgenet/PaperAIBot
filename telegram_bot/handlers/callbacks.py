import logging
import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Router, types, F, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


class Menu(StatesGroup):
    choosing_task = State()


class Report(StatesGroup):
    time = State()
    theme = State()
    format = State()


router = Router()


@router.callback_query(F.data == "home")
async def back_home(callback: types.CallbackQuery, state: FSMContext):
    menu_btns = InlineKeyboardBuilder()
    menu_btns.add(types.InlineKeyboardButton(
        text="Доклад",
        callback_data="report")
    )
    await callback.message.edit_text(text="Выбери, с чем тебе помочь",
                         reply_markup=menu_btns.as_markup()
    )
    await state.set_state(Menu.choosing_task)


@router.callback_query(F.data == "report")
async def report(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer(
    )
    report_btns = InlineKeyboardBuilder()
    report_btns.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="home"
    ),
    types.InlineKeyboardButton(
        text="5 минут",
        callback_data="report_fiveminutes"
    ),
    types.InlineKeyboardButton(
        text="10+ минут",
        callback_data="report_tenminutes"
    )
    )
    await callback.message.edit_text(text="Супер, тебе нужен доклад. На сколько?",
                                     reply_markup=report_btns.as_markup())
    await state.set_state(Report.time)


@router.callback_query(F.data == "report_fiveminutes")
async def report_fivem(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Напиши тему"
    )
    await state.set_state(Report.theme)


@router.callback_query(F.data == "report_tenminutes")
async def report_tenm(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Напиши тему"
    )
    await state.set_state(Report.theme)


@router.message(Report.theme)
async def report_theme(message: types.Message, state: FSMContext):
    await message.answer(
        text="Супер, теперь выбери формат доклада",
        reply_markup=task_format().as_markup()
    )
    await state.set_state(Report.format)
    await state.update_data(theme=message.text)


def task_format():
    format_btn = InlineKeyboardBuilder()
    format_btn.add(
        types.InlineKeyboardButton(
            text=".txt",
            callback_data="txt"
        ),
        types.InlineKeyboardButton(
            text=".docx",
            callback_data="docx"
        ),
        types.InlineKeyboardButton(
            text=".pdf",
            callback_data="pdf"
        )
    )
    return format_btn


@router.callback_query(F.data == "txt")
async def format_txt(callback: types.CallbackQuery, state: FSMContext):
    pass


@router.callback_query(F.data == "docx")
async def format_txt(callback: types.CallbackQuery, state: FSMContext):
    pass


@router.callback_query(F.data == "pdf")
async def format_txt(callback: types.CallbackQuery, state: FSMContext):
    pass
