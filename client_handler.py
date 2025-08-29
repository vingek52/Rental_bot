from datetime import datetime
from http import client
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import FSInputFile
from aiogram.types import InputMediaPhoto


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

#############################################################################################################################################################################################################################################################

@client_router.message(Command("start"))
async def start_menu(message: types.Message):
    await message.answer_photo(photo = "https://cdn2.divan.ru/img/v1/sf9i8YRoVw34ZNh4LXzWT7om6dloRy_sUaEK3_8MNps/rs:fit:1920:1440:0:0/g:ce:0:0/bg:ffffff/q:85/czM6Ly9kaXZhbi9ja2VkaXRvci93aWtpLWFydGljbGUvMjU3MC82M2M1NWQ5OTY3ODhiLmpwZw.jpg",
                               caption = "Привет, это бот для снятия жилья в моих хоромах, выбери раздел для просмотра", reply_markup=start_kb())
    await message.answer()


@client_router.callback_query(F.data == "start_menu")
async def start(callback: CallbackQuery):
    await callback.message.answer_photo(photo = "https://cdn2.divan.ru/img/v1/sf9i8YRoVw34ZNh4LXzWT7om6dloRy_sUaEK3_8MNps/rs:fit:1920:1440:0:0/g:ce:0:0/bg:ffffff/q:85/czM6Ly9kaXZhbi9ja2VkaXRvci93aWtpLWFydGljbGUvMjU3MC82M2M1NWQ5OTY3ODhiLmpwZw.jpg",
                            caption = "Привет, это бот для снятия жилья в моих хоромах, выбери раздел для просмотра", reply_markup=start_kb())
    await callback.answer()


@client_router.callback_query(F.data == "room1")
async def room1(callback: CallbackQuery):
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.aueoQ7a5xg6e6gQL8C4Cz8LhxAgW4kQG3ufEDBr2wgw.jpg"),
                    caption="<b>Комната 1</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 3х человек",
                        parse_mode=ParseMode.HTML),
                        InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.gKuFMba5LEKzmO5HiUOVg--TLkQ7kK5K85UuQDeEKEA.fLf5q_ir1PtTgS1SXeydRd3mDR5lN_QQeSA0sIpxaJw.jpg")),
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.sNglI7a5HDETit40SU2l8E-BHjebgp45U4ceM5eWGDM.L81i4I9NbvN6lglTGOZS7QyZ0JAF0z7a39J-I3m_HKg.jpg")), 
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.u-uuo7a5FwKYCtUH1PXcw8QBFQQQApUK2AcVABwWEwA.JyXDDJVA6NsjryvmTZ5wkr6zj6beni77b-qArGSA94Q.jpg"))]
    await callback.message.answer_media_group(media=media)
    await callback.message.answer("Выберете действие", reply_markup=go_order())
    await callback.answer()

@client_router.callback_query(F.data == "room2")
async def room2(callback: CallbackQuery):
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.WorLUra59mP9-zRm83sDz6Pw9GV183Rrvfb0YXnn8mE.jpg"), 
                             caption="<b>Комната 2</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 2х человек\nДиван расскладывается в большое двухместное спальное место", 
                             parse_mode=ParseMode.HTML), 
                             InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.2eC9T7a5dQmL5rcMg3iApdXtdw8D7vcBy-t3Cw_6cQs.nzp9R0Cfav5Y_OBDH5ynzqi696AXDsvaFcKbP-n37Q0.jpg")), 
                                                                         InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.L3lwora5g5BGC0GVIvoDURoAgZbOAwGYBgaBksIXh5I.gFEbS_DWbAFY2NVxn2R7mIZMsylfZBRNDheIgGdZ00I.jpg")), 
                                                                                         InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\dvor_room2.jpg"))]
    await callback.message.answer_media_group(media = media)
    await callback.message.answer("Выберете действие", reply_markup=go_order())
    await callback.answer()

@client_router.callback_query(F.data == "room3")
async def room3(callback: CallbackQuery):
    media = [InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.aueoQ7a5xg6e6gQL8C4Cz8LhxAgW4kQG3ufEDBr2wgw.jpg"),
                    caption="<b>Комната 3</b>\nКомната с собственным холодильником и душевой. \n Есть кондиционер и телевизор\n номер расчитан до 3х человек",
                        parse_mode=ParseMode.HTML),
                        InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.gKuFMba5LEKzmO5HiUOVg--TLkQ7kK5K85UuQDeEKEA.fLf5q_ir1PtTgS1SXeydRd3mDR5lN_QQeSA0sIpxaJw.jpg")),
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.sNglI7a5HDETit40SU2l8E-BHjebgp45U4ceM5eWGDM.L81i4I9NbvN6lglTGOZS7QyZ0JAF0z7a39J-I3m_HKg.jpg")), 
                            InputMediaPhoto(media=FSInputFile(r"C:\Projectori\Rental_bot\img\1.u-uuo7a5FwKYCtUH1PXcw8QBFQQQApUK2AcVABwWEwA.JyXDDJVA6NsjryvmTZ5wkr6zj6beni77b-qArGSA94Q.jpg"))]
    await callback.message.answer_media_group(media=media)
    await callback.message.answer("Выберете действие", reply_markup=go_order())
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
    wait_for_num = State()
    wait_for_name = State()
    wait_for_date1 = State()
    wait_for_date2 = State()
    wait_for_chooseroom = State()
    wait_for_confirm = State()



