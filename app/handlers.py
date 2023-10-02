import keyboard as kb
import config

from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!", 
                         reply_markup=kb.main)



@router.message(F.text == "/show_ruslan")
async def show_ruslan(message: Message):
    await message.answer_photo(photo=config.IDs.get("ruslanuis_photo_id"), 
                               caption="Ces`t la Ruslanius."
                               )


@router.message(F.photo)
async def cmd_get_photo_id(message: Message):
    if message.from_user.id in config.ADMIN_IDs:
        await message.answer(message.photo[-1].file_id)
    else:
        await message.answer("This command can be used only by Admin. And you are.... NOT AN ADMIN, чортяка!")


@router.message()
async def no_cmd_chosen(message: Message):
    await message.answer("Такої команди нема, чєртіла!")