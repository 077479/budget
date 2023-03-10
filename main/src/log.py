import data.globals
import datetime, pathlib

class Logger:
    
    def __init__(self):

        self.msg = ""

        log_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.msg += f"\n{'#'*4} {'-'*38} {'#'*4}\n"
        self.msg += f"{'#'*4} {'-'*8} {log_time} {'-'*9} {'#'*4}\n"
        self.msg += f"{'#'*4} {'-'*38} {'#'*4}"
    
    def add(self, msg):
        self.msg += f"\n\t{msg}"

    def write(self):

        log_location = pathlib.Path(__file__).parents[1] / "logs/actual.txt"
        if not log_location.exists(): log_location.touch()

        with open(log_location, "a") as open_file:
            open_file.write(self.msg)
        
        data.globals.log = None