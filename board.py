import pygame

# Screen size
width = 1920
height = 1080

# Board size
board_size = min(width, height)
square_size = board_size // 8

# Center the board
offset_x = (width - board_size) // 2
offset_y = (height - board_size) // 2

# Board colors
white = (240, 217, 181)
brown = (181, 136, 99)

# Chess files
files = "abcdefgh"


# Draw the chessboard
def draw_board(screen):

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


# Draw chess coordinates
def draw_coordinates(screen):

    font = pygame.font.Font(None, 30)

    # Draw a-h
    for col in range(8):

        text = font.render(files[col], True, (0, 0, 0))

        x = offset_x + col * square_size + 5
        y = offset_y + board_size - 30

        screen.blit(text, (x, y))

    # Draw 8-1
    for row in range(8):

        text = font.render(str(8 - row), True, (0, 0, 0))

        x = offset_x + 5
        y = offset_y + row * square_size + 5

        screen.blit(text, (x, y))


# Convert mouse position to chess square
def get_square(mouse_x, mouse_y):

    # Check if the mouse is inside the board
    if (offset_x <= mouse_x < offset_x + board_size and
        offset_y <= mouse_y < offset_y + board_size):

        column = (mouse_x - offset_x) // square_size
        row = (mouse_y - offset_y) // square_size

        file = files[column]
        rank = 8 - row

        return file + str(rank)

    return None