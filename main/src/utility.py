import src.config, src.db, src.client, data.globals, src.log
import time, pathlib, datetime

def maintenance_thread():
    log_it("starting maintenance thread")
    log_write()

    while True:
        if not src.config.value_get("MAINTENANCE", "thread_running") == "yes":
            exit(0)

        current_time = time.localtime()

        if current_time.tm_wday == 0 and current_time.tm_hour == 0 and current_time.tm_min == 0 :
            log_it("maintenance_thread here: adding weekly amount to balance")
            log_write()
            
            # [(id, date, value)]
            actual_balance = src.db.make_querry("balance_get_last")[0]
            new_balance = actual_balance[2] + src.config.value_get("MONEY", "week_amount")
            # date, value
            now = datetime.datetime.now().timestamp()
            src.db.make_querry("balance_add", (now, new_balance))            
            
        if current_time.tm_mday == 1 and current_time.tm_hour == 0 and current_time.tm_min == 0 :
            log_it("maintenance_thread here: adding monthly amount to spare")
            log_write()

            # [(id, date, value)]
            actual_spare = src.db.make_querry("spare_get_last")[0]
            new_spare = actual_spare[2] + src.config.value_get("MONEY", "spare_amount")
            # date, value
            now = datetime.datetime.now().timestamp()
            src.db.make_querry("spare_add", (now, new_spare))
        
        if current_time.tm_hour == 0 and current_time.tm_min == 0:
            log_it("maintenance_thread here: just casually reporting activeness")
            log_write()

        time.sleep(60)

def set_db_location():
    db_path = str(pathlib.Path(__file__).parents[1] / "data/budget.db")
    src.config.value_set("MAINTENANCE", "DB_location", db_path)

def set_querry_location():
    location = str(pathlib.Path(__file__).parents[1] / "querries")
    src.config.value_set("MAINTENANCE", "querry_location", location)

def message_std():
    #[(id, date, value)]
    actual_spare = src.db.make_querry("spare_get_last")[0]
    actual_balance = src.db.make_querry("balance_get_last")[0]

    spare = f"{(float(actual_spare[2]) / 100):.2f}"
    balance = f"{(float(actual_balance[2]) / 100):.2f}"

    msg = f"savings: {spare}\nbalance: {balance}\nfor help type 'help'"

    log_it("clearing chat and sending msg:")
    log_it(f"{msg}")

    src.client.clear_chat()
    src.client.send_message(msg)

def message_custom(custom_msg):
    
    #[(id, date, value)]
    actual_spare = src.db.make_querry("spare_get_last")[0]
    actual_balance = src.db.make_querry("balance_get_last")[0]

    spare = f"{(float(actual_spare[2]) / 100):.2f}"
    balance = f"{(float(actual_balance[2]) / 100):.2f}"

    msg = f"savings: {spare}\nbalance: {balance}\nfor help type 'help'"
    msg += f"\n{custom_msg}"


    log_it("clearing chat and sending msg:")
    log_it(f"{msg}")

    src.client.clear_chat()
    src.client.send_message(msg)


def log_it(msg):
    if not data.globals.log: data.globals.log = src.log.Logger()
    msg = msg.replace("\n", "\n\t")
    data.globals.log.add(f"{msg}\n")

def log_write():
    if data.globals.log:
        data.globals.log.write()
    else:
        data.globals.log = src.log.Logger()
        data.globals.log.add("maintenance was called to write the log but there is no log object")
        data.globals.log.write()

def lock_set(lock_state):
    data.globals.lock = lock_state

def lock():
    return data.globals.lock

def setup_db():
    date = datetime.datetime.now().timestamp()

    if not (pathlib.Path(__file__).parents[1] / "data/budget.db").exists():
        src.db.make_querry("balance_create")
        src.db.make_querry("spare_create")
        src.db.make_querry("chargeBalance_create")
        src.db.make_querry("chargeSpare_create")
    
    if not src.db.make_querry("balance_get_last"):        
        week_amount = src.config.value_get("MONEY", "week_amount")
        src.db.make_querry("balance_add", (date, week_amount))
    
    if not src.db.make_querry("spare_get_last"):
        spare_amount = src.config.value_get("MONEY", "spare_amount")
        src.db.make_querry("spare_add", (date, spare_amount))

