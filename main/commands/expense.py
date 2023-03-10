import src.db, src.config, src.utility

# [X]

def run(message_obj):
    """
    message_obj attributes:
        message: str
        expense_value: int // as cent amount
        is_expense: bool
        command: str
        date: int // as timestamp
        value_sparator: str
    """

    try:
        # [(id, date, value)]
        actual_balance = src.db.make_querry("balance_get_last")[0]

        src.utility.log_it(f"'commands.expense': actual_balance: {str(actual_balance)}")
        src.utility.log_it(f"making querry: 'balance_edit' and 'chargeBalance_add'")

        # value, id
        src.db.make_querry("balance_edit", (actual_balance[2] - message_obj.expense_value, actual_balance[0]))
        # date, value, id
        src.db.make_querry("chargeBalance_add", (message_obj.date, message_obj.expense_value, actual_balance[0]))

        src.utility.message_std()
    
    except Exception as e:
        src.utility.log_it("while accessing the db in 'expense.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)