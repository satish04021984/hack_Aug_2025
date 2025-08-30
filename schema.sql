
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL NOT NULL DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT
);

-- Initial data for demonstration
INSERT OR IGNORE INTO customers (customer_id, first_name, last_name, email, phone) VALUES
(1, 'Alice', 'Smith', 'alice.smith@example.com', '555-1234'),
(2, 'Bob', 'Johnson', 'bob.johnson@example.com', '555-5678');

INSERT OR IGNORE INTO accounts (account_id, customer_id, account_type, balance) VALUES
(101, 1, 'savings', 1500.00),
(102, 1, 'checking', 500.00),
(103, 2, 'savings', 2500.00);

INSERT OR IGNORE INTO transactions (transaction_id, account_id, transaction_type, amount, description) VALUES
(1001, 101, 'deposit', 200.00, 'Online transfer'),
(1002, 102, 'withdrawal', 50.00, 'ATM withdrawal'),
(1003, 101, 'interest', 15.00, 'Monthly interest');
