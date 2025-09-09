from datetime import datetime, date
from http import client
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import FSInputFile, Message, ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import List
from database.models import Order


client_router = Router()


def start_kb():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Комната 1", callback_data="room1"))
    builder.add(types.InlineKeyboardButton(text="Комната 2", callback_data="room2"))
    builder.add(types.InlineKeyboardButton(text="Комната 3", callback_data="room3"))
    builder.add(types.InlineKeyboardButton(text="Двор", callback_data="yard"))
    builder.add(types.InlineKeyboardButton(text="О нас", callback_data="about"))
    builder.add(types.InlineKeyboardButton(text="Частые вопросы", callback_data="popular_questions"))
    builder.adjust(1)
    return builder.as_markup()

def go_order():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Перейти к заказу", callback_data="order_start"))
    builder.add(types.InlineKeyboardButton(text="Назад 🔙", callback_data="start_menu"))
    builder.adjust(1)
    return builder.as_markup()



@client_router.message(Command("start"))
async def start_menu(message: types.Message):
    await message.answer_photo(photo = "https://cdn2.divan.ru/img/v1/sf9i8YRoVw34ZNh4LXzWT7om6dloRy_sUaEK3_8MNps/rs:fit:1920:1440:0:0/g:ce:0:0/bg:ffffff/q:85/czM6Ly9kaXZhbi9ja2VkaXRvci93aWtpLWFydGljbGUvMjU3MC82M2M1NWQ5OTY3ODhiLmpwZw.jpg",
                               caption = "Привет, это бот для снятия жилья в моих хоромах, выбери раздел для просмотра", reply_markup=start_kb())





@client_router.callback_query(F.data == "start_menu")
async def start(callback: CallbackQuery):
    await callback.message.answer_photo(photo = "https://cdn2.divan.ru/img/v1/sf9i8YRoVw34ZNh4LXzWT7om6dloRy_sUaEK3_8MNps/rs:fit:1920:1440:0:0/g:ce:0:0/bg:ffffff/q:85/czM6Ly9kaXZhbi9ja2VkaXRvci93aWtpLWFydGljbGUvMjU3MC82M2M1NWQ5OTY3ODhiLmpwZw.jpg",
                            caption = "Привет, это бот для снятия жилья в моих хоромах, выбери раздел для просмотра", reply_markup=start_kb())
    #await callback.answer()





@client_router.callback_query(F.data == "room1")
async def room1(callback: CallbackQuery):
    b = InlineKeyboardBuilder()
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.aueoQ7a5xg6e6gQL8C4Cz8LhxAgW4kQG3ufEDBr2wgw.jpg"),
                    caption="<b>Комната 1</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 3х человек",
                        parse_mode=ParseMode.HTML),
                        InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.gKuFMba5LEKzmO5HiUOVg--TLkQ7kK5K85UuQDeEKEA.fLf5q_ir1PtTgS1SXeydRd3mDR5lN_QQeSA0sIpxaJw.jpg")),
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.sNglI7a5HDETit40SU2l8E-BHjebgp45U4ceM5eWGDM.L81i4I9NbvN6lglTGOZS7QyZ0JAF0z7a39J-I3m_HKg.jpg")), 
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.u-uuo7a5FwKYCtUH1PXcw8QBFQQQApUK2AcVABwWEwA.JyXDDJVA6NsjryvmTZ5wkr6zj6beni77b-qArGSA94Q.jpg"))]
    b.button(text = "Перейти к заказу", callback_data="order_start")
    b.button(text = "Следующая комната ▶️", callback_data="room2")
    b.button(text="Назад 🔙", callback_data="start_menu")
    b.adjust(1)
    await callback.message.answer_media_group(media=media)
    await callback.message.answer("Выберете действие", reply_markup=b.as_markup())
    await callback.answer()







@client_router.callback_query(F.data == "room2")
async def room2(callback: CallbackQuery):
    b = InlineKeyboardBuilder()
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.WorLUra59mP9-zRm83sDz6Pw9GV183Rrvfb0YXnn8mE.jpg"), 
                             caption="<b>Комната 2</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 2х человек\nДиван расскладывается в большое двухместное спальное место", 
                             parse_mode=ParseMode.HTML), 
                             InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.2eC9T7a5dQmL5rcMg3iApdXtdw8D7vcBy-t3Cw_6cQs.nzp9R0Cfav5Y_OBDH5ynzqi696AXDsvaFcKbP-n37Q0.jpg")), 
                                                                         InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.L3lwora5g5BGC0GVIvoDURoAgZbOAwGYBgaBksIXh5I.gFEbS_DWbAFY2NVxn2R7mIZMsylfZBRNDheIgGdZ00I.jpg")), 
                                                                                         InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\dvor_room2.jpg"))]
    b.button(text = "Перейти к заказу", callback_data="order_start")
    b.button(text = "Следующая комната ▶️", callback_data="room3")
    b.button(text="Назад 🔙", callback_data="start_menu")
    b.adjust(1)
    
    await callback.message.answer_media_group(media = media)
    await callback.message.answer("Выберете действие", reply_markup=b.as_markup())
    await callback.answer()






@client_router.callback_query(F.data == "room3")
async def room3(callback: CallbackQuery):
    b = InlineKeyboardBuilder()
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.aueoQ7a5xg6e6gQL8C4Cz8LhxAgW4kQG3ufEDBr2wgw.jpg"),
                    caption="<b>Комната 3</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 3х человек",
                        parse_mode=ParseMode.HTML),
                        InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.gKuFMba5LEKzmO5HiUOVg--TLkQ7kK5K85UuQDeEKEA.fLf5q_ir1PtTgS1SXeydRd3mDR5lN_QQeSA0sIpxaJw.jpg")),
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.sNglI7a5HDETit40SU2l8E-BHjebgp45U4ceM5eWGDM.L81i4I9NbvN6lglTGOZS7QyZ0JAF0z7a39J-I3m_HKg.jpg")), 
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.u-uuo7a5FwKYCtUH1PXcw8QBFQQQApUK2AcVABwWEwA.JyXDDJVA6NsjryvmTZ5wkr6zj6beni77b-qArGSA94Q.jpg"))]
    b.button(text = "Перейти к заказу", callback_data="order_start")
    b.button(text = "Следующая комната ▶️", callback_data="room1")
    b.button(text="Назад 🔙", callback_data="start_menu")
    b.adjust(1)
    await callback.message.answer_media_group(media=media)
    await callback.message.answer("Выберете действие", reply_markup=b.as_markup())
    await callback.answer()
    
    
    
    

@client_router.callback_query(F.data == "yard")
async def yard(cb: CallbackQuery):
    media = [InputMediaPhoto(media = FSInputFile(r"C:\Projectori\Rental_bot\img\yard1.jpg"),
                              caption="<b>Двор</b>\nВ нашем просторном дворе есть, мангальная зона, большая беседка и общая кухня со всей нужной посудой",
                                parse_mode=ParseMode.HTML),
              InputMediaPhoto(media = FSInputFile(r"C:\Projectori\Rental_bot\img\yard2.jpg")),
                InputMediaPhoto(media = FSInputFile(r"C:\Projectori\Rental_bot\img\yard3.jpg")),
                InputMediaPhoto(media = FSInputFile(r"C:\Projectori\Rental_bot\img\yard4.jpg"))]
    await cb.message.answer_media_group(media = media)
    await cb.message.answer("Выберите действие", reply_markup=go_order())
    await cb.answer()



@client_router.callback_query(F.data == "about")
async def about(cb: CallbackQuery):
    await cb.message.answer_photo(photo = "https://thumbs.dreamstime.com/b/%D0%B1%D0%B0%D0%B1%D1%83%D1%88%D0%BA%D0%B0-%D0%B2-%D0%BE%D1%87%D0%BA%D0%B0%D1%85-%D0%BE%D0%B1%D0%BD%D0%B8%D0%BC%D0%B0%D0%B5%D1%82-%D0%B2%D0%BD%D1%83%D0%BA%D0%B0-%D0%BF%D0%B0%D1%80%D0%BA%D0%B5-%D0%BD%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D1%83%D0%BB%D0%BA%D0%B5-370336011.jpg",
                                   caption="Мы с бабушкой сдаем двор уже миллион лет, приезжайте ебать", 
                                   reply_markup=go_order())
    await cb.answer()





@client_router.callback_query(F.data == "popular_questions")
async def popular_questions(cb: CallbackQuery):
    await cb.message.answer_photo(photo = "https://cdn-icons-png.flaticon.com/512/25/25333.png",
                                   caption="До моря 15 минут", 
                                   reply_markup=go_order())
    
    await cb.answer()



class Booking(StatesGroup):
    wait_for_name = State()
    wait_for_date1 = State()
    wait_for_date2 = State()
    wait_for_rooms = State()
    wait_for_phone = State()
    wait_for_confirm = State()


AVAILABLE_ROOMS = ["1", "2", "3"]



def parse_date(s: str):
    try:
        return datetime.strptime(s.strip(), "%d.%m.%Y").date()
    except Exception:
        return None


