CREATE TABLE purchase_history (
    id INTEGER NOT NULL,
    year INTEGER NOT NULL, 
    month INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    hour INTEGER NOT NULL, 
    minute INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    ticker TEXT NOT NULL,
    shares INTEGER NOT NULL,
    share_price REAL,
    total_price REAL,
    total_cash_balance REAL,
    person_id INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(person_id) REFERENCES users(id)
);

CREATE TABLE stock_positions (
    id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    ticker TEXT NOT NULL,
    shares_owned INTEGER NOT NULL,
    market_value REAL,
    PRIMARY KEY(id),
    FOREIGN KEY(person_id) REFERENCES users(id)
);


INSERT INTO 
purchase_history (year, month, day, hour, minute, transaction_type, ticker, shares, share_price, total_price, total_cash_balance, person_id)
VALUES
(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)


INSERT INTO stock_positions (person_id, ticker, shares_owned, market_value) VALUES (2, "BABA", 10, 1000); 