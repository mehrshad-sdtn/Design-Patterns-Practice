class SingletonObject(object):
    class __Logger():
        def __init__(self):
            self.file_name = None
        
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
    
    instance = None
    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__Logger
        
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name) 

    def __str__(self):
        return id(self.instance)

        
    