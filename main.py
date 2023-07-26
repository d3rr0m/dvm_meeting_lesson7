import ptbot
import random
from pytimeparse import parse
from dotenv import dotenv_values


CONFIG = dotenv_values('.env')

def wait(chat_id, question):
    bot.create_timer(5, reply, chat_id=chat_id, question=question)    


def set_timer(chat_id, request):
    timer_secs = parse(request)
    message_id = bot.send_message(chat_id, f'Обратный отсчет стартует')
    bot.create_countdown(timer_secs, notify_progress, chat_id=chat_id, message_id=message_id)
    bot.create_timer(timer_secs, timer_notify, chat_id=chat_id, message='Время вышло')


def timer_notify(message, chat_id):
    bot.send_message(chat_id, message)


def notify_progress(secs_left, chat_id, message_id):
    message = f'Осталось {secs_left} секунд'
    bot.update_message(chat_id, message_id, message)
    


def reply(chat_id, question):
    answers = ('Yes', 'No', 'Maybe')
    answer = random.choice(answers)
    print(f'пользователь с id {chat_id} написал {question}')
    bot.send_message(chat_id, f'''Какого хрена ты мне это написал? - {question}
                     Мой ответ - {answer}''')


def echo_reply(chat_id, message):
    bot.send_message(chat_id, message)

answers = ('Yes', 'No', 'Maybe')
answer = random.choice(answers)
bot = ptbot.Bot(CONFIG['TELEGRAM_TOKEN'])
#bot.send_message(CONFIG['TG_CHAT_ID'], f'Бот отвечает: {answer}')
#bot.reply_on_message(echo_reply)
bot.reply_on_message(set_timer)
bot.run_bot()
