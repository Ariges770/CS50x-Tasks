from curses.ascii import isdigit
import os
import requests
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, makeTransaction

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Retrieve all users current holdings
    holdings = db.execute("SELECT * FROM stock_positions WHERE person_id = ?", session["user_id"])
    # Declare listings list and assign market value 
    listings = []
    market_value = 0
    for stock in holdings:
        # Get info from lookup and add all table values to dict
        info = lookup(stock["ticker"])
        stock["ticker"] = {
            "name": info["name"],
            "ticker": stock["ticker"],
            "price": info["price"],
            "total_shares": stock["shares_owned"],
            "total_price": info["price"] * stock["shares_owned"]
        }
        # Add up each stocks total price for a grand total calculation
        market_value += stock["ticker"]["total_price"]
        listings.append(stock["ticker"])

    # Create a dict of total counts and values
    totals = {
        "names": db.execute("SELECT COUNT(ticker) AS total FROM stock_positions WHERE person_id = ?", session["user_id"])[0]["total"],
        "shares": db.execute("SELECT SUM(shares_owned) AS total FROM stock_positions WHERE person_id = ?", session["user_id"])[0]["total"],
        "value": market_value + db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"],
        "cash": db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    }
    return render_template("index.html", listings=listings, totals=totals)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Save Ticker and Shares count input
        ticker = request.form.get("symbol")
        amount = request.form.get("shares")
        # Ensure ticker value is entered and exists
        if not ticker or not lookup(ticker):
            return apology("Please Enter Valid Ticker", code="400")
        # Ensure user inputs a numerical amount of shares
        if not amount or not amount.isdigit() or float(amount) <= 0:
            return apology("Only Whole Numbers Accepted", code="400")

        # Make transaction
        error_code = makeTransaction(db, "buy", ticker, amount, session["user_id"])
        if error_code:
            return error_code

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    # Set transactions to the purchase_history table
    transactions = db.execute(
        """SELECT * 
        FROM purchase_history 
        WHERE person_id = ? 
        ORDER BY year DESC, 
        month DESC, 
        day DESC, 
        hour DESC, 
        minute DESC""", 
        session["user_id"])
        
    """Show history of transactions"""
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Save ticker
        ticker = request.form.get("symbol")
        # Save the JSON from API response
        stockInfo = lookup(ticker)
        if stockInfo is None:
            return apology("Stock Not Found", code="400")
        stockInfo["price"] = usd(stockInfo["price"])
        # Provide API response to rendered html 
        return render_template("quoted.html", stockInfo=stockInfo)
    else: 
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    username = request.form.get("username")
    password = request.form.get("password")
    # If user submitted register form
    if request.method == "POST":
        # Ensure Username contains some value
        if not username:
            return apology("Enter Username", code="400")
        # Ensure username is not taken
        if db.execute("SELECT * FROM users WHERE username = ?", username):
            return apology("Username Taken", code="400")
        # Ensure password was submitted
        if not password:
            return apology("Enter Password", code="400")
        # Ensure user validates password
        if not request.form.get("confirmation"):
            return apology("Confirm Password", code="400")
        # Compare password with validation
        if not password == request.form.get("confirmation"):
            return apology("Recheck Password", code="400")

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", username, generate_password_hash(password))

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Save Ticker and Shares count input
        ticker = request.form.get("symbol")
        amount = request.form.get("shares")
        # Ensure ticker value is entered and exists
        if not ticker or not lookup(ticker):
            return apology("Please Enter Valid Ticker", code="400")
        # Ensure user inputs a numerical amount of shares
        if not amount or int(amount) <= 0:
            return apology("Only Whole Numbers Accepted", code="400")
        # Make transaction
        error_code = makeTransaction(db, "sell", ticker, amount, session["user_id"])
        if error_code:
            return error_code
        return redirect("/")
    else:
        # Select all owned stock tickers
        stocks_owned = db.execute("SELECT ticker, shares_owned FROM stock_positions WHERE person_id = ?", session["user_id"])
        return render_template("sell.html", stocks_owned=stocks_owned)