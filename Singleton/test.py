from Single_logger import SingletonObject 
FILE = "logs.txt"

obj1 = SingletonObject()
obj1.file_name = FILE
print(obj1, id(obj1))
obj2 = SingletonObject()
print(obj2, id(obj2))

obj1.critical("message")

