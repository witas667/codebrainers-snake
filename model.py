import random


def initialize_board():
    _board = {}
    for x in range(20):
        for y in range(20):
            _board[(x, y)] = None
    return _board


def initialize_snake(_board):
    _snake = [(random.randint(8, 12), (random.randint(8, 12)))]
    _board[_snake[0]] = "SnakeHead"
    return _snake


def create_apple(_board):
    _apple = (random.randint(0, 19), random.randint(0, 19))
    while _board[_apple] is not None:
        _apple = (random.randint(0, 19), random.randint(0, 19))
    _board[_apple] = "Apple"
    return _apple
def game_over(_board, coordinate):
    if coordinate[0] < 0 or coordinate[0] > 19 or coordinate[1] < 0 or coordinate[1] > 19 or _board[coordinate] == "SnakeHead":
        exit(2)

def move_tail(snake):
    return snake[:-1]

def set_new_position(direction, snake, _board):
    move_tail(snake)
    head_x, head_y = snake[0]
    _board[(head_x, head_y)] = None
    if direction == 0:
        head_y = head_y - 1
    if direction == 1:
        head_x = head_x + 1
    if direction == 2:
        head_y = head_y + 1
    if direction == 3:
        head_x = head_x - 1
    game_over(_board, coordinate=(head_x, head_y))
    _board[(head_x, head_y)] = "SnakeHead"
    snake = [(head_x, head_y)] + move_tail(snake)
    for elem in snake:
        _board[elem] = "SnakeHead"
    return snake

def eat_apple(_board, _snake, _apple):
    if _snake[0] == _apple:
        _snake.append(_apple)
        print(_snake)
        return create_apple(_board)
    return _apple