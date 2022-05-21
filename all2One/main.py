#!/usr/bin/env python3

import var as keys
from telegram.ext import *
import responses as R

print('Bot started....')
def start_command(update, context):
    # update.message.reply_text("Get started?")
    update.message.reply_text("Would you like to enter 'one' or 'more' seed phrase?")
    update.message.reply_text("You can import your seed phrases by saving them in seed.txt, one per line")

def help_command(update, context):
    update.message.reply_text("Need help?")
    update.message.reply_text("You can import your seed phrases by saving them in seed.txt, one per line")
    update.message.reply_text("Would you like to enter 'one' or 'more' seed phrase?")
    update.message.reply_text("Ensure to prepare your seed phrases in seed.txt and then in import them in the import options ")

def execute_command(update, context):
    update.message.reply_text("Get started?")
    update.message.reply_text("Would you like to enter 'one' or 'more' seed phrase?")
    update.message.reply_text("You can import your seed phrases by saving them in seed.txt, one per line")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response= R.userResponses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater= Updater(keys.API_KEY, use_context= True)
    dp= updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