def come_menu():
    b = InlineKeyboardBuilder()
    b.button(text="Вернуться в главное меню 🏡", callback_data="start_menu")
    b.adjust(1)
    return b.as_markup()


def confirm_kb():
    b = InlineKeyboardBuilder()
    b.add(types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm:yes"))
    b.button(text="❌ Отмена", callback_data="confirm:no")
    b.adjust(2)
    return b.as_markup()





def rooms_kb():
    b = InlineKeyboardBuilder()
    b.button(text="Комната 1", callback_data="room:1")
    b.button(text="Комната 2", callback_data="room:2")
    b.button(text="Комната 3", callback_data="room:3")
    b.button(text="⬅️ Назад", callback_data="back:dates_to")
    b.adjust(1)
    return b.as_markup()    
    
@client_router.callback_query(F.data == "order_start")
async def start_order(cb: CallbackQuery, state: FSMContext): # type: ignore
    await state.set_state(Booking.wait_for_name)
    await cb.message.answer("Как вас зовут? Введите полное ФИО")
    await cb.answer()

@client_router.message(Booking.wait_for_name, F.text.len() > 1)
async def got_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text.strip())
    await state.set_state(Booking.wait_for_date1)
    await msg.answer("Дата заезда? Формат: ДД.ММ.ГГГГ")

def parse_date(s: str):
    try:
        return datetime.strptime(s.strip(), "%d.%m.%Y").date()
    except ValueError:
        return None

@client_router.message(Booking.wait_for_date1)
async def got_date_from(msg: Message, state: FSMContext):
    d = parse_date(msg.text)
    if not d:
        await msg.answer("Не понял дату. Пример: 05.09.2025")
        return
    await state.update_data(date_from=d.isoformat())
    await state.set_state(Booking.wait_for_date2)
    await msg.answer("Дата выезда? Формат: ДД.ММ.ГГГГ")




@client_router.message(Booking.wait_for_date2)
async def got_date_to(msg: Message, state: FSMContext):
    d_to = parse_date(msg.text)  # это дата выезда из ввода ДД.ММ.ГГГГ
    if not d_to:
        await msg.answer("Не понял дату. Пример: 12.09.2025")
        return

    data = await state.get_data()
    iso_from = data.get("date_from")
    if not iso_from:
        await msg.answer("Не вижу дату заезда. Начните заново: /order")
        await state.clear()
        return

    d_from = datetime.fromisoformat(iso_from).date()  # ← корректное чтение ISO

    if d_to <= d_from:
        await msg.answer("Дата выезда должна быть ПОСЛЕ даты заезда. Попробуйте ещё раз.")
        return

    await state.update_data(date_to=d_to.isoformat())
    await state.set_state(Booking.wait_for_chooseroom)
    await msg.answer("Выберите комнату:", reply_markup=rooms_kb())





@client_router.callback_query(Booking.wait_for_chooseroom, F.data.startswith("room:"))
async def choose_room(cb: CallbackQuery, state: FSMContext):
    room_id = cb.data.split(":")[1]
    await state.update_data(room = room_id)
    data = await state.get_data()

    text = (
        f"Проверьте данные:\n"
        f"Имя: {data.get('name')}\n"
        f"Заезд: {data.get('date_from')}\n"
        f"Выезд: {data.get('date_to')}\n"
        f"Комната: {data.get('room')}\n\n"
        f"Подтвердить?"
    )
    await state.set_state(Booking.wait_for_confirm)
    await cb.message.answer(text, reply_markup=confirm_kb())
    await cb.answer()

@client_router.callback_query(Booking.wait_for_confirm, F.data == "confirm:yes")
async def confirm(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    # здесь ты делаешь запись в БД/проверку доступности и т.п.
    await cb.message.answer("Бронь принята ✅\nМы свяжемся с вами.", reply_markup=come_menu())
    await state.clear()
    await cb.answer()


@client_router.callback_query(Booking.wait_for_confirm, F.data == "confirm:no")
async def not_confirm(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("Отменено. Если хотите начать сначала — /order", reply_markup=come_menu())
    await state.clear()
    await cb.answer()



    
    
    

