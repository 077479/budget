import src.utility, src.config, data.globals, src.db

# [X]

def run(message_obj):

    try:
        src.utility.log_it("writing current state to log")

        src.utility.log_it("ini")

        thread_running = src.config.value_get("MAINTENANCE", "thread_running")
        querry_location = src.config.value_get("MAINTENANCE", "querry_location")
        db_location = src.config.value_get("MAINTENANCE", "db_location")
        week_amount = src.config.value_get("MONEY", "week_amount")
        spare_amount = src.config.value_get("MONEY", "spare_amount")
        
        src.utility.log_it(f"\tini->thread_running: {thread_running}")
        src.utility.log_it(f"\tini->querries_location: {querry_location}")
        src.utility.log_it(f"\tini->db_location: {db_location}")
        src.utility.log_it(f"\tini->week_amount: {week_amount}")
        src.utility.log_it(f"\tini->spare_amount: {spare_amount}")

        src.utility.log_it("globals")

        lock_state = data.globals.lock
        maintenance_running = data.globals.maintenance_thread_running

        src.utility.log_it(f"\tglobals->lock: {lock_state}")
        src.utility.log_it(f"\tglobals->maintenance_running: {maintenance_running}")

        src.utility.log_it("db")

        actual_balance = src.db.make_querry("balance_get_last")
        actual_spare = src.db.make_querry("spare_get_last")

        src.utility.log_it(f"\tdb->balance: {actual_balance[0]}")
        src.utility.log_it(f"\tdb->spare: {actual_spare}")

        src.utility.log_write()
        src.utility.message_custom("state succesfully wrote to log")
    
    except Exception as e:
        src.utility.log_it(f"an exception occured in commands.state while logging the state: {e}")
        src.utility.log_write()