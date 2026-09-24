import pygame

white = (240, 217, 181)
brown = (181, 136, 99)

files = "abcdefgh"


def draw_board(screen):

    width, height = screen.get_size()

    board_size = min(width, height)
    square_size = board_size // 8

    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    for i in range(8):
        for j in range(8):

            x = offset_x + j * square_size
            y = offset_y + i * square_size

            if (i + j) % 2 == 0:
                color = white
            else:
                color = brown

            pygame.draw.rect(
                screen,
                color,
                (x, y, square_size, square_size)
            )


def draw_coordinates(screen):

    font = pygame.font.SysFont("Arial", 20)

    width, height = screen.get_size()

    board_size = min(width, height)
    square_size = board_size // 8

    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    for col in range(8):

        text = font.render(files[col], True, (70, 70, 70))

        x = offset_x + col * square_size + 5
        y = offset_y + board_size - 25

        screen.blit(text, (x, y))

    for row in range(8):

        text = font.render(str(8 - row), True, (70, 70, 70))

        x = offset_x + 5
        y = offset_y + row * square_size + 5

        screen.blit(text, (x, y))


def get_square(screen, mouse_x, mouse_y):

    width, height = screen.get_size()

    board_size = min(width, height)
    square_size = board_size // 8

    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    if (offset_x <= mouse_x < offset_x + board_size and
        offset_y <= mouse_y < offset_y + board_size):

        column = (mouse_x - offset_x) // square_size
        row = (mouse_y - offset_y) // square_size

        file = files[column]
        rank = 8 - row

        return file + str(rank)

    return None