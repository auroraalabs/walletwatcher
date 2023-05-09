import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        address = request.form.get("address")
        action = request.form.get("action")

        if action == "add":
            with open("../telegram_bot/wallets.txt", "a") as f:
                f.write(f"{address}\n")
        elif action == "remove":
            with open("../telegram_bot/wallets.txt", "r") as f:
                addresses = f.readlines()
            
            with open("../telegram_bot/wallets.txt", "w") as f:
                for addr in addresses:
                    if addr.strip() != address:
                        f.write(addr)

    with open("../telegram_bot/wallets.txt", "r") as f:
        addresses = f.read().splitlines()

    return render_template("index.html", addresses=addresses)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('FLASK_PORT', 8080)))

