from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Bot tokeningizni o'rnating
BOT_TOKEN = "BOTFATHERDAN OLINGAN TOKEN"

# /start uchun funksiya
def start(update: Update, context: CallbackContext):
    # WebApp tugmasini yaratamiz
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("WebAppni ochish", url="https://test-two-rho-48.vercel.app/")]
    ])
    
    # Tugmani foydalanuvchiga yuborish
    update.message.reply_text(
        "Salom! WebApp sahifamizni ochish uchun quyidagi tugmani bosing:",
        reply_markup=keyboard
    )

# Botni ishga tushirish
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # /start buyrug'iga handler qo'shish
    dispatcher.add_handler(CommandHandler("start", start))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
