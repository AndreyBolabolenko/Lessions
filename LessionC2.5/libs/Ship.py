from .Dot import Dot
from .Exceptions import ShipLengthException, ShipDirectionException


class Ship:
    """
    Класс содержащий в себе информацию о коробле
    """

    _length = None  # type: int
    _head = None  # type: Dot
    _direction = None  # type: str

    _dots = None  # type: list[Dot]

    def __init__(self, head: Dot, dots: [Dot], direction: str):
        self._head = head
        self._dots = dots
        self._direction = direction
        self._length = len(dots)

    def dots(self):
        return self._dots

    def lives(self):
        """
        Подсчитываем колличество жизней у коробля
        :return:
        """
        count = 0
        for item in self._dots:
            if not item.hit:
                count += 1

        return count

    @staticmethod
    def generate_ship(head: Dot, direction: str, length: int):
        """
        Генерируем корабль от точки головы по направлению
        """
        if 0 <= length > 3:
            print("Current lenght: " + str(length))
            raise ShipLengthException

        dots = [head]

        # Генерируем корабль по вертикали
        if direction == "vertical":
            for coordinate in range(head.coordinate_y+1, head.coordinate_y+length):
                dots.append(
                    Dot(head.coordinate_x, coordinate)
                )
            return Ship(head, dots, direction)

        # Генерируем корабль по горизонтали
        if direction == "horizontal":
            for coordinate in range(head.coordinate_x+1, head.coordinate_x+length):
                dots.append(
                    Dot(coordinate, head.coordinate_y)
                )
            return Ship(head, dots, direction)

        # Выдаем ошибку в случае указания не правильного направления
        raise ShipDirectionException

    def __str__(self):
        return str([(dot.coordinate_x, dot.coordinate_y, dot.hit) for dot in self._dots])
