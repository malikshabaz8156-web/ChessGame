import pygame
import os


class ChessGUI:

    def __init__(self, board_size=640):

        pygame.init()

        # -----------------------------------------
        # Window
        # -----------------------------------------

        self.BOARD_SIZE = board_size
        self.SQUARE_SIZE = board_size // 8

        self.SIDEBAR_WIDTH = 220

        self.WINDOW_WIDTH = (
            self.BOARD_SIZE + self.SIDEBAR_WIDTH
        )

        self.WINDOW_HEIGHT = self.BOARD_SIZE

        self.screen = pygame.display.set_mode(
            (
                self.WINDOW_WIDTH,
                self.WINDOW_HEIGHT
            )
        )

        pygame.display.set_caption(
            "Python Pygame Chess"
        )

        self.clock = pygame.time.Clock()

        # -----------------------------------------
        # Board colors
        # -----------------------------------------

        self.LIGHT_SQUARE = (240, 217, 181)
        self.DARK_SQUARE = (181, 136, 99)

        # -----------------------------------------
        # Highlight colors
        # -----------------------------------------

        self.SELECTED_COLOR = (255, 215, 0)
        self.MOVE_COLOR = (80, 180, 80)
        self.CAPTURE_COLOR = (200, 70, 70)
        self.LAST_MOVE_COLOR = (100, 150, 220)

        # -----------------------------------------
        # GUI colors
        # -----------------------------------------

        self.BACKGROUND_COLOR = (35, 35, 35)
        self.TEXT_COLOR = (255, 255, 255)

        # -----------------------------------------
        # State
        # -----------------------------------------

        self.selected_square = None

        self.possible_moves = []

        self.captured_pieces = []

        self.last_move = None

        # -----------------------------------------
        # Load pieces
        # -----------------------------------------

        self.pieces = {}

        self.load_piece_images()

    # =====================================================
    # LOAD PIECE IMAGES
    # =====================================================

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
                    (
                        self.SQUARE_SIZE,
                        self.SQUARE_SIZE
                    )
                )

                self.pieces[piece] = image

            except pygame.error:

                print(
                    f"Warning: Could not load {path}"
                )

    # =====================================================
    # DRAW BOARD
    # =====================================================

    def draw_board(self):

        for row in range(8):

            for col in range(8):

                if (row + col) % 2 == 0:

                    color = self.LIGHT_SQUARE

                else:

                    color = self.DARK_SQUARE

                x = col * self.SQUARE_SIZE
                y = row * self.SQUARE_SIZE

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        x,
                        y,
                        self.SQUARE_SIZE,
                        self.SQUARE_SIZE
                    )
                )

    # =====================================================
    # DRAW BOARD COORDINATES
    # =====================================================

    def draw_coordinates(self):

        font = pygame.font.Font(None, 18)

        files = [
            "a", "b", "c", "d",
            "e", "f", "g", "h"
        ]

        ranks = [
            "8", "7", "6", "5",
            "4", "3", "2", "1"
        ]

        for col in range(8):

            x = (
                col * self.SQUARE_SIZE
                + self.SQUARE_SIZE
                - 12
            )

            y = self.BOARD_SIZE - 18

            text = font.render(
                files[col],
                True,
                (80, 80, 80)
            )

            self.screen.blit(
                text,
                (x, y)
            )

        for row in range(8):

            x = 5

            y = (
                row * self.SQUARE_SIZE
                + 5
            )

            text = font.render(
                ranks[row],
                True,
                (80, 80, 80)
            )

            self.screen.blit(
                text,
                (x, y)
            )

    # =====================================================
    # DRAW LAST MOVE
    # =====================================================

    def draw_last_move(self):

        if self.last_move is None:
            return

        start_square, end_square = self.last_move

        for row, col in [
            start_square,
            end_square
        ]:

            x = col * self.SQUARE_SIZE
            y = row * self.SQUARE_SIZE

            surface = pygame.Surface(
                (
                    self.SQUARE_SIZE,
                    self.SQUARE_SIZE
                ),
                pygame.SRCALPHA
            )

            surface.fill(
                (
                    self.LAST_MOVE_COLOR[0],
                    self.LAST_MOVE_COLOR[1],
                    self.LAST_MOVE_COLOR[2],
                    80
                )
            )

            self.screen.blit(
                surface,
                (x, y)
            )

    # =====================================================
    # DRAW SELECTED SQUARE
    # =====================================================

    def draw_selected_square(self):

        if self.selected_square is None:
            return

        row, col = self.selected_square

        x = col * self.SQUARE_SIZE
        y = row * self.SQUARE_SIZE

        pygame.draw.rect(
            self.screen,
            self.SELECTED_COLOR,
            (
                x,
                y,
                self.SQUARE_SIZE,
                self.SQUARE_SIZE
            ),
            5
        )

    # =====================================================
    # DRAW POSSIBLE MOVES
    # =====================================================

    def draw_possible_moves(self):

        for move in self.possible_moves:

            row, col = move

            center_x = (
                col * self.SQUARE_SIZE
                + self.SQUARE_SIZE // 2
            )

            center_y = (
                row * self.SQUARE_SIZE
                + self.SQUARE_SIZE // 2
            )

            pygame.draw.circle(
                self.screen,
                self.MOVE_COLOR,
                (
                    center_x,
                    center_y
                ),
                10
            )

    # =====================================================
    # DRAW PIECES
    # =====================================================

    def draw_pieces(self, board):

        for row in range(8):

            for col in range(8):

                piece = board[row][col]

                # Empty square
                if piece == "--":
                    continue

                # No piece
                if piece is None:
                    continue

                image = self.pieces.get(piece)

                if image is None:
                    continue

                x = col * self.SQUARE_SIZE
                y = row * self.SQUARE_SIZE

                self.screen.blit(
                    image,
                    (
                        x,
                        y
                    )
                )

    # =====================================================
    # DRAW CAPTURED PIECES
    # =====================================================

    def draw_captured_pieces(self):

        font = pygame.font.Font(
            None,
            25
        )

        title = font.render(
            "Captured Pieces",
            True,
            self.TEXT_COLOR
        )

        self.screen.blit(
            title,
            (
                self.BOARD_SIZE + 20,
                25
            )
        )

        x = self.BOARD_SIZE + 20
        y = 65

        for piece in self.captured_pieces:

            image = self.pieces.get(piece)

            if image is None:
                continue

            small_image = pygame.transform.smoothscale(
                image,
                (40, 40)
            )

            self.screen.blit(
                small_image,
                (x, y)
            )

            x += 45

            if x > self.WINDOW_WIDTH - 45:

                x = self.BOARD_SIZE + 20
                y += 45

    # =====================================================
    # DRAW SIDE PANEL
    # =====================================================

    def draw_sidebar(self):

        pygame.draw.rect(
            self.screen,
            self.BACKGROUND_COLOR,
            (
                self.BOARD_SIZE,
                0,
                self.SIDEBAR_WIDTH,
                self.WINDOW_HEIGHT
            )
        )

        font = pygame.font.Font(
            None,
            30
        )

        title = font.render(
            "CHESS",
            True,
            self.TEXT_COLOR
        )

        self.screen.blit(
            title,
            (
                self.BOARD_SIZE + 60,
                10
            )
        )

    # =====================================================
    # CONVERT MOUSE → BOARD SQUARE
    # =====================================================

    def get_board_square(self, mouse_position):

        mouse_x, mouse_y = mouse_position

        # Click outside board
        if mouse_x < 0:
            return None

        if mouse_x >= self.BOARD_SIZE:
            return None

        if mouse_y < 0:
            return None

        if mouse_y >= self.BOARD_SIZE:
            return None

        col = mouse_x // self.SQUARE_SIZE
        row = mouse_y // self.SQUARE_SIZE

        return row, col

    # =====================================================
    # SELECT PIECE
    # =====================================================

    def select_piece(self, square, board):

        if square is None:
            return False

        row, col = square

        piece = board[row][col]

        # Empty square
        if piece == "--" or piece is None:

            self.selected_square = None
            self.possible_moves = []

            return False

        # Select piece
        self.selected_square = square

        return True

    # =====================================================
    # SET POSSIBLE MOVES
    # =====================================================

    def set_possible_moves(self, moves):

        """
        Called by Member 3's Movement Engine.

        Example:

        [
            (5, 4),
            (4, 4)
        ]
        """

        self.possible_moves = moves

    # =====================================================
    # CLEAR SELECTION
    # =====================================================

    def clear_selection(self):

        self.selected_square = None
        self.possible_moves = []

    # =====================================================
    # SET LAST MOVE
    # =====================================================

    def set_last_move(
        self,
        start_square,
        end_square
    ):

        self.last_move = (
            start_square,
            end_square
        )

    # =====================================================
    # ADD CAPTURED PIECE
    # =====================================================

    def add_captured_piece(self, piece):

        if piece is None:
            return

        if piece == "--":
            return

        self.captured_pieces.append(piece)

    # =====================================================
    # DRAW EVERYTHING
    # =====================================================

    def draw(self, board):

        self.screen.fill(
            self.BACKGROUND_COLOR
        )

        # Board
        self.draw_board()

        # Last move
        self.draw_last_move()

        # Possible moves
        self.draw_possible_moves()

        # Selected square
        self.draw_selected_square()

        # Pieces
        self.draw_pieces(board)

        # Coordinates
        self.draw_coordinates()

        # Sidebar
        self.draw_sidebar()

        # Captured pieces
        self.draw_captured_pieces()

        pygame.display.flip()

    # =====================================================
    # HANDLE MOUSE EVENTS
    # =====================================================

    def handle_events(self, board):

        for event in pygame.event.get():

            # Close window
            if event.type == pygame.QUIT:

                return False

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    square = self.get_board_square(
                        event.pos
                    )

                    if square is None:
                        continue

                    selected = self.select_piece(
                        square,
                        board
                    )

                    if selected:

                        print(
                            "Selected:",
                            board[
                                square[0]
                            ][
                                square[1]
                            ],
                            "Square:",
                            square
                        )

        return True

    # =====================================================
    # RUN GUI
    # =====================================================

    def run(self, board):

        running = True

        while running:

            running = self.handle_events(
                board
            )

            self.draw(board)

            self.clock.tick(60)

        pygame.quit()