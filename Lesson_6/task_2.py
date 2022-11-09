"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
from dataclasses import dataclass

@dataclass
class Road:
    """ Roadway class """
    # specific gravity of 1 sq.m of roadway with a thickness of 1 cm (tons)
    # _surface_spec_gravity: float = 0.05

    def __init__(self, length: [int, float], width: [int, float]):
        """
        :param length: the length of the roadway in meters
        :param width: the width of the roadway in meters
        """
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float, surface_spec_gravity: float) -> [float, None]:
        """ Calculation of the mass of the roadway of a given thickness
        :param thickness: the thickness of the road surface in centimeters
        :return: the mass of the roadway in tons if everything is OK, otherwise None
        """
        try:
            return (self._length * self._width
                    * thickness * surface_spec_gravity)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 20)
        print(
            'The mass of the road surface will be:',
            road.get_surface_gravity(25, 0.05),
            'kilograms'
        )
    except TypeError:
        print('Road Class should has 2 positional arguments')
