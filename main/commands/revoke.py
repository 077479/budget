import src.db, src.utility

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
        # [id, date, value, balance_id]
        last_charge = src.db.make_querry("chargeBalance_get_last")
        # [(id, date, value)]
        actual_balance = src.db.make_querry("balance_get_last")

        src.utility.log_it(f"'commands.revoke': last_charge: {str(last_charge)}, actual_balance: {actual_balance}")
        src.utility.log_it(f"making querry: 'balance_edit' and 'chargeBalance_remove_id'")

        if last_charge:
            src.db.make_querry("balance_edit", ((actual_balance[0][2] + last_charge[0][2]), actual_balance[0]))
            src.db.make_querry("chargeBalance_remove_id", (last_charge[0][0],))

            src.utility.message_std()        
        else:
            src.utility.message_custom("nothing to revoke")
    
    except Exception as e:
        # src.utility.log_it("while accessing the db in 'revoke.py' an exception occured")
        # src.utility.log_it(f"{e}")
        # src.utility.log_write()
        # src.utility.lock_set(False)
        print(e)