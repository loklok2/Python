class Dog:
    """클래스 Dog 정의"""
    def __init__(self, name, age):
        """클래스 Dog의 생성자"""
        self.name = name
        self.age = age
        self.city = "busan"
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

myDog = Dog("hong", 10)
myDog.sit()