async def is_room_free(session: AsyncSession, room_id: str, date_from: date, date_to: date) -> bool:
    """
    Возвращает True если комната свободна на период [date_from, date_to)
    Пересечение определяется условием:
        existing.date_from < new.date_to AND existing.date_to > new.date_from
    """
    q = select(Order).where(
        and_(
            Order.room == room_id,
            Order.date_from < date_to,
            Order.date_to > date_from
        )
    )
    res = await session.execute(q)
    return res.first() is None


def build_rooms_kb(selected: List[str]) -> types.InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for r in AVAILABLE_ROOMS:
        prefix = "✅ " if r in selected else ""
        b.button(text=f"{prefix}Комната {r}", callback_data=f"toggle_room:{r}")
    b.button(text="✅ Готово", callback_data="rooms_done")
    b.button(text="Назад 🔙", callback_data="back_dates_to")
    b.button(text="На главную 🏡", callback_data="start_menu")
    b.adjust(3, 1, 1)
    return b.as_markup()



@client_router.callback_query(F.data == "order_start")
async def start_order(cb: CallbackQuery, state: FSMContext):
    await state.set_state(Booking.wait_for_name)
    await cb.message.answer("Как вас зовут? Введите полное ФИО")
    await cb.answer()



@client_router.message(Booking.wait_for_name, F.text & (F.text.len() > 1))
async def got_name(message: Message, state: FSMContext):
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("Слишком короткое имя. Введите полное ФИО.")
        return

    await state.update_data(name=name)
    await state.set_state(Booking.wait_for_date1)
    b = InlineKeyboardBuilder()
    b.button(text="Назад 🔙", callback_data="back_name")
    b.button(text="На главную 🏡", callback_data="start_menu")
    b.adjust(2)
    await message.answer("Дата заезда? Формат: ДД.ММ.ГГГГ", reply_markup=b.as_markup())


@client_router.callback_query(F.data == "back_name")
async def back_name(cb: CallbackQuery, state: FSMContext):
    await state.set_state(Booking.wait_for_name)
    await cb.message.answer("Как вас зовут? Введите полное ФИО")
    await cb.answer()



@client_router.message(Booking.wait_for_date1, F.text)
async def got_date_from(message: Message, state: FSMContext):
    d = parse_date(message.text)
    if not d:
        await message.answer("Не понял дату. Пример: 05.09.2025")
        return
    if d < date.today():
        await message.answer("Дата заезда не может быть в прошлом. Введите другую дату.")
        return

    await state.update_data(date_from=d.isoformat())
    await state.set_state(Booking.wait_for_date2)

    b = InlineKeyboardBuilder()
    b.button(text="Назад 🔙", callback_data="back_name")
    b.button(text="На главную 🏡", callback_data="start_menu")
    b.adjust(2)
    await message.answer("Дата выезда? Формат: ДД.ММ.ГГГГ", reply_markup=b.as_markup())


@client_router.callback_query(F.data == "back_dates_from")
async def back_dates_from(cb: CallbackQuery, state: FSMContext):
    await state.set_state(Booking.wait_for_date1)
    b = InlineKeyboardBuilder()
    b.button(text="Назад 🔙", callback_data="back_name")
    b.button(text="На главную 🏡", callback_data="start_menu")
    b.adjust(2)
    await cb.message.answer("Дата заезда? Формат: ДД.ММ.ГГГГ", reply_markup=b.as_markup())
    await cb.answer()



@client_router.message(Booking.wait_for_date2, F.text)
async def got_date_to(message: Message, state: FSMContext):
    d_to = parse_date(message.text)
    if not d_to:
        await message.answer("Не понял дату. Пример: 12.09.2025")
        return

    data = await state.get_data()
    iso_from = data.get("date_from")
    if not iso_from:
        await message.answer("Не вижу дату заезда. Начните заново: /order")
        await state.clear()
        return

    d_from = datetime.fromisoformat(iso_from).date()
    if d_to <= d_from:
        await message.answer("Дата выезда должна быть ПОСЛЕ даты заезда. Попробуйте ещё раз.")
        return

    await state.update_data(date_to=d_to.isoformat())
    await state.update_data(rooms=[])  
    await state.set_state(Booking.wait_for_rooms)

    await message.answer("Выберите комнаты (можно несколько):", reply_markup=build_rooms_kb([]))


@client_router.callback_query(F.data == "back_dates_to")
async def back_dates_to(cb: CallbackQuery, state: FSMContext):
    await state.set_state(Booking.wait_for_date2)
    b = InlineKeyboardBuilder()
    b.button(text="Назад 🔙", callback_data="back_dates_from")
    b.button(text="На главную 🏡", callback_data="start_menu")
    b.adjust(2)
    await cb.message.answer("Дата выезда? Формат: ДД.ММ.ГГГГ", reply_markup=b.as_markup())
    await cb.answer()



