import src.client, src.utility, src.config

# [X]

def run(message_obj):

    try:
        src.utility.log_it(f"stopping meintenance_thread and client")        
        src.config.value_set("MAINTENANCE", "thread_running", "no")
        src.utility.message_std()
        src.client.stop_bot()
    
    except Exception as e:
        src.utility.log_it("while stopping the client an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)