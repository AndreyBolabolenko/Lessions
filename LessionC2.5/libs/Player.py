import random

from .Board import Board
from .Exceptions import *


class Player:
    enemy_board = None  # type: Board
    board = None  # type: Board
    player_name = ""  # type: str

    def __init__(self, enemy_board, board):
        self.enemy_board = enemy_board
        self.board = board

    def ask(self):
        """
        Запрос на ввод координат выстрела.
        """
        pass

    def move(self):
        """
        Делаем ход по доске противника, в случае попадания повторяем ход
        """
        pass


class AI(Player):

    player_name = "Компьютер"

    def ask(self):
        coordinate_x = random.randint(0, 5)
        coordinate_y = random.randint(0, 5)
        return coordinate_x, coordinate_y

    def move(self):
        next_move = True
        while next_move:
            try:
                coordinate_x, coordinate_y = self.ask()

                next_move = self.enemy_board.shot(coordinate_x, coordinate_y)
                print(f"Выстрел компьютера: [{coordinate_x}, {coordinate_y}]")
            except ShotAnOnePoint:
                continue


class User(Player):

    player_name = "Игрок"

    def ask(self):
        """
        Запрашиваем у пользователя ввод координат
        """
        while True:
            try:
                coordinate_x, coordinate_y = input("Введите координаты выстрела x,y: ").replace(" ", "").split(",")

                return int(coordinate_x), int(coordinate_y)

            except ValueError:
                print("Ошибка ввода! Пожалуйста введите координаты в формате X,Y")

    def move(self):
        while True:
            try:
                coordinate_x, coordinate_y = self.ask()
                if self.enemy_board.shot(coordinate_x, coordinate_y):
                    self.enemy_board.print_board()
                    print("Есть попадание!")

                    if self.enemy_board.all_ships_dead():
                        break
                    continue

                break

            except (BoardOutException, ShotAnOnePoint) as err:
                print(err)
                continue
