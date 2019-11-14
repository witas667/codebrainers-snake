import pygame

from model import initialize_board, initialize_snake, set_new_position, create_apple, eat_apple
from view import draw

step = 20
width = 400
height = 400
dimensions = (width, height)


pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("codebrainers-snake")
clock = pygame.time.Clock()

def turn(direction):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN]:
        return 2
    if pressed_key[pygame.K_UP]:
        return 0
    if pressed_key[pygame.K_LEFT]:
        return 3
    if pressed_key[pygame.K_RIGHT]:
        return 1
    return direction


head_direction = 0
board = initialize_board()
snake = initialize_snake(board)
apple = create_apple(board)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)
    head_direction = turn(head_direction)

    apple = eat_apple(board, snake, apple)

    snake = set_new_position(head_direction, snake, board)

    # create_apple(apple)

    screen.fill((255, 255, 255))

    draw(board, screen)
    print(board)
    pygame.display.flip()

    counter = clock.tick(12)


