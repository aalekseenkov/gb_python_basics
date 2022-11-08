"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from dataclasses import dataclass
import logging

@dataclass
class TrafficLight:
    """TrafficLight docstring"""
    __color = ["red", "yellow", "green"]

    def __init__(self):
        self.__times = [7, 2, 10]

    def running(self):
        """running docstring"""
        try:
            for num, value in enumerate(self.__color):
                print(f"Switch on to : {value}")

                if num == 0:
                    sleep(self.__times[0])
                elif num == 1:
                    sleep(self.__times[1])
                else:
                    sleep(self.__times[2])

        except ValueError as err:
            logging.exception(err)

my_TrafficLight = TrafficLight()
my_TrafficLight.running()
