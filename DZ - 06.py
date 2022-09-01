#ЗАДАНИЕ 1

import itertools
import time

class trafficLights:
    __color: str
    __timing: dict

    def __init(self, red_time:  int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {
            "red" = red_time,
        "yellow" = yellow_time
        "green" = green_time
        }

        def running(self):
            for mode, timer in itertools.cycle(self.__timing.items()):
                self.__color = mode

for second in range(timer):
    print(f"{self} [{second + 1}")
    time.sleep(1)

    def __repr__(self):
        return f"Текущий режим" = {self.__color}

        try:
            traffic_light = TrafficLight(7, 2, 5)
            traffic_light.running()
        except keyboardinterrupt:
            print("Exit the program")


# ЗАДАНИЕ 2
class Road:
    __mass: float = 25.0
    _length: float
    _width: float
    def __init__(self, length: float, width: float)
        self._length = length
        self._width = width

        def calculate(self, depth: float = 1)
            return self._length * self._width * self._mass * depth) / 1000

            road = Road(20, 5000)
            calculation = road.calculate(5)
            print(f"{calculation} T")

#ЗАДАНИЕ 3
class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def__init__(self, name: str, surname: str, position: str, wage: int, bonus: int)
    self.name = name
    self.surname = surname
    self._income = {
        "wage" = wage
    "bonus" = bonus
    }

    class Position(Worker):
        def get_full_name(self):
            return f"{self.name} {self.surname}"

        def get_total_income(self):
            return sum(self._income.values())




