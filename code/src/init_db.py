# init_db.py
import sqlite3

conn = sqlite3.connect("bank.db")
c = conn.cursor()

c.executescript("""
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    balance REAL,
    account_type TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    txn_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    amount REAL,
    txn_type TEXT,
    txn_date DATE,
    FOREIGN KEY(account_id) REFERENCES accounts(account_id)
);
""")

c.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
])

c.executemany("INSERT INTO accounts (customer_id, balance, account_type) VALUES (?, ?, ?)", [
    (1, 50000, "savings"),
    (2, 150000, "current"),
    (3, 75000, "savings"),
])

c.executemany("INSERT INTO transactions (account_id, amount, txn_type, txn_date) VALUES (?, ?, ?, ?)", [
    (1, 10000, "debit", "2025-08-01"),
    (1, 5000, "credit", "2025-08-10"),
    (2, 20000, "debit", "2025-08-15"),
    (3, 3000, "credit", "2025-08-20"),
])

conn.commit()
conn.close()
print("Database initialized ✅")
