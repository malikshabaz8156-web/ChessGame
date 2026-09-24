class Game:
    """
    Game Controller

    Responsible for:
    - Managing player turns
    - Selecting pieces
    - Processing moves
    - Maintaining move history
    - Tracking captured pieces
    - Managing game status
    - Pause / resume
    - Restarting the game
    """

    def __init__(self, board):
        self.board = board

        # Current turn
        self.current_player = "white"

        # Selected piece
        self.selected_piece = None

        # Previous move
        self.previous_move = None

        # Captured pieces
        self.captured_pieces = {
            "white": [],
            "black": []
        }

        # Move history
        self.move_history = []

        # Game state
        self.game_status = "playing"
        self.paused = False
        self.winner = None

    # ==================================================
    # TURN MANAGEMENT
    # ==================================================

    def get_current_player(self):
        return self.current_player

    def change_turn(self):
        """Change the turn after a successful move."""

        if self.current_player == "white":
            self.current_player = "black"
        else:
            self.current_player = "white"

    # ==================================================
    # PIECE SELECTION
    # ==================================================

    def select_piece(self, position):
        """
        Select a piece from the board.

        position = (row, column)
        """

        piece = self.board.get_piece(position)

        # No piece at this position
        if piece is None:
            return False

        # Check whether the piece belongs
        # to the current player
        if not self.is_correct_player(piece):
            return False

        self.selected_piece = position

        return True

    def deselect_piece(self):
        """Deselect the currently selected piece."""

        self.selected_piece = None

    def is_correct_player(self, piece):
        """Check whether the selected piece belongs
        to the current player."""

        if hasattr(piece, "color"):
            return piece.color == self.current_player

        # If pieces are represented as strings
        if isinstance(piece, str):

            if piece.startswith("W"):
                return self.current_player == "white"

            if piece.startswith("B"):
                return self.current_player == "black"

        return False

    # ==================================================
    # MOVE PROCESSING
    # ==================================================

    def make_move(self, destination, rules):
        """
        Process a move from the selected square
        to the destination square.
        """

        # Game must be running
        if self.game_status != "playing":
            return False

        # Game must not be paused
        if self.paused:
            return False

        # A piece must be selected
        if self.selected_piece is None:
            return False

        source = self.selected_piece

        # Ask Rules module to validate the move
        if not rules.is_legal_move(
            self.board,
            source,
            destination,
            self.current_player
        ):
            return False

        # Check whether a piece will be captured
        captured_piece = self.board.get_piece(destination)

        # Move the piece on the board
        self.board.move_piece(source, destination)

        # Store captured piece
        if captured_piece is not None:
            self.captured_pieces[self.current_player].append(
                captured_piece
            )

        # Store the move
        self.previous_move = {
            "player": self.current_player,
            "from": source,
            "to": destination,
            "captured": captured_piece
        }

        # Add to history
        self.move_history.append(
            self.previous_move.copy()
        )

        # Clear selection
        self.selected_piece = None

        # Change player
        self.change_turn()

        # Check whether game has ended
        self.check_game_over(rules)

        return True

    # ==================================================
    # MOVE HISTORY
    # ==================================================

    def get_move_history(self):
        return self.move_history

    def get_previous_move(self):
        return self.previous_move

    # ==================================================
    # CAPTURED PIECES
    # ==================================================

    def get_captured_pieces(self, color):
        return self.captured_pieces[color]

    # ==================================================
    # GAME OVER
    # ==================================================

    def check_game_over(self, rules):
        """
        Check for checkmate or stalemate.
        """

        player = self.current_player

        # Checkmate
        if rules.is_checkmate(self.board, player):

            self.game_status = "checkmate"

            if player == "white":
                self.winner = "black"
            else:
                self.winner = "white"

            return

        # Stalemate
        if rules.is_stalemate(self.board, player):

            self.game_status = "stalemate"
            self.winner = None

    def is_game_over(self):
        return self.game_status != "playing"

    # ==================================================
    # PAUSE / RESUME
    # ==================================================

    def pause_game(self):

        if self.game_status == "playing":
            self.paused = True

    def resume_game(self):

        if self.game_status == "playing":
            self.paused = False

    def is_paused(self):
        return self.paused

    # ==================================================
    # RESTART
    # ==================================================

    def restart_game(self):

        # Reset board
        self.board.reset_board()

        # Reset turn
        self.current_player = "white"

        # Reset selection
        self.selected_piece = None

        # Reset previous move
        self.previous_move = None

        # Clear captured pieces
        self.captured_pieces = {
            "white": [],
            "black": []
        }

        # Clear move history
        self.move_history = []

        # Reset game state
        self.game_status = "playing"
        self.paused = False
        self.winner = None

    # ==================================================
    # GAME INFORMATION
    # ==================================================

    def get_game_status(self):
        return self.game_status

    def get_winner(self):
        return self.winner

    def get_selected_piece(self):
        return self.selected_piece