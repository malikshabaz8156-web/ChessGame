import pygame
import board

# Initialize Pygame
pygame.init()

# Create resizable window
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Set window title
pygame.display.set_caption("Chess")

# Control the game loop
running = True

while running:

    # Draw the chess board
    board.draw_board(screen)

    # Draw chess coordinates
    board.draw_coordinates(screen)

    # Get and handle events
    for event in pygame.event.get():

        # Close the window
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:

            # Close the game when ESC is pressed
            if event.key == pygame.K_ESCAPE:
                running = False

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Get the clicked chess square
            square = board.get_square(
                screen,
                event.pos[0],
                event.pos[1]
            )

            # Print the square if it is valid
            if square:
                print(square)

    # Update the display
    pygame.display.update()

# Close Pygame
pygame.quit()