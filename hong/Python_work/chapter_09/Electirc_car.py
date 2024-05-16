class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self, make, model, year, color):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"[{self.make},{self.model}]"
    
    def fill_gas_tank(self):
        print(f"this car doesn't have a gas tank!")

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year}{self.make}{self.model} \n{self.color}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    
my_new_car = Car('audi', 'a4', 2024, 'red')
print(my_new_car)#출력하기 위해서는 string이 필요> 객체를 str로 변환필요> __str__() 자동호출
print(my_new_car.get_descriptive_name())
my_new_car.color = 'blue'
print(my_new_car.get_descriptive_name())

class Battery:
    def __init__(self, battery_size=40):
        """배터리속성을 초기화"""
        self.battery_size = battery_size


class ElecticCar(Car):
    """슈퍼클래스의 subclass"""
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        self.battery = Battery() ##클래스 Battery의 생성자
    
    def fill_gas_tank(self):
        super().fill_gas_tank()
        print(f"전기차는 탱크 없음")

my_leaf = ElecticCar('nissan', 'leaf', 2024, 'red')
print(my_leaf.get_descriptive_name())