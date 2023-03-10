help = """balanceadd xx.XX: adds the amount to the actual balance

xx.XX: creates an expense in the db and subtract the amount from the actual balance

s xx.XX: creates an spare expense in the db and subtract the amount from the actual spare

reset: resets the actual week to zero expenses (will be lost forever) and sets the balance to default

resets: resets the actual week of spare charges to zero (will be lost forever) and sets the spare to default

revoke: revokes the last expense (will be lost forever)

revokes: revokes the last expense spare (will be lost forever)

spareadd xx.XX: adds the amount to the actual spare

state: writes the actual state with all vars and ledgers to the log

stop: stops the chat bot

week: shows all expenses made this week (WORK IN PROGRESS LOOK AT LOG AFTER COMMAND)"""

lock = False
log = None

maintenance_thread = None
maintenance_thread_running = True