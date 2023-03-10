import src.utility, src.config

# [X]

def run(message_obj):
    try:
        src.utility.log_it(f"setting the monthly spare amount to {str(message_obj.expense_value)}")
        src.config.value_set("MONEY", "spare_amount", str(message_obj.expense_value))
        src.utility.message_custom(f"monthly amount set to {round(message_obj.expense_value/100):.2f}")

    except Exception as e:
        src.utility.log_it("while setting the weekly spare amount an exception ocurred:")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)