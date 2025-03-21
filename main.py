from decouple import config
from telegram import Update
from telegram.ext import Application , CommandHandler , ContextTypes , ConversationHandler, filters, MessageHandler

import jdatetime
import datetime

API_TOKEN = config("API_TOKEN")

async def start(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id= update.effective_chat.id,
        text= "به بات تاریخ دان حموم خوش آمدید",
    )

shamsi_date = jdatetime.datetime.now().strftime("%Y/%m/%d")
shamsi_month = jdatetime.datetime.now().strftime("%B")

async def shamsi_datetime(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f"تاریخ شمسی امروز: {shamsi_date} , ماه : {shamsi_month}"),   
    )

jalali_date = jdatetime.datetime.now()
gregorian_date = jalali_date.togregorian()
new_gregorian_date = gregorian_date - datetime.timedelta(days=17)
new_jalali_date = str(jdatetime.date.fromgregorian(date=new_gregorian_date))

hamoum_month = []

if(shamsi_month == 'Farvardin'):
    hamoum_month.append('Kheir')
if(shamsi_month == 'Ordibehesht'):
    hamoum_month.append('seda ghat')
if(shamsi_month == 'Khordad'):
    hamoum_month.append('Dousti')
if(shamsi_month == 'Tir'):
    hamoum_month.append('Barekat')
if(shamsi_month == 'Mordad'):
    hamoum_month.append('Zehniat')
if(shamsi_month == 'Shahrivar'):
    hamoum_month.append('Tagh')
if(shamsi_month == 'Mehr'):
    hamoum_month.append('Tavaghof')
if(shamsi_month == 'Aban'):
    hamoum_month.append('Samimiat')
if(shamsi_month == 'Azar'):
    hamoum_month.append('Maram o Marefat')
if(shamsi_month == 'Dey'):
    hamoum_month.append('Otagh')
if(shamsi_month == 'Bahman'):
    hamoum_month.append('Shafaat')
if(shamsi_month == 'Esfand'):
    hamoum_month.append('Viski')

async def hamoum_datetime(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f" {new_jalali_date} تاریخ حمومی امروز :ماه {hamoum_month} "),   
    )

def main():
    print("bot is running")
    
    # build api token
    app = Application.builder().token(API_TOKEN).build()

    app.add_handlers([
        CommandHandler("start", start),
        CommandHandler("shamsidate", shamsi_datetime),
        CommandHandler("hamoumdate", hamoum_datetime),
    ])

    print("bot is polling")
    app.run_polling()

if __name__ == "__main__":
    main()
