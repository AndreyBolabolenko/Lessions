class Dot:
    """
    Класс с точками корабля
    """

    __coordinate_x = None  # type: int
    __coordinate_y = None  # type: int
    __hit = None  # type: bool

    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.__hit = False

    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, value):
        self.__coordinate_x = value

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, value):
        if 0 > value > 5:
            raise
        self.__coordinate_y = value

    @property
    def hit(self):
        return self.__hit

    def kick(self):
        """
        Зафиксировать попадание по точке корабля
        :return:
        """
        self.__hit = True

    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise ValueError
        other: Dot

        return self.coordinate_y == other.coordinate_y and self.coordinate_x == other.coordinate_x

    def __repr__(self):
        if self.__hit:
            return "X"
        return "■"

    def __str__(self):
        return f"Dot[{self.__coordinate_x}, {self.__coordinate_y}]/[{self.__hit}]"


class BoardDot(Dot):

    miss = None
    contur = None

    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.contur = False
        self.miss = False

    def __repr__(self):
        if not self.miss and not self.hit and not self.contur:
            return " "

        if self.miss:
            return "T"

        if self.hit:
            return "X"

        if self.contur:
            return "•"

    def __str__(self):
        return f"BoardDot[{self.__coordinate_x}, {self.__coordinate_y}]/[{self.__hit}, {self.miss}]"
