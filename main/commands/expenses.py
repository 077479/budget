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

        # [(id, date, value)]
        actual_spare = src.db.make_querry("Spare_get_last")[0]        

        src.utility.log_it(f"'commands.expenses': actual_spare: {str(actual_spare)}")
        src.utility.log_it(f"making querry: 'spare_edit' and 'chargeSpare_add'")

        # value, id
        src.db.make_querry("spare_edit", (actual_spare[2] - message_obj.expense_value, actual_spare[0]))
        src.db.make_querry("chargeSpare_add", (message_obj.date, message_obj.expense_value, actual_spare[0]))

        src.utility.message_std()

    except Exception as e:
        src.utility.log_it("while accessing the db in 'expenses.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)