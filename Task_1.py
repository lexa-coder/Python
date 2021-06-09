"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __color = ['\033[31mКрасный', '\033[33mЖелтый', '\033[32mЗеленый']

    def __init__(self, name):
        self.name = name
        self._run()

    def _run(self):
        print(self.name, ': Запуск')

    def running(self):
        a = int(input('Введите количество итераций: '))
        i = 0
        while i < a * 3:

            for el in enumerate(TrafficLight.__color):

                if el[0] == 0:
                    print(el[1])
                    time.sleep(7)
                elif el[0] == 1:
                    print(el[1])
                    time.sleep(2)
                elif el[0] == 2:
                    print(el[1])
                    time.sleep(5)

                i += 1


TrafficLight = TrafficLight('Светофор')

TrafficLight.running()

