from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main_kb = [[
    KeyboardButton(text="Покажи Андрія"),
    KeyboardButton(text="Покажи Руслана"),
    KeyboardButton(text="Покажи Богдана")
]]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)