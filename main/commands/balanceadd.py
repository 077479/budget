import src.db, src.utility, src.config

# [X]

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

        src.utility.log_it(f"'commands.balanceadd', actual_balance: {actual_balance}")
        
        # value, id
        src.utility.log_it(f"'commands.balanceadd' making querry to db: balance_edit")
        src.db.make_querry("balance_edit", (actual_balance[2] + message_obj.expense_value, actual_balance[0]))
        
        src.utility.message_std()
    
    except Exception as e:
        src.utility.log_it(f"an exception occured during blanceadd, exception: {e}")
        src.utility.log_write()
        src.utility.lock_set(False)