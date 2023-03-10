import commands, src.utility
import datetime

class Message:
    """
    class _
    
    ===== Attributes =====
    message: str
    expense_value: int
    is_expense: bool
    command: str
    date: int (timestamp)
    value_sparator: str

    
    ===== Methods =====
    None
    
    ===== Exceptions =====
    None
    """
    
    def __init__(self, message):
        self.message = str(message)
        self.expense_value = None
        self.command = None
        self.date = int(datetime.datetime.now().timestamp())

        self.set_is_saving_expense()
        self.set_value_sepatator()
        self.set_is_expense()
        
        if not self.command: self.command = self.message



    def set_is_saving_expense(self):
        
        if self.message[:2] == "s ":
            self.is_saving_expense = True
            self.message = self.message[2:]
            self.command = "expenses"
            return
        
        self.is_saving_expense = False           


    def set_value_sepatator(self):
        if "," in self.message:
            self.value_separator = ","
            return
        
        if "." in self.message:
            self.value_separator = "."
            return
        
        self.value_separator = None


    def set_is_expense(self):
        amount = self.message.replace(",", ".")

        
        if len(amount) >= 7:
            if amount[:8] == "spareadd": 
                amount = amount[9:]
                self.command = "spareadd"
            elif amount[:10] == "balanceadd":
                amount = amount[11:]
                self.command = "balanceadd"
            elif amount[:8] == "setspare":
                amount = amount[9:]
                self.command = "setspare"
            elif amount[:10] == "setbalance":
                amount = amount[11:]
                self.command = "setbalance"

        if self.value_separator:
            try:
                self.expense_value = int(round(float(amount)*100))
                self.is_expense = True
                if not self.command: self.command = "expense"
            except ValueError:
                self.is_expense = False
        else: 
            try:
                self.expense_value = int(round(float(amount)*100))
                self.is_expense = True
                if not self.command: self.command = "expense"                
            except ValueError:
                self.is_expense = False


    def __str__(self):
        return "new_message:" + \
            f"\n\tmessage: {self.message}" + \
            f"\n\tdate: {self.date}" + \
            f"\n\tis_expense: {self.is_expense}" + \
            f"\n\tis_saving_expense: {self.is_saving_expense}" + \
            f"\n\tvalue_separator: {self.value_separator}" + \
            f"\n\texpense_value: {self.expense_value}" + \
            f"\n\tcommand: {self.command}"


def parse_message(message_gathered):

    message_obj = Message(message_gathered)

    src.utility.log_it(f"'message.parse_message', message_obj: {str(message_obj)}")

    if hasattr(commands, message_obj.command):
        getattr(commands, message_obj.command).run(message_obj)
    
    else:
        src.utility.log_it(f"command not in commands module")
        src.utility.log_write()
        src.utility.lock_set(False)