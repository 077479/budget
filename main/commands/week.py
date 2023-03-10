import src.db, src.utility
import datetime

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

        today = datetime.datetime.today()
        today = datetime.datetime(today.year, today.month, today.day)

        day_of_week = today.isocalendar().weekday - 1 # to get to monday

        monday = today - datetime.timedelta(days=day_of_week)
        sunday = monday + datetime.timedelta(days=7)

        src.utility.log_it(f"'commands.week': today: {str(today)}, monday: {str(monday)}, sunday: {str(sunday)}")
        src.utility.log_it(f"making querry: 'chargeBalance_get_week'")

        week_expenses = src.db.make_querry("chargeBalance_get_week", (monday.timestamp(), sunday.timestamp()))
        src.utility.log_it(str(week_expenses))

        src.utility.message_custom("NOT IMPLEMENTED YET, look at log")

    except Exception as e:
        src.utility.log_it("while accessing the db in 'week.py' an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)