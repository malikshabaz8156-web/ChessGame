import pygame
import board

pygame.init()

screen = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Chess")

running = True

while running:

    board.draw_board(screen)

    board.draw_coordinates(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            square = board.get_square(
                event.pos[0],
                event.pos[1]
            )

            if square:
                print(square)

    pygame.display.update()

pygame.quit()