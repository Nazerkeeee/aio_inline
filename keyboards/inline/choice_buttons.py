
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_LINGUAMARINA, URL_lUCY, URL_TED, URL_BBC, URL_TV

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Linguamarina", callback_data=buy_callback.new(item_name="Linguamarina", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="English with Lucy", callback_data="buy:English with Lucy:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Ted Talks", callback_data="buy:Ted Talks:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="BBC", callback_data="buy:BBC:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="English with TV series", callback_data="buy:English with TV series:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="Visit", url=URL_LINGUAMARINA)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_lUCY)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_BBC)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_TED)

    ]



])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_TV)

    ]

])