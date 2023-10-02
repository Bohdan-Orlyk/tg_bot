import app.keyboard as kb 
import config

from aiogram import Router, F
from aiogram.types import Message

# from utils import get_person

router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer_photo(photo=config.IDs["gustavo"])
    await message.answer(f"""
                        Hello, {message.from_user.full_name}!
                        \nMy Name Is Gustavo But You Can Call Me Gus.
                        \nI will be your guide on this tour. 
                        \nFirst of all I want to show one of us but you need to chose who.
                        """, 
                        reply_markup=kb.main
                    )


@router.message(F.text == "Руслана")
async def show_ruslan(message: Message):
    # person = await get_person(message)

    await message.answer_photo(photo=config.IDs.get("ruslanuis_photo_id"), 
                               caption="C'est Ruslanius."
                            )


@router.message(F.text == "Богдана")
async def show_ruslan(message: Message):
    await message.answer_photo(photo=config.IDs.get("my_photo_id"), 
                               caption="C'est moi."
                            )


@router.message(F.text == "Андрія")
async def show_ruslan(message: Message):
    await message.answer_photo(photo=config.IDs.get("andrews_photo_id"), 
                               caption="C'est Andrew."
                            )


@router.message(F.text == config.OPTIONs["nobody"])
async def show_ruslan(message: Message):
    await message.answer_animation(animation=config.IDs.get("monkey_with_phone"), 
                                   caption="Don't worry, we're already looking for you. This may be your last day on Earth."
                                )


@router.message()
async def no_cmd_chosen(message: Message):
    await message.answer("Такої команди нема, чєртіла!")


@router.message(F.animation)
async def cmd_get_animation_id(message: Message):
    if message.from_user.id in config.ADMIN_IDs:
        await message.answer(message.animation.file_id)
    else:
        await message.answer("This command can be used only by Admin. And you are.... NOT AN ADMIN, чортяка!")


@router.message(F.photo)
async def cmd_get_photo_id(message: Message):
    if message.from_user.id in config.ADMIN_IDs:
        await message.answer(message.photo[-1].file_id)
    else:
        await message.answer("This command can be used only by Admin. And you are.... NOT AN ADMIN, чортяка!")