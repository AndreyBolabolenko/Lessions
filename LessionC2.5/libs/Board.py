from . import Ship
from .Exceptions import BoardOutException, BoardShipCollision, ShotAnOnePoint
from .Dot import Dot, BoardDot
from copy import deepcopy


class Board:
    """
    Доска на которой находятся корабли
    **Расстояние минимум 1 клетка

    """
    __hidden = True  # type: bool
    __ships = None  # type: list[Ship]
    __board = None  # type: list[list[BoardDot]]

    __board_name = None

    def __init__(self, board_name):
        self.__board_name = board_name
        self.__board = Board.generate_board()
        self.__ships = []

    @staticmethod
    def generate_board():
        gen_board = []
        for i in range(0, 6):
            line_x = []
            for x in range(0, 6):
                line_x.append(BoardDot(i, x))
            gen_board.append(line_x)
        return gen_board

    def enable_visible(self):
        """
        Включаем видимость кораблей на доске
        """
        self.__hidden = False

    def print_board(self, board=None):
        """
        Отображаем информацию с доски в консоль
        :return:
        """
        print_board = self.__board if board is None else board

        if not self.__hidden:
            for ship in self.__ships:
                for dot in ship.dots():
                    print_board[dot.coordinate_y][dot.coordinate_x] = dot

        print("-" * 7 + " {:^6} Board ".format(self.__board_name) + "-" * 7)
        print(f"   " + str("{:^3} {:^3} {:^3} {:^3} {:^3} {:^3} ").format(0, 1, 2, 3, 4, 5, 6))

        for idy, dots in enumerate(print_board):
            elements = [repr(i) for i in dots]
            print(f"{idy} |" + str("{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|").format(*elements))
        print("-" * 27)

    def shot(self, coordinate_x, coordinate_y):
        """
        Выстреливаем по указанным координатам
        :param coordinate_x:
        :param coordinate_y:
        :return: Возвращаем булевое значение в случае попадания по цели
        """
        if 0 < coordinate_y > 5 or 0 < coordinate_x > 5:
            raise BoardOutException

        shot_dot = Dot(coordinate_x, coordinate_y)

        # Находим из списка короблей все точки и сверяем с указанными координатами
        for ship in self.__ships:
            for dot in ship.dots():
                if shot_dot == dot:

                    if dot.hit:
                        raise ShotAnOnePoint

                    if isinstance(self.__board[coordinate_y][coordinate_x], BoardDot):
                        if self.__board[coordinate_y][coordinate_x].miss:
                            raise ShotAnOnePoint

                    dot.kick()
                    self.__board[dot.coordinate_y][dot.coordinate_x].kick()

                    if ship.lives() == 0:
                        self.contur_ship(ship, inboard=True)

                    return True

        self.__board[shot_dot.coordinate_y][shot_dot.coordinate_x].miss = True
        return False

    def contur_ship(self, ship, contur_board=None, inboard=False):
        """
        Обводим корабль по контуру
        :param ship: текущий корабль который обводим
        :param contur_board: доска на которую наносим контур
        :param inboard: сохранить доску с контуром на игровую
        :return:
        """

        if contur_board is None:
            contur_board = deepcopy(self.__board)

        near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dot in ship.dots():
            for dx, dy in near:
                coordinate_x = dot.coordinate_x + dx
                coordinate_y = dot.coordinate_y + dy

                if not Board.out(coordinate_x, coordinate_y):
                    contur_board[coordinate_y][coordinate_x].contur = True

        if inboard:
            self.__board = contur_board

        return contur_board

    @staticmethod
    def out(coordinate_x: int, coordinate_y: int):
        """
        Проверка не выходят ли координаты за пределы поля
        """
        if 0 <= coordinate_x <= 5 and 0 <= coordinate_y <= 5:
            return False
        return True

    def add_ship(self, ship: Ship):
        """
        Добавляем корабль на доску
        """
        board = None

        if len(self.__ships) > 0:
            for element in self.__ships:
                board = self.contur_ship(element, contur_board=board)

            for dot in ship.dots():
                if self.out(dot.coordinate_x, dot.coordinate_y):
                    raise BoardOutException

                if not repr(board[dot.coordinate_y][dot.coordinate_x]) == " ":
                    raise BoardShipCollision
        else:
            for dot in ship.dots():
                if self.out(dot.coordinate_x, dot.coordinate_y):
                    raise BoardOutException
        self.__ships.append(ship)
        return True

    def all_ships_dead(self):
        """
        Проверка есть ли живые корабли на доске
        """
        for item in self.__ships:  # type: Ship
            if item.lives() > 0:
                return False

        return True

    def is_contur(self, coordinate_x, coordinate_y):
        try:
            return self.__board[coordinate_y][coordinate_x].contur
        except AttributeError:
            return False
