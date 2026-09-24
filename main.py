import pygame
# import board

pygame.init() # initializes Pygame's modules.

# TODO: store width, height values in a constant. 
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # will create a display surface.

pygame.display.set_caption("Chess") # title for the window.
icon = pygame.image.load("assets/logo.jpg") # loads the 'image/icon'.
# TODO: look up if this method can be replaced.
pygame.display.set_icon(icon) # sets the 'image/icon'.

running = True

while running: # game loop; for rendering graphics, repeatedly handle events and update game logic.

    board.draw_board(screen) # draws the 'board'.
    board.draw_coordinates(screen) # draws the coordinates on the board.

    for event in pygame.event.get(): # iterates through the list of 'events' that occur.

        if event.type == pygame.QUIT: # pretty straightforward.
            running = False

        if event.type == pygame.KEYDOWN: # triggered when pressed a keyboard key.
            if event.key == pygame.K_ESCAPE: # 'esc' button.
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # pretty straighforward; mouse click.

            square = board.get_square( # gets the pos of the square that is being clicked.
                screen,
                event.pos[0],
                event.pos[1]
            )

            if square: # if the click happens inside a particular cell/square it's displayed.
                print(square)

    pygame.display.update() # refresh/update the page so that changes are visible.

pygame.quit() # shutting down; releasing resources per se.