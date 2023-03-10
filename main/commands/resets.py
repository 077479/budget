import src.db, src.config, src.utility

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
        actual_spare = src.db.make_querry("spare_get_last")[0]
        new_spare = src.config.value_get("MONEY", "spare_amount")

        src.utility.log_it(f"'commands.resets': actual_spare: {str(actual_spare)}, new_spare: {str(new_spare)}")
        src.utility.log_it(f"making querry: 'chargeBalance_remove_spare_id' and 'spare_edit'")

        src.db.make_querry("chargeSpare_remove_spare_id", (actual_spare[0], ))
        src.db.make_querry("spare_edit", (new_spare, actual_spare[0]))

        src.utility.message_std()

    except Exception as e:
        src.utility.log_it("while accessing the db in 'resets.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)