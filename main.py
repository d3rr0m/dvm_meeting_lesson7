import ptbot
from pytimeparse import parse
from dotenv import dotenv_values

from render_progressbar import render_progressbar

CONFIG = dotenv_values('.env')


def set_timer(chat_id, request, bot):
    timer_secs = parse(request)
    if timer_secs is not None:
        message_id = bot.send_message(chat_id, f'Обратный отсчет стартует')
        bot.create_countdown(timer_secs, timer_notify_progress, chat_id=chat_id, message_id=message_id, total_secs=timer_secs, bot=bot)
        bot.create_timer(timer_secs, timer_notify, chat_id=chat_id, message='Время вышло', bot=bot)
    else:
        bot.send_message(chat_id, 'Было введено не корректное время.')


def timer_notify(message, chat_id, bot):
    bot.send_message(chat_id, message)


def timer_notify_progress(secs_left, chat_id, message_id, total_secs, bot):
    progress_bar = render_progressbar(total_secs, total_secs-secs_left, length=20)
    message = f'Осталось {secs_left} секунд\n{progress_bar}'
    bot.update_message(chat_id, message_id, message)


def main():
    bot = ptbot.Bot(CONFIG['TELEGRAM_TOKEN'])
    bot.reply_on_message(set_timer, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()