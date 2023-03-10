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
        last_spare = src.db.make_querry("spare_get_last")[0]

        src.utility.log_it(f"'commands.spareadd': last_spare: {str(last_spare)}")
        src.utility.log_it(f"making querry: 'spare_edit'")

        src.db.make_querry("spare_edit", (last_spare[2] + message_obj.expense_value, last_spare[0]))

        src.utility.message_std()
    
    except Exception as e:
        src.utility.log_it("while accessing the db in 'spareadd.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)