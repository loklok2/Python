class Person:
    def __init__(self, pid, pname, age):
        self.pid = pid
        self.pname = pname
        self.age = age
    
    def __str__(self):
        f"Person: {self.pid}, {self.pname}, {self.age}"


