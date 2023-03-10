import src.db, src.config, src.utility

# [ ]

def run(message_obj):
    """
    message_obj attributes:
        message: str
        expense_value: int // as cent amount
        is_expense: bool
        command: str
        date: int (timestamp)
        value_sparator: str
    """

    try:

        # [(id, date, value)]
        actual_balance = src.db.make_querry("balance_get_last")[0]
        new_balance = src.config.value_get("MONEY", "week_amount")

        src.utility.log_it(f"'commands.reset': actual_balance: {str(actual_balance)}, new_balance: {str(new_balance)}")
        src.utility.log_it(f"making querry: 'chargeBalance_remove_balance_id' and 'balance_edit'")

        src.db.make_querry("chargeBalance_remove_balance_id", (actual_balance[0], ))
        src.db.make_querry("balance_edit", (new_balance, actual_balance[0]))

        src.utility.message_std()

    except Exception as e:
        src.utility.log_it("while accessing the db in 'reset.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)