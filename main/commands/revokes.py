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
        last_charge = src.db.make_querry("chargeSpare_get_last")
        # [(id, date, value)]
        actual_spare = src.db.make_querry("Spare_get_last")

        src.utility.log_it(f"'commands.revokes': last_charge: {str(last_charge)}, actual_charge: {actual_spare}")
        src.utility.log_it(f"making querry: 'spare_edit' and 'chargeSpare_remove_id'")

        if last_charge:
            src.db.make_querry("spare_edit", ((actual_spare[0][2] + last_charge[0][2]), actual_spare[0]))
            src.db.make_querry("chargeSpare_remove_spare_id", (last_charge[0][0],))

            src.utility.message_std()        
        else:
            src.utility.message_custom("nothing to revoke")

    except Exception as e:
        src.utility.log_it("while accessing the db in 'revokes.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)