import asyncio

from aiogram.types import Message

async def get_person(message: Message):
    if message.text.startswith("P"):
        return "ruslanuis_photo_id"
    if message.text.startswith("Б"):
        return "my_photo_id"
    if message.text.startswith("Ан"):
        return "andrews_photo_id"