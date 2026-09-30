import os
import pygame


class PieceRenderer:

    def __init__(self, square_size):
        self.square_size = square_size
        self.pieces = {}

        self.load_piece_images()

    def load_piece_images(self):
        piece_names = [
            "WP", "WR", "WN", "WB", "WQ", "WK",
            "BP", "BR", "BN", "BB", "BQ", "BK"
        ]

        for piece in piece_names:
            path = os.path.join(
                "assets",
                "pieces",
                piece + ".png"
            )

            try:
                image = pygame.image.load(path)

                image = pygame.transform.smoothscale(
                    image,
                    (self.square_size, self.square_size)
                )

                self.pieces[piece] = image

            except pygame.error:
                print(f"Warning: Could not load {path}")

    def draw_pieces(self, screen, board):
        for row in range(8):
            for col in range(8):

                piece = board[row][col]

                if piece == "--" or piece is None:
                    continue

                image = self.pieces.get(piece)

                if image is None:
                    continue

                x = col * self.square_size
                y = row * self.square_size

                screen.blit(image, (x, y))

    def draw_captured_pieces(
        self,
        screen,
        captured_pieces,
        board_size,
        window_width
    ):
        x = board_size + 20
        y = 65

        for piece in captured_pieces:

            image = self.pieces.get(piece)

            if image is None:
                continue

            small_image = pygame.transform.smoothscale(
                image,
                (40, 40)
            )

            screen.blit(
                small_image,
                (x, y)
            )

            x += 45

            if x > window_width - 45:
                x = board_size + 20
                y += 45