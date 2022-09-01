#ЗАДАНИЕ 1

class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

        def __add__(self, other: 'Matrix'):
            try:
                rows_count = len(self.value)
                items_count = len(self.value[0])

                new value = [
                    [
                    self.value[row][idx] + other.value [row][idx]
                     for idx in range(items_count)
                     ]
                    for row in range(rows_count)
                ]

                return Matrix(new_value)
            except IndexError:
                print("Ошибка матрицы разного размера")
                exit(1)

                def __str__(self)
                    return "\n".join(
                        str(row).strip('[]').replace(',','')
                        for row in self.value
                    )

a = Matrix([
    [21, 22, 23]
    [24, 25, 26]
])

b = Matrix([
    [21, 22, 23]
    [24, 25, 26]
])

c = a + b
print(c)

#ЗАДАНИЕ 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    name: str

    def __int__(self, name: str):
self.name = name
@property
@abstractmethod
def calculate(self) -> float
    pass

class Coat(Clothes):
    _size: float

    def __int__(self, name:str, size: float):
        super().__int__(name)
        self._size = size

        @property
        def calculate(self) -> float:
            return self._size = size

class Suit(Clothes):
    _height: float

def __int__(self, name:str, height: float):
    super().__init__(name)
    self._hight = height

    @property
    def calculate(self) -> float:
        return 2 * self._height + 0.3

coat = Coat('Пальто', 3)
print(coat.calculate)
print(suit.calculate)












