class MyClass:
    def __init__(self, x):
        self.x = x

    def __str__(self): #인스턴스를 문자열로 표현
        return f"MyClass object with x={self.x}"

    def __add__(self, other): # 덧셈 연산자 '+' 오버로딩
      return self.x + other.x

a = MyClass(1)
print(a)
a_description= a.__str__()
print(a_description)
b = MyClass(2)
print(a + b)