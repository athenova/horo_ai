from project import *
import schedule
import time




if __name__ == '__main__':
    tg = ProjectTelegram()
    vk = ProjectVk()

    def job(type, chat_id=None, group_id=None):
        tg.send(type=type, chat_id=chat_id)
        if group_id is not None:
            vk.send(type=type, group_id=group_id)

    schedule.every().day.at("20:00",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the', group_id='229837683')
    schedule.every().day.at("20:01",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the', group_id='229837854')
    schedule.every().day.at("20:02",'Europe/Moscow').do(job, type="taurus")
    schedule.every().day.at("20:03",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the', group_id='229837895')
    schedule.every().day.at("20:04",'Europe/Moscow').do(job, type="cancer")
    schedule.every().day.at("20:05",'Europe/Moscow').do(job, type="leo")
    schedule.every().day.at("20:06",'Europe/Moscow').do(job, type="virgo")
    schedule.every().day.at("20:07",'Europe/Moscow').do(job, type="libra")
    schedule.every().day.at("20:08",'Europe/Moscow').do(job, type="scorpio")
    schedule.every().day.at("20:09",'Europe/Moscow').do(job, type="sagittarius")
    schedule.every().day.at("20:10",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the', group_id='229837876')
    schedule.every().day.at("20:11",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the', group_id='229837930')

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
