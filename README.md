# Wallet Monitor

A reusable project that monitors Ethereum wallet addresses for transactions and sends notifications via a Telegram bot. It also includes a Flask-based web interface for managing the list of wallet addresses.

## File Structure

wallet_monitor
│
├── run.py
│
├── telegram_bot
│ ├── bot.py
│ └── wallets.txt
│
└── flask_app
├── app.py
└── templates
└── index.html


## Configuration

The following environment variables are used to configure the project:

- `TELEGRAM_TOKEN`: The Telegram bot token obtained from the BotFather on Telegram.
- `ALCHEMY_WEBHOOK_URL`: The webhook URL obtained from your Alchemy account.
- `FLASK_PORT`: (Optional) The port on which the Flask app will run. Default is 8080.

## Usage

1. Install the required Python packages:

pip install python-telegram-bot requests Flask


2. Set the environment variables:

export TELEGRAM_TOKEN="your-telegram-bot-token"
export ALCHEMY_WEBHOOK_URL="your-alchemy-webhook-url"
export FLASK_PORT="8080" # Optional, default is 8080


3. Run the project:


This command will start both the Telegram bot and the Flask app concurrently. The Flask app will be accessible at `http://0.0.0.0:8080` or `http://localhost:8080`. You can open this URL in your browser to interact with the web interface, allowing you to add, remove, and display wallet addresses.

4. When the Flask app updates the `wallets.txt` file, you might need to restart the entire project using the `run.py` script to make sure the Telegram bot uses the updated list of wallet addresses.

