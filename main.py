import pygame

pygame.init()

width=1920
height=1080
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Chess")

board_size = min(1080, 1080)
square_size = board_size // 8

offset_x = (width - board_size) // 2
offset_y = (height - board_size) // 2

white= (240, 217, 181)
brown = (181, 136, 99)

for i in range(8):
    for j in range(8):

        x = offset_x + j * square_size
        y = offset_y + i * square_size

        if (i+j) % 2 == 0:
            color = white
        else:
            color = brown

        pygame.draw.rect(screen,color,(x, y, square_size, square_size))


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            column = (mouse_x - offset_x) // square_size
            row = (mouse_y - offset_y) // square_size

            files = "abcdefgh"
            font = pygame.font.Font(None, 30)

            for col in range(8):
                text = font.render(files[col], True, (0, 0, 0))

                x = offset_x + col * square_size + 5
                y = offset_y + board_size - 30

                screen.blit(text, (x, y))

                file = files[column]
                rank = 8 - row

                square = file + str(rank)

                print(square)
            for row in range(8):
                text = font.render(str(8 - row), True, (0, 0, 0))

                x = offset_x + 5
                y = offset_y + row * square_size + 5

                screen.blit(text, (x, y))
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()