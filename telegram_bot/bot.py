import os
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
ALCHEMY_WEBHOOK_URL = os.environ.get('ALCHEMY_WEBHOOK_URL')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the Wallet Monitor Bot!')

def watch_transactions():
    while True:
        with open('wallets.txt', 'r') as f:
            wallet_addresses = f.read().splitlines()

        for address in wallet_addresses:
            url = f'{ALCHEMY_WEBHOOK_URL}{address}'
            response = requests.get(url)
            transactions = response.json()

            for tx in transactions:
                message = f'New transaction from {tx["from"]}\nAmount: {tx["value"]}\n'
                context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    watch_transactions()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

