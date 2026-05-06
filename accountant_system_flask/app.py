from flask import Flask, render_template
from get_path import get_path
from helpers.BalanceManager import BalanceManager
from helpers.StockManager import StockManager
from helpers.HistoryManager import HistoryManager

app = Flask(__name__)

balance_path = get_path("data/balance.txt")
balance_obj = BalanceManager(balance_path)

stock_path = get_path("data/stock.json")
stock_obj = StockManager(stock_path)

history_path = get_path("data/history.json")
history_obj = HistoryManager(history_path)


@app.route('/')
def home():
    balance_data = balance_obj.load_balance()
    stock_data = stock_obj.load_stock()
    return render_template(
        "main.html",
        amount=balance_data,
        stock=stock_data
    )


@app.route('/history/')
def history():
    history_data = history_obj.load_history()
    return render_template(
        "history.html",
        history=history_data
    )


@app.route('/history/<int:start>/<int:end>/')
def history_range(start, end):
    history_data = history_obj.load_history()

    total = len(history_data)

    if start < 1 or end > total or start > end:
        return render_template(
            "error.html",
            msg=f"Podano nieprawidłowy zakres. Dostępny zakres: 1 - {total}"
        )

    return render_template(
        "history.html",
        history=history_data[start - 1:end]
    )


if __name__ == "__main__":
    app.run(debug=True)
