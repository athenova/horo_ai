import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@horo_ai'

def job(sign):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный астролог" },
            { "role": "user", "content": f"Составь гороскоп на сегодня для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

schedule.every().day.at("08:00",'Europe/Moscow').do(job, sign="Рыбы")
#schedule.every().day.at("08:01",'Europe/Moscow').do(job, sign="Овен")
#schedule.every().day.at("08:02",'Europe/Moscow').do(job, sign="Телец")
#schedule.every().day.at("08:03",'Europe/Moscow').do(job, sign="Близнецы")
#schedule.every().day.at("08:04",'Europe/Moscow').do(job, sign="Рак")
#schedule.every().day.at("08:05",'Europe/Moscow').do(job, sign="Лев")
#schedule.every().day.at("08:06",'Europe/Moscow').do(job, sign="Дева")
#schedule.every().day.at("08:07",'Europe/Moscow').do(job, sign="Весы")
#schedule.every().day.at("08:08",'Europe/Moscow').do(job, sign="Скорпион")
#schedule.every().day.at("08:09",'Europe/Moscow').do(job, sign="Стрелец")
#schedule.every().day.at("08:10",'Europe/Moscow').do(job, sign="Козерог")
#schedule.every().day.at("08:11",'Europe/Moscow').do(job, sign="Водолей")

fifteen_minutes = 15 * 60

for i in range(fifteen_minutes):
    schedule.run_pending()
    time.sleep(1)
