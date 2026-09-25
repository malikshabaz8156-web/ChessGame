# movement.py

BOARD_SIZE = 8


def is_inside_board(row, col):
    """Check whether a coordinate is inside the chessboard."""
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def get_pawn_moves(board, row, col):
    """
    Return all valid movement squares for a pawn.

    White pawn moves upward (-1).
    Black pawn moves downward (+1).

    Board pieces:
        WP = White Pawn
        BP = Black Pawn
        None = Empty square
    """

    piece = board[row][col]
    moves = []

    if piece not in ("WP", "BP"):
        return moves

    direction = -1 if piece == "WP" else 1
    start_row = 6 if piece == "WP" else 1

    new_row = row + direction

    if is_inside_board(new_row, col):

        if board[new_row][col] is None:

            moves.append((new_row, col))

            if row == start_row:

                new_row_2 = row + (2 * direction)

                if (
                    is_inside_board(new_row_2, col)
                    and board[new_row_2][col] is None
                ):
                    moves.append((new_row_2, col))

    for new_col in (col - 1, col + 1):

        new_row = row + direction

        if is_inside_board(new_row, new_col):

            target = board[new_row][new_col]

            if target is not None:

                if piece == "WP" and target.startswith("B"):
                    moves.append((new_row, new_col))

                elif piece == "BP" and target.startswith("W"):
                    moves.append((new_row, new_col))

    return moves


def get_rook_moves(board, row, col):
    """Return valid movement squares for a rook."""
    return []


def get_knight_moves(board, row, col):
    """Return valid movement squares for a knight."""
    return []


def get_bishop_moves(board, row, col):
    """Return valid movement squares for a bishop."""
    return []


def get_queen_moves(board, row, col):
    """Return valid movement squares for a queen."""
    return []


def get_king_moves(board, row, col):
    """Return valid movement squares for a king."""
    return []


def get_valid_moves(board, row, col):
    """Return all valid movement squares for the selected piece."""

    piece = board[row][col]

    if piece == "WP" or piece == "BP":
        return get_pawn_moves(board, row, col)

    elif piece == "WR" or piece == "BR":
        return get_rook_moves(board, row, col)

    elif piece == "WN" or piece == "BN":
        return get_knight_moves(board, row, col)

    elif piece == "WB" or piece == "BB":
        return get_bishop_moves(board, row, col)

    elif piece == "WQ" or piece == "BQ":
        return get_queen_moves(board, row, col)

    elif piece == "WK" or piece == "BK":
        return get_king_moves(board, row, col)

    return []