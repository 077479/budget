CREATE TABLE ChargeSpare (
    ChargeSpare_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ChargeSpare_date INTEGER NOT NULL,
    ChargeSpare_value INTEGER NOT NULL,
    Spare_id INTEGER,
    FOREIGN KEY (Spare_id) REFERENCES Spare(Spare_id)
);