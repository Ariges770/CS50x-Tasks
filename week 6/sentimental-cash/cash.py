from shelve import DbfilenameShelf
from cs50 import get_float

cash = {
    "change": -1,
    "coins": 0
}

def main():
    while (cash["change"] < 0):
        cash["change"] = get_float("How much change? ")
    
    change_amounts(0.25)
    change_amounts(0.10)
    change_amounts(0.05)
    change_amounts(0.01)

    print(round(cash["coins"]))

def change_amounts(coin_value):
    cash["coins"] += cash["change"] // coin_value
    cash["change"] = cash["change"] % coin_value

main()
