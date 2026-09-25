import pygame

# Board colors
green = (118, 150, 86)
white = (238, 238, 210)

# Chess file names
files = "abcdefgh"


def draw_board(screen):

    # Get window size
    width, height = screen.get_size()

    # Calculate board and square size
    board_size = min(width, height)
    square_size = board_size // 8

    # Center the board
    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    # Loop through all rows and columns
    for i in range(8):
        for j in range(8):

            # Calculate square position
            x = offset_x + j * square_size
            y = offset_y + i * square_size

            # Alternate square colors
            if (i + j) % 2 == 0:
                color = white
            else:
                color = green

            # Draw the square
            pygame.draw.rect(
                screen,
                color,
                (x, y, square_size, square_size)
            )


def draw_coordinates(screen):

    # Set font and size
    font = pygame.font.SysFont("Arial", 20)

    # Get window size
    width, height = screen.get_size()

    # Calculate board and square size
    board_size = min(width, height)
    square_size = board_size // 8

    # Center the board
    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    # Draw a-h
    for col in range(8):

        # Create the file letter
        text = font.render(files[col], True, (70, 70, 70))

        # Position of the letter
        x = offset_x + col * square_size + 5
        y = offset_y + board_size - 25

        # Draw the letter
        screen.blit(text, (x, y))

    # Draw 8-1
    for row in range(8):

        # Create the rank number
        text = font.render(str(8 - row), True, (70, 70, 70))

        # Position of the number
        x = offset_x + 5
        y = offset_y + row * square_size + 5

        # Draw the number
        screen.blit(text, (x, y))


def get_square(screen, mouse_x, mouse_y):

    # Get window size
    width, height = screen.get_size()

    # Calculate board and square size
    board_size = min(width, height)
    square_size = board_size // 8

    # Center the board
    offset_x = (width - board_size) // 2
    offset_y = (height - board_size) // 2

    # Check if mouse is inside the board
    if (offset_x <= mouse_x < offset_x + board_size and
        offset_y <= mouse_y < offset_y + board_size):

        # Find clicked column and row
        column = (mouse_x - offset_x) // square_size
        row = (mouse_y - offset_y) // square_size

        # Convert to chess coordinates
        file = files[column]
        rank = 8 - row

        # Return square name such as e4
        return file + str(rank)

    # Return nothing if click is outside the board
    return None