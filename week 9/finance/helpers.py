from datetime import datetime
import os
import tarfile
import requests
import urllib.parse

from cs50 import SQL
from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def makeTransaction(db, transaction_type, ticker, amount, user_id):
    # Set variables
    # Make amount an int
    amount = int(amount)
    # Get current time
    time = datetime.now()
    # Reformat the transaction type
    transaction_type = transaction_type.lower().capitalize()
    # Retrieve current share price
    share_price = lookup(ticker)["price"]
    # Calculate total share price
    total_price = amount * share_price
    # Check if user is buying or selling
    if transaction_type == "Buy":
        cash_balance = db.execute("SELECT * FROM users WHERE id = ?", user_id)[0]["cash"] - total_price
    if transaction_type == "Sell":
        cash_balance = db.execute("SELECT * FROM users WHERE id = ?", user_id)[0]["cash"] + total_price
        
        # Check if there are any holdings (for error handling)
        if not db.execute("SELECT shares_owned FROM stock_positions WHERE person_id = ? AND ticker = ?", user_id, ticker):
            return apology("Not Enough Shares To Sell", code="400")
            
        # Ensure user has enough shares to sell
        if amount > db.execute("SELECT shares_owned FROM stock_positions WHERE person_id = ? AND ticker = ?", user_id, ticker)[0]["shares_owned"]:
            return apology("Not Enough Shares To Sell", code="400")

    # Ensure user has positive balance
    if cash_balance < 0:
        return apology("Insufficient Funds", code="400")

    # Insert into purchase_history
    db.execute(
        '''
        INSERT INTO purchase_history (year, month, day, hour, minute, transaction_type, ticker, shares, share_price, total_price, total_cash_balance, person_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', time.year, time.month, time.day, time.hour, time.minute, transaction_type, ticker, amount, share_price, total_price, cash_balance, user_id)

    # Update users cash balance
    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_balance, user_id)

    # Update users holdings
    updatePositions(db, user_id, ticker, amount, share_price, transaction_type)
    return


def updatePositions(db, user_id, ticker, amount, share_price, transaction_type):
    # Set amount to negative (as user is decreasing shares)
    if transaction_type == "Sell":
        amount *= -1
    # Calculate total shares owned of stock
    historical_cost = 0
    shares_owned = 0
    for transaction in db.execute("SELECT * FROM purchase_history WHERE ticker = ?", ticker):
        if transaction["transaction_type"] == "Buy":
            shares_owned += transaction["shares"]
            historical_cost += transaction["shares"] * transaction["share_price"]
        if transaction["transaction_type"] == "Sell":
            shares_owned -= transaction["shares"]
            historical_cost -= transaction["shares"] * transaction["share_price"]
    # Update position by inserting, replacing or deleting balance
    if shares_owned == 0:
        db.execute("DELETE FROM stock_positions WHERE person_id = ? AND ticker = ?", user_id, ticker)
    else:
        db.execute('''
            INSERT OR REPLACE 
            INTO stock_positions (person_id, ticker, shares_owned, historical_cost) 
            VALUES (?, ?, ?, ?)
            ''', user_id, ticker, shares_owned, historical_cost)
    return