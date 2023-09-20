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

async def variz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   mojaz=[-907940574,-950928313,-907799310,-90321337,-96743383,-947681902,-1001431838651]
   chatid=update.message.chat.id
   if chatid in mojaz :
    args=context.args
    chatid=update.message.chat.id
    data={"chatid":chatid,"amount":args[0],"cancel":"0"}
    requests.post("http://ir.asmantarh.ir:5000/variz/",data=data,allow_redirects=False)
    #await update.message.reply_html(text="done!")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   mojaz=[5945775325,]
   fromid=update.message.from.id
   if fromid in mojaz :  
    # args=context.args
    # chatid=update.message.chat.id
    # data={"chatid":chatid,"amount":args[0],"cancel":"1"}
    # requests.post("http://ir.asmantarh.ir:5000/variz/",data=data,allow_redirects=False)
    await update.message.reply_html(text="cancel Done!")


async def bot_tele(text):
    # Create application
    application = (
        Application.builder().token(getenv("TOKEN")).build()
    )

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("variz", variz))
    application.add_handler(CommandHandler("cancel", cancel))

    # Start application
    await application.bot.set_webhook(url=getenv("webhook"))
    await application.update_queue.put(
            Update.de_json(data=text, bot=application.bot)
        )
    async with application:
        await application.start()
        await application.stop()
