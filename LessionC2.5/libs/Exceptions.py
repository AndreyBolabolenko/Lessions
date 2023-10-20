class BoardOutException(Exception):
    def __str__(self):
        return "Выход за пределы игровой доски! Коондинаты должны быть в диапазоне от 0 до 5"


class ShipLengthException(Exception):
    def __str__(self):
        return "Корабль должен иметь длинну от 1 до 3!"


class ShipDirectionException(Exception):
    def __str__(self):
        return "Укажте правильное направление корабля (vertical, horizontal)"


class BoardShipCollision(Exception):
    def __str__(self):
        return "Корабль пересекается или не имеет отступа"


class GenerationBoardFailed(Exception):
    def __str__(self):
        return "Ошибка генерации доски"


class ShotAnOnePoint(Exception):
    def __str__(self):
        return "Выстрел в одну и туже точку запрещен"