@client_router.callback_query(Booking.wait_for_rooms, F.data.startswith("toggle_room:"))
async def toggle_room(cb: CallbackQuery, state: FSMContext):
    room = cb.data.split(":", 1)[1]
    data = await state.get_data()
    selected = data.get("rooms", [])
    if not isinstance(selected, list):
        selected = []

    if room in selected:
        selected.remove(room)
    else:
        selected.append(room)

    await state.update_data(rooms=selected)

    
    try:
        await cb.message.edit_text(
            f"Выберите комнаты (можно несколько):\n\nВыбрано: {', '.join(selected) if selected else 'ничего'}",
            reply_markup=build_rooms_kb(selected)
        )
    except Exception:
        
        await cb.message.answer(
            f"Выберите комнаты (можно несколько):\n\nВыбрано: {', '.join(selected) if selected else 'ничего'}",
            reply_markup=build_rooms_kb(selected)
        )
    await cb.answer()


@client_router.callback_query(Booking.wait_for_rooms, F.data == "rooms_done" or F.data == "rooms_done")
async def rooms_done(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    rooms = data.get("rooms", [])
    if not rooms:
        await cb.answer("Выберите хотя бы одну комнату.", show_alert=True)
        return

    
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="📱 Отправить номер телефона", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await cb.message.answer(f"✅ Выбрано комнат: {', '.join(rooms)}\n\nТеперь отправьте номер телефона, пожалуйста.", reply_markup=kb)
    await state.set_state(Booking.wait_for_phone)
    await cb.answer()



@client_router.message(Booking.wait_for_phone, F.contact)
async def got_contact(msg: Message, state: FSMContext):
    phone = msg.contact.phone_number
    await state.update_data(phone=phone)
    await msg.answer(f"✅ Спасибо! Ваш номер: {phone}", reply_markup=ReplyKeyboardRemove())

    
    await state.set_state(Booking.wait_for_confirm)
    data = await state.get_data()
    await msg.answer(
        "📌 Проверьте данные:\n"
        f"Имя: {data.get('name')}\n"
        f"Заезд: {data.get('date_from')}\n"
        f"Выезд: {data.get('date_to')}\n"
        f"Комнаты: {', '.join(data.get('rooms', []))}\n"
        f"Телефон: {data.get('phone')}\n\n"
        "Подтвердить бронь?",
        reply_markup=InlineKeyboardBuilder()
            .button(text="✅ Подтвердить", callback_data="confirm:yes")
            .button(text="❌ Отмена", callback_data="confirm:no")
            .adjust(2)
            .as_markup()
    )



@client_router.message(Booking.wait_for_phone, F.text)
async def got_phone_text(msg: Message, state: FSMContext):
    # простая валидация, поддерживающая +7... или 10 цифр
    txt = msg.text.strip()
    if not (txt.startswith("+") and len(txt) >= 10) and not txt.isdigit():
        await msg.answer("Пожалуйста, используйте кнопку '📱 Отправить номер телефона' или введите корректный номер.")
        return
    await state.update_data(phone=txt)
    await got_contact(msg, state)  



@client_router.callback_query(Booking.wait_for_confirm, F.data == "confirm:yes")
async def confirm_booking(cb: CallbackQuery, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    d_from = date.fromisoformat(data["date_from"])
    d_to = date.fromisoformat(data["date_to"])
    rooms = data.get("rooms", [])
    phone = data.get("phone")
    name = data.get("name")

    busy = []
    free = []
    for r in rooms:
        if await is_room_free(session, r, d_from, d_to):
            free.append(r)
        else:
            busy.append(r)

    if busy:
        
        await cb.message.answer("⚠️ К сожалению, эти комнаты заняты: " + ", ".join(busy) +
                                "\nПожалуйста, выберите другие комнаты или измените даты.")
        await state.set_state(Booking.wait_for_rooms)
        await cb.message.answer("Выберите комнаты (можно несколько):", reply_markup=build_rooms_kb(data.get("rooms", [])))
        await cb.answer()
        return

    
    for r in free:
        order = Order(
            name=name,
            phone=phone,
            date_from=d_from,
            date_to=d_to,
            room=r
        )
        session.add(order)
    await session.commit()

    b = InlineKeyboardBuilder()
    b.button(text="Вернуться в главное меню 🏡", callback_data="start_menu")
    b.adjust(1)  

    await cb.message.answer(
        "✅ Бронь успешно оформлена! Мы свяжемся с вами.",
        reply_markup=b.as_markup()
    )
    await state.clear()
    await cb.answer()


@client_router.callback_query(Booking.wait_for_confirm, F.data == "confirm:no")
async def cancel_booking(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("Отменено. Если хотите начать сначала — /order")
    await state.clear()
    await cb.answer()





    
    
    

