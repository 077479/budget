import src.utility, time

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
        src.utility.log_it("'commands.msg: getting out the standard msg'")
        src.utility.message_std()
    
    except Exception as e:
        src.utility.log_it("while getting out the msg in 'msg.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)