"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
from dataclasses import dataclass


@dataclass
class Stationery:
    """ Stationery Class Docstring """
    # title: str = None

    def __init__(self):
        self.title = ''

    def draw(self):
        """ Draw Method Docstring """
        print("Drawing is starting...")


@dataclass
class Pen(Stationery):
    """ Pen Class Docstring """
    title = "pen"

    def draw(self):
        print(f"The {self.title} is writing...")


@dataclass
class Pencil(Stationery):
    """ Pencil Class Docstring """
    title = "pencil"

    def draw(self):
        print(f"The {self.title} is tracing...")


@dataclass
class Handle(Stationery):
    """ Handle Class Docstring """
    title = "marker"

    def draw(self):
        print(f"The {self.title} is painting...")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
