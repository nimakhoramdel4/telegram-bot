import asyncio
from telegram import Bot
from datetime import datetime
from khayyam import JalaliDatetime
import schedule
import time
# اطلاعات ربات و کانال
TOKEN = "7831913940:AAECa-9ZQzy-ZkpPApXYcbTRUBYVwQ-a8hg"  # توکن ربات
CHAT_ID = "-1002327036935"  # آیدی کانال (مثلاً -1001234567890)

# شمارنده روز
start_date = datetime.now()

# تابع ارسال پیام به کانال
async def send_daily_message():
    global start_date

    # تاریخ شمسی امروز
    today_date = JalaliDatetime.now().strftime('%Y/%m/%d')

    # محاسبه تعداد روزهای گذشته
    now = datetime.now()
    day_counter = (now - start_date).days + 1

    # پیام ارسالی
    message = f"📅 تاریخ امروز: {today_date}\n🕒 {day_counter} روز گذشته است."

    # ارسال پیام به کانال
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"پیام ارسال شد: {message}")

# زمان‌بندی ارسال پیام (هر روز در ساعت 9 صبح)
def schedule_task():
    asyncio.run(send_daily_message())

schedule.every().day.at("11:40").do(schedule_task)

# اجرای برنامه
if __name__ == "__main__":
    print("ربات در حال اجرا است...")
    while True:
        schedule.run_pending()
        time.sleep(1)
