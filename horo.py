import os
import telebot
import schedule
import time
from openai import OpenAI
from datetime import datetime

AI_TEXT_MODEL = 'chatgpt-4o-latest'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@horo_ai'

def job(sign, symbol,CHAT_ID=CHAT_ID):
    today = datetime.today().strftime('%Y-%m-%d')
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный астролог" },
            { "role": "user", "content": f"Составь гороскоп на {today} для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    text = f"""{symbol} **{sign} {today}** {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    schedule.every().day.at("08:00",'Europe/Moscow').do(job, sign="Рыбы", symbol='♓',CHAT_ID='@pisces_the')
    schedule.every().day.at("08:01",'Europe/Moscow').do(job, sign="Овен", symbol='♈')
    schedule.every().day.at("08:02",'Europe/Moscow').do(job, sign="Телец", symbol='♉')
    schedule.every().day.at("08:03",'Europe/Moscow').do(job, sign="Близнецы", symbol='♊')
    schedule.every().day.at("08:04",'Europe/Moscow').do(job, sign="Рак", symbol='♋')
    schedule.every().day.at("08:05",'Europe/Moscow').do(job, sign="Лев", symbol='♌')
    schedule.every().day.at("08:06",'Europe/Moscow').do(job, sign="Дева", symbol='♍')
    schedule.every().day.at("08:07",'Europe/Moscow').do(job, sign="Весы", symbol='♎')
    schedule.every().day.at("08:08",'Europe/Moscow').do(job, sign="Скорпион", symbol='♏')
    schedule.every().day.at("08:09",'Europe/Moscow').do(job, sign="Стрелец", symbol='♐')
    schedule.every().day.at("08:10",'Europe/Moscow').do(job, sign="Козерог", symbol='♑',CHAT_ID='@capricorn_the')
    schedule.every().day.at("08:11",'Europe/Moscow').do(job, sign="Водолей", symbol='♒')

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
