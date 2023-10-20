import random

from .Player import User, AI, Player
from .Board import Board
from .Dot import Dot
from .Ship import Ship
from .Exceptions import *


class Game:
    __user = User  # type: User
    __ai = AI  # type: AI

    __current_player = None  # type: Player

    def __init__(self):
        board_user = Game.random_board("Player")
        board_ai = Game.random_board("AI")

        self.__user = User(board_ai, board_user)
        self.__ai = AI(board_user, board_ai)

        self.__user.board.enable_visible()

        self.__current_player = random.choice([self.__user, self.__ai])

    def start(self):
        """Метод запускающий игру"""
        Game.great()
        self.loop()

    @staticmethod
    def great():
        """Приветсвуем игрока, рсссказываем о правилах игры"""
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x,y ")
        print(" x - номер строки  ")
        print(" y - номер столбца \n\n")

    def change_player(self):
        """
        Смена игрока
        """
        self.__current_player = self.__ai if self.__current_player == self.__user else self.__user

    def print_all_boards(self):
        self.__ai.board.print_board()
        self.__user.board.print_board()

    def loop(self):
        """Основной цикл игры"""

        self.print_all_boards()
        print(f"Первым ходит {self.__current_player.player_name}")

        while True:
            self.__current_player.move()

            if self.__current_player.enemy_board.all_ships_dead():
                self.__ai.board.enable_visible()
                self.print_all_boards()
                print(f"Игра оконченна! Победа игрока: {self.__current_player.player_name}")
                break

            self.print_all_boards()
            self.change_player()

    @staticmethod
    def random_board(board_name):
        """
        Генерируем случайную доску
        """
        ship_type = [(1, 3), (2, 2), (4, 1)]

        while True:
            try:
                board = Board(board_name)

                for ship_info in ship_type:
                    count, length = ship_info
                    for i in range(1, count + 1):
                        try_index = 0
                        while try_index <= 1000:
                            coordinate_x = random.randint(0, 5)
                            coordinate_y = random.randint(0, 5)
                            direction = random.choice(['vertical', 'horizontal'])

                            try:
                                gen_ship = Ship.generate_ship(Dot(coordinate_x, coordinate_y), direction, length)
                                if board.add_ship(gen_ship):
                                    break

                            except (BoardShipCollision, BoardOutException,):
                                try_index += 1
                                continue
                        if try_index == 1000:
                            raise GenerationBoardFailed

                return board

            except GenerationBoardFailed:
                continue
