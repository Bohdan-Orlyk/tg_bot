from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main_kb = [[
    KeyboardButton(text="Андрія"),
    KeyboardButton(text="Руслана"),
    KeyboardButton(text="Богдана"),
    KeyboardButton(text="Нікого не показуй, я \U0001F921")
]]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)