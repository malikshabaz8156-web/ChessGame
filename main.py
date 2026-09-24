import pygame
import board

pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

pygame.display.set_caption("Chess")
icon = pygame.image.load("assets/logo.jpg")
pygame.display.set_icon(icon)

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
                screen,
                event.pos[0],
                event.pos[1]
            )

            if square:
                print(square)

    pygame.display.update()

pygame.quit()