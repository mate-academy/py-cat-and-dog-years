import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = 0
    earned_money = 0
    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"] is not None:
            earned_money += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            earned_money -= (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money * (-1)),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
