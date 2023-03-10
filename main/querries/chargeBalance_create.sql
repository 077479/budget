CREATE TABLE ChargeBalance (
    ChargeBalance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ChargeBalance_date INTEGER NOT NULL,
    ChargeBalance_value INTEGER NOT NULL,
    Balance_id INTEGER,
    FOREIGN KEY (Balance_id) REFERENCES Balance(Balance_id)
);