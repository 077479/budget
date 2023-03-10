import src.utility, data.globals

# [X]

def run(message_obj):

    try:
        src.utility.message_custom(data.globals.help)
    
    except Exception as e:
        src.utility.log_it("while getting out the help msg out an exception occured")
        src.utility.log_it(f"{e}")
        src.utility.log_write()
        src.utility.lock_set(False)