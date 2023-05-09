import os
import sys
from dotenv import load_dotenv
from multiprocessing import Process

load_dotenv()

def run_telegram_bot():
    os.chdir('telegram_bot')
    os.system(f'{sys.executable} bot.py')

def run_flask_app():
    os.chdir('flask_app')
    os.system(f'{sys.executable} app.py')

if __name__ == '__main__':
    telegram_bot_process = Process(target=run_telegram_bot)
    flask_app_process = Process(target=run_flask_app)

    telegram_bot_process.start()
    flask_app_process.start()

    telegram_bot_process.join()
    flask_app_process.join()

