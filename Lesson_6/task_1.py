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
from datetime import datetime as dt
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

@dataclass
class TrafficLight2:
    """TrafficLight2 docstring"""
    _states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        """running docstring"""
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"Leave state '{self._color}' after "
                  f"{(dt.now() - start_state_time).seconds} seconds")

print("Starting TrafficLight v1...")

tl = TrafficLight()
tl.running()

print()

print("Starting TrafficLight v2...")

tl_2 = TrafficLight2()
tl_2.running()
