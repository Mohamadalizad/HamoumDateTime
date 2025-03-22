from decouple import config
from telegram import Update
from telegram.ext import Application , CommandHandler , ContextTypes
import jdatetime

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

    j_month_minus_17 = h_date.strftime("%B")

    return mapping.get(j_month_minus_17)

async def start(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "به بات تاریخ دان حمام خوش امدید"
    )

async def shamsi_month(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        f"این ماه {get_shamsi_month()} است"
    )

async def shamsi_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        f"{english_num_to_persian_num(get_shamsi_date())}"
    )

async def hamoumi_month(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        f"این ماه {get_hamoumi_month()} است"
    )

async def hamoumi_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...

def main():
    print("bot is running")
    
    # build api token
    app = Application.builder().token(API_TOKEN).build()

    app.add_handlers([
        CommandHandler("start", start),
        CommandHandler("shamsi_month", shamsi_month),
        CommandHandler("shamsi_date", shamsi_date),
        CommandHandler("hamoum_month", hamoumi_month),
        CommandHandler("hamoum_date", hamoumi_date),
    ])

    print("bot is polling")
    app.run_polling()

if __name__ == "__main__":
    main()
