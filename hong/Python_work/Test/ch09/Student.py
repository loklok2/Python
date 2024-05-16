from Person import Person
from dept import Dept

class Student(Person):
    def __init__(self, pid, pname, age, syear, sdept):
        super().__init__(pid, pname, age)
        self.syear = syear
        self.sdept = sdept
dept = 

p1 = Person('1', 'p1', 20)
p2 = Person('2', 'p2', 21)
p3 = Person('3', 'p3', 22)
p4 = Person('4', 'p4', 23)
p5 = Person('5', 'p5', 24)

s1 = Student('6', 'S1', 25, 2021)
s2 = Student('7', 'S2', 25, 2021)
s3 = Student('8', 'S3', 25, 2021)
s4 = Student('9', 'S4', 25, 2021)
s5 = Student('10', 'S5', 25, 2021)

pList = [p1,p2,p3,p4,p5]
sList = [s1,s2,s3,s4,s5]

