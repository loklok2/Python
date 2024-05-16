class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self, make, model, year, color):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year}{self.make}{self.model} \n{self.color}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    
my_new_car = Car('audi', 'a4', 2024, 'red')
print(my_new_car.get_descriptive_name())
my_new_car.color = 'blue'
print(my_new_car.get_descriptive_name())
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()