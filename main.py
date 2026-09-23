import pygame
import board

pygame.init()

# Create screen
screen = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Chess")

running = True

while running:

    # Draw board
    board.draw_board(screen)

    # Draw coordinates
    board.draw_coordinates(screen)

    # Handle events
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Press ESC to close
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            square = board.get_square(
                event.pos[0],
                event.pos[1]
            )

            if square:
                print(square)

    # Update screen
    pygame.display.update()

pygame.quit()