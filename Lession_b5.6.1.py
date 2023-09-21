import random

players = (
    {
        'name': None,
        'charset': "0",
    },
    {
        'name': None,
        'charset': 'X',
    }
)
current_player = players[0]
board = ([None]*3, [None]*3, [None]*3)


def board_is_full():
    """
    Проверка на наличие свободных ячеек в игре
    :return:
    """
    for cell in board:
        if None in cell:
            return False
    return True


def print_board():
    """
    Выводим доску в консоль
    :return:
    """
    print("-" * 17)
    print(f"    " + str("{:^3} {:^3} {:^3} ").format(0, 1, 2))
    for idx, element_x in enumerate(board):
        elements = [' ' if x is None else x for x in element_x]
        print(f"{idx}  |" + str("{:^3}|{:^3}|{:^3}|").format(*elements))
    print("-" * 17)


def setup_player_name():
    """
    Задаём имена игроков
    :return:
    """
    for player in players:
        if player['name'] is None:
            player['name'] = input(f"Введите имя игрока [{player['charset']}]: ")


def change_player():
    """
    Смена текущего игрока
    :return:
    """
    global current_player
    current_player = players[1] if current_player == players[0] else players[0]


def movie_player():
    """
    Ход игрока
    :return:
    """
    while True:
        try:
            x_coordinate = int(input("Введите координату X: "))
            y_coordinate = int(input("Введите координату Y: "))

            if not 0 <= x_coordinate <= 2 or not 0 <= y_coordinate <= 2:
                print("Введите правильные координаты!")
                continue

            if not board[y_coordinate][x_coordinate] is None:
                print("Эта ячейка уже занята!")
                continue

            board[y_coordinate][x_coordinate] = current_player['charset']
            break
        except ValueError:
            print("Необходимо ввести только целые числа")
            continue


def check_winner():
    """
    Проверяем победил ли текущий игрок
    :return:
    """

    # Проверка выйгрыша по горизонтали
    for horizontal in board:
        if horizontal.count(current_player['charset']) == 3:
            return True

    # Проверка выйгрыша по вертикали
    for i in range(0, 3):
        line = []
        for x in range(0, 3):
            line.append(board[x][i])

        if line.count(current_player['charset']) == 3:
            return True

    # Проверка выйгрыша по диагонали
    diagonal_1 = []
    for x in range(0, 3):
        diagonal_1.append(board[x][x])

    if diagonal_1.count(current_player['charset']) == 3:
        return True

    diagonal_2 = []
    y = 0
    for x in reversed(range(0, 3)):
        diagonal_2.append(board[y][x])
        y += 1

    if diagonal_2.count(current_player['charset']) == 3:
        return True

    return False


def game_loop():
    """
    Основной цикл игры
    :return:
    """

    while not board_is_full():
        print(f"Ход игрока {current_player['name']} [{current_player['charset']}]")
        movie_player()
        print_board()

        if check_winner():
            print(f"Победил игрок {current_player['name']} [{current_player['charset']}] !")
            return

        change_player()
    print("У нас ничья!")


if __name__ == '__main__':
    setup_player_name()
    current_player = random.choice(players)

    print(f"\nИгру начинает {current_player['name']} [{current_player['charset']}]")
    print_board()
    game_loop()
