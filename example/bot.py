from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import requests
from os import getenv

# Define a few command handlers.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="hello world!")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    res=requests.get("http://ir.asmantarh.ir:5000/variz/")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=res.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="DONE")
    await update.message.reply_html(text=res.text)

async def bot_tele(text):
    # Create application
    application = (
        Application.builder().token(getenv("TOKEN")).build()
    )

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    # Start application
    await application.bot.set_webhook(url=getenv("webhook"))
    await application.update_queue.put(
            Update.de_json(data=text, bot=application.bot)
        )
    async with application:
        await application.start()
        await application.stop()
