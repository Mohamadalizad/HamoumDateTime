"""
this is just a project for fun,

in our class we have a so called "kingdom" called hamoum, which basically means bathroom.

This is a bot for Hamoum's calender which is based on the shamsi (Jalali) calender
"""
from decouple import config
from telegram import Update
from telegram.ext import Application , CommandHandler , ContextTypes
import jdatetime
import datetime

API_TOKEN = config("API_TOKEN")

def english_num_to_persian_num(n: str):
    table = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    return n.translate(table)

def get_shamsi_date():
    return jdatetime.datetime.now().strftime("%Y/%m/%d")
    
def get_shamsi_month():
    month =  jdatetime.datetime.now().strftime("%B")

    mapping = {
        'Farvardin': 'فروردین',
        'Ordibehesht': 'اردیبهشت',
        'Khordad': 'خرداد',
        'Tir': 'تیر',
        'Mordad': 'مرداد',
        'Shahrivar': 'شهریور',
        'Mehr': 'مهر',
        'Aban': 'ابان',
        'Azar': 'اذر',
        'Dey': 'دی',
        'Bahman': 'بهمن',
        'Esfand': 'اسفند'
    }

    return mapping.get(month)

def get_hamoumi_month():
    
    mapping = {
        'Farvardin': 'خیر',
        'Ordibehesht': 'صداقت',
        'Khordad': 'دوستی',
        'Tir': 'برکت',
        'Mordad': 'ذهنیت',
        'Shahrivar': 'تق',
        'Mehr': 'توقف',
        'Aban': 'صمیمیت',
        'Azar': 'مرام و معرفت',
        'Dey': 'اتاق',
        'Bahman': 'شفاعت',
        'Esfand': 'ویسکی'
    }

    # based on the explanations provided to me, hamoumi time is just shamsi time - 17 days, not caring about leap years as well, so lets implement that part

    j_date = jdatetime.datetime.now()

    h_date = j_date - jdatetime.timedelta(days=17)

    j_month_minus_13 = h_date.strftime("%B")

    return mapping.get(j_month_minus_13)


jalali_date = jdatetime.datetime.now()

gregorian_date = jalali_date.togregorian()

new_gregorian_date = jalali_date - datetime.timedelta(days=18)

new_jalali_date = str(jdatetime.date.fromgregorian(date=new_gregorian_date))

async def start(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "به بات تاریخ دان حمام خوش امدید"
    )

async def shamsi_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        f"تاریخ: {english_num_to_persian_num(get_shamsi_date())} ماه: {get_shamsi_month()}"
    )

async def air_hijri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f"تاریخ: {english_num_to_persian_num(new_gregorian_date.strftime('%Y/%m/%d'))} ماه: {get_hamoumi_month()}"), 
    )

def main():
    print("bot is running")
    
    # build api token
    app = Application.builder().token(API_TOKEN).build()

    app.add_handlers([
        CommandHandler("start", start),
        CommandHandler("shamsi_date", shamsi_date),
        CommandHandler("air_hijri", air_hijri),
    ])

    print("bot is polling")
    app.run_polling()

if __name__ == "__main__":
    main()
