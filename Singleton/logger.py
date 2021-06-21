class Logger():
    def __init__(self, file_name):
        self.file_name = file_name
    
    def log(self, level, msg):
        with open(self.file_name, "a") as file:
            file.write("[{0}]: {1}".format(level, msg))

    
    def critical(self, msg):
        self.log("CRITICAL", msg)
    
    def error(self, msg):
        self.log("ERROR", msg)
    
    def warning(self, msg):
        self.log("WARNING", msg)
    
    def debug(self, msg):
        self.log("DEBUG", msg)