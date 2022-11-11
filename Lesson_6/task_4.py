"""
Задание 4.

Реализуйте базовый класс Car.
У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    """ Base Car Class Docstring """

    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False
    ):
        """
        :param color: car's color
        :param name: car's name
        :param is_police: is the car from police
        :param speed: car's speed
        """
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.speed = 0

        self._direction = ''

    def go(self, speed: float):
        """ starts moving of the car at given speed
        :param speed: speed of moving
        """
        try:
            self.speed = float(speed)
        except ValueError:
            print(f"'{speed}' is invalid speed")
            # pass

    def stop(self):
        """ stops the car """
        self.speed = 0

    def turn(self, direction: str):
        """ sets the direction of car's rotation
        :param direction: sets the direction of rotation ('left', 'right')
        """
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"Can't turn to '{direction}' in place")
            return

        self._direction = direction

    def show_speed(self):
        """ shows the current speed of the car """
        print(f'My speed is {self.speed} km/h')
        return self.speed

    @property
    def direction(self):
        """ show the current direction """
        return self._direction


class TownCar(Car):
    """ Класс городских автомобилей """

    # максимальная скорость движения
    def show_speed(self):
        """ shows the current speed of the car """
        print(f'My speed is {self.speed} km/h')
        _max_granted_speed = 60
        if self.speed > _max_granted_speed:
            print(f'!!! My granted speed is {_max_granted_speed} km/h !!!')
            print(
                f'!!! Over speed on {self.speed - _max_granted_speed} km/h !!!')
        return self.speed


class SportCar(Car):
    """ Класс спортивный автомобилей """
    # pass


class WorkCar(Car):
    """ Класс авто для работы """

    # максимальная скорость движения
    def show_speed(self):
        """ shows the current speed of the car """
        print(f'My speed is {self.speed} km/h')
        _max_granted_speed = 40
        if self.speed > _max_granted_speed:
            print(f'!!! My granted speed is {_max_granted_speed} km/h !!!')
            print(
                f'!!! Over speed on {self.speed - _max_granted_speed} km/h !!!')
        return self.speed


class PoliceCar(Car):
    """ Класс полицейского авто """

    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Yellow', 'Aston Martin Cygnet'): TownCar,
        ('Green', 'BMW M3'): SportCar,
        ('White', 'VAZ 2106'): WorkCar,
        ('Red', 'Ford Crown Victoria'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('#######################################')
        print(f"Car name '{car.name}'")
        print(f"Car color '{car.color}'")
        print(f"Car is police '{car.is_police}'")
        print(f"Car speed '{car.speed}'")
        print(f"Car direction '{car.direction}'")
        print(f"Car show speed '{car.show_speed()}'")

        car.turn('up')
        car.turn('left')
        car.go('somewhere')
        print("Car speed after invalid go", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Car direction '{car.direction}'")
        car.turn('right')
        print(f"Car direction '{car.direction}'")
        car.stop()
        car.show_speed()
        print('#######################################\n\n')
