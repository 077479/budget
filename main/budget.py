import src.utility, data.globals, src.client, src.config
import threading

def main():
    src.utility.set_db_location()
    src.utility.set_querry_location()

    try:
        src.config.value_set("MAINTENANCE", "thread_running", "yes")
        data.globals.maintenance_thread = threading.Thread(target=src.utility.maintenance_thread)
        data.globals.maintenance_thread.start()
        src.client.run()

    except KeyboardInterrupt:
        src.config.value_set("MAINTENANCE", "thread_running", "no")
        src.client.stop_bot()

# ---------------- entry ------------------------------------------ #
if __name__ == "__main__":
    main()