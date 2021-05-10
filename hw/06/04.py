# 4. 
# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.  Создайте
# экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.

class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"New car: {self.name}, color {self.color}, police - {self.is_police}")

    def go(self):
        print(f'{self.name}: car is driving')

    def stop(self):
        print(f'{self.name}: car stopped')

    def turn(self, direction):
        print(f"{self.name}: car turned {direction}")

    def show_speed(self):
        print(f"{self.name}: car speed - {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}: car is going too fast - speed {self.speed}")
        else:
            print(f"{self.name}: car speed - {self.speed}")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}: car is going too fast - speed {self.speed}")
        else:
            print(f"{self.name}: car speed - {self.speed}")


class SpeedCar(Car):
    """Speed Car"""

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


my_car = TownCar(50, 'Grey', 'My Car', False)
my_car.go()
my_car.show_speed()

work_car = WorkCar(50, 'White', 'Work Car', False)
work_car.show_speed()

speed_car = SpeedCar(100, 'Red', 'Speed Car', False)
speed_car.turn('right')
print(speed_car.name)

police_car = PoliceCar(90, 'Blue', 'Police')
print(police_car.name)
police_car.go()
police_car.stop()
