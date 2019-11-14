import pygame

def draw(board, screen):
    for coordinates, value in board.items():
        new_coordinates = map(lambda x: x*20, coordinates)
        if value == "SnakeHead":
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (128, 128, 128), head_rect)
        elif value is None:
            head_x = coordinates[0] * 20
            head_y = coordinates[1] * 20
            head_rect = pygame.Rect(head_x, head_y, 20, 20)
            pygame.draw.rect(screen, (228, 190, 207), head_rect)
        elif value == "Apple":
            apple_x = coordinates[0] * 20
            apple_y = coordinates[1]
            head_rect = pygame.Rect(*new_coordinates, 20, 20)
            pygame.draw.rect(screen, (255, 0, 0), head_rect)