import pygame
from piece_renderer import PieceRenderer


class ChessGUI:

    def __init__(self, board_size=640):

        pygame.init()

        # Window
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

        # Board colors
        self.LIGHT_SQUARE = (240, 217, 181)
        self.DARK_SQUARE = (181, 136, 99)

        # Highlight colors
        self.SELECTED_COLOR = (255, 215, 0)
        self.MOVE_COLOR = (80, 180, 80)
        self.LAST_MOVE_COLOR = (100, 150, 220)

        # GUI colors
        self.BACKGROUND_COLOR = (35, 35, 35)
        self.TEXT_COLOR = (255, 255, 255)

        # State
        self.selected_square = None
        self.possible_moves = []
        self.captured_pieces = []
        self.last_move = None

        # Piece renderer
        self.piece_renderer = PieceRenderer(
            self.SQUARE_SIZE
        )

    # -----------------------------
    # BOARD
    # -----------------------------

    def draw_board(self):

        for row in range(8):
            for col in range(8):

                color = (
                    self.LIGHT_SQUARE
                    if (row + col) % 2 == 0
                    else self.DARK_SQUARE
                )

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        col * self.SQUARE_SIZE,
                        row * self.SQUARE_SIZE,
                        self.SQUARE_SIZE,
                        self.SQUARE_SIZE
                    )
                )

    def draw_coordinates(self):

        font = pygame.font.Font(None, 18)

        files = "abcdefgh"
        ranks = "87654321"

        for col in range(8):

            x = (
                col * self.SQUARE_SIZE
                + self.SQUARE_SIZE
                - 12
            )

            text = font.render(
                files[col],
                True,
                (80, 80, 80)
            )

            self.screen.blit(
                text,
                (x, self.BOARD_SIZE - 18)
            )

        for row in range(8):

            text = font.render(
                ranks[row],
                True,
                (80, 80, 80)
            )

            self.screen.blit(
                text,
                (5, row * self.SQUARE_SIZE + 5)
            )

    # -----------------------------
    # HIGHLIGHTS
    # -----------------------------

    def draw_last_move(self):

        if self.last_move is None:
            return

        for row, col in self.last_move:

            surface = pygame.Surface(
                (
                    self.SQUARE_SIZE,
                    self.SQUARE_SIZE
                ),
                pygame.SRCALPHA
            )

            surface.fill(
                (*self.LAST_MOVE_COLOR, 80)
            )

            self.screen.blit(
                surface,
                (
                    col * self.SQUARE_SIZE,
                    row * self.SQUARE_SIZE
                )
            )

    def draw_selected_square(self):

        if self.selected_square is None:
            return

        row, col = self.selected_square

        pygame.draw.rect(
            self.screen,
            self.SELECTED_COLOR,
            (
                col * self.SQUARE_SIZE,
                row * self.SQUARE_SIZE,
                self.SQUARE_SIZE,
                self.SQUARE_SIZE
            ),
            5
        )

    def draw_possible_moves(self):

        for row, col in self.possible_moves:

            center = (
                col * self.SQUARE_SIZE
                + self.SQUARE_SIZE // 2,
                row * self.SQUARE_SIZE
                + self.SQUARE_SIZE // 2
            )

            pygame.draw.circle(
                self.screen,
                self.MOVE_COLOR,
                center,
                10
            )

    # -----------------------------
    # SIDEBAR
    # -----------------------------

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

        font = pygame.font.Font(None, 30)

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

        font = pygame.font.Font(None, 25)

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

        self.piece_renderer.draw_captured_pieces(
            self.screen,
            self.captured_pieces,
            self.BOARD_SIZE,
            self.WINDOW_WIDTH
        )

    # -----------------------------
    # MOUSE / SELECTION
    # -----------------------------

    def get_board_square(self, mouse_position):

        mouse_x, mouse_y = mouse_position

        if not (
            0 <= mouse_x < self.BOARD_SIZE
            and 0 <= mouse_y < self.BOARD_SIZE
        ):
            return None

        col = mouse_x // self.SQUARE_SIZE
        row = mouse_y // self.SQUARE_SIZE

        return row, col

    def select_piece(self, square, board):

        if square is None:
            return False

        row, col = square
        piece = board[row][col]

        if piece == "--" or piece is None:
            self.clear_selection()
            return False

        self.selected_square = square

        return True

    def set_possible_moves(self, moves):
        self.possible_moves = moves

    def clear_selection(self):
        self.selected_square = None
        self.possible_moves = []

    def set_last_move(self, start_square, end_square):
        self.last_move = (
            start_square,
            end_square
        )

    def add_captured_piece(self, piece):

        if piece is not None and piece != "--":
            self.captured_pieces.append(piece)

    # -----------------------------
    # DRAW
    # -----------------------------

    def draw(self, board):

        self.screen.fill(
            self.BACKGROUND_COLOR
        )

        self.draw_board()
        self.draw_last_move()
        self.draw_possible_moves()
        self.draw_selected_square()

        self.piece_renderer.draw_pieces(
            self.screen,
            board
        )

        self.draw_coordinates()
        self.draw_sidebar()

        pygame.display.flip()

    # -----------------------------
    # EVENTS
    # -----------------------------

    def handle_events(self, board):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button != 1:
                    continue

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
                        board[square[0]][square[1]],
                        "Square:",
                        square
                    )

        return True

    # -----------------------------
    # RUN
    # -----------------------------

    def run(self, board):

        running = True

        while running:

            running = self.handle_events(board)

            self.draw(board)

            self.clock.tick(60)

        pygame.quit()