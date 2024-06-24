from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


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