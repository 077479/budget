import src.client, src.utility

# [X]

def run(message_obj):

    try:
        src.utility.log_it(f"'commands.clear' calling src.client.clear_chat")
        src.utility.log_write()
        src.client.clear_chat()
        src.utility.lock_set(False)
    
    except Exception as e:
        src.utility.log_it(f"'commands.clear' an exception occured during clearing the chat: {e}")
        src.utility.log_write()
        src.utility.lock_set(False)
