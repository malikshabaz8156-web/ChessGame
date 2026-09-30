BOARD_SIZE = 8


def is_inside_board(row, col):
    """Check whether a coordinate is inside the chessboard."""
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


def is_white(piece):
    """Check whether a piece is white."""
    return piece is not None and piece.startswith("W")


def is_black(piece):
    """Check whether a piece is black."""
    return piece is not None and piece.startswith("B")


def is_enemy(piece, target):
    """Check whether target is an opponent's piece."""
    if piece is None or target is None:
        return False

    return is_white(piece) != is_white(target)


def get_pawn_moves(board, row, col):
    """Return all valid movement squares for a pawn."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    if piece == "WP":
        direction = -1
        start_row = 6
    else:
        direction = 1
        start_row = 1

    new_row = row + direction

    if is_inside_board(new_row, col):
        if board[new_row][col] is None:
            moves.append((new_row, col))

            if row == start_row:
                two_row = row + (2 * direction)

                if board[two_row][col] is None:
                    moves.append((two_row, col))

    for dc in (-1, 1):
        new_col = col + dc

        if is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is not None and is_enemy(piece, target):
                moves.append((new_row, new_col))

    return moves


def get_rook_moves(board, row, col):
    """Return all valid movement squares for a rook."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        while is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is None:
                moves.append((new_row, new_col))
            else:
                if is_enemy(piece, target):
                    moves.append((new_row, new_col))
                break

            new_row += dr
            new_col += dc

    return moves


def get_knight_moves(board, row, col):
    """Return all valid movement squares for a knight."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    knight_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1)
    ]

    for dr, dc in knight_moves:
        new_row = row + dr
        new_col = col + dc

        if is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is None:
                moves.append((new_row, new_col))
            elif is_enemy(piece, target):
                moves.append((new_row, new_col))

    return moves


def get_bishop_moves(board, row, col):
    """Return all valid movement squares for a bishop."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        while is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is None:
                moves.append((new_row, new_col))
            else:
                if is_enemy(piece, target):
                    moves.append((new_row, new_col))
                break

            new_row += dr
            new_col += dc

    return moves


def get_queen_moves(board, row, col):
    """Return all valid movement squares for a queen."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        while is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is None:
                moves.append((new_row, new_col))
            else:
                if is_enemy(piece, target):
                    moves.append((new_row, new_col))
                break

            new_row += dr
            new_col += dc

    return moves


def get_king_moves(board, row, col):
    """Return all valid movement squares for a king."""

    moves = []
    piece = board[row][col]

    if piece is None:
        return moves

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if is_inside_board(new_row, new_col):
            target = board[new_row][new_col]

            if target is None:
                moves.append((new_row, new_col))
            elif is_enemy(piece, target):
                moves.append((new_row, new_col))

    return moves


def get_valid_moves(board, row, col):
    """Return movement squares for the selected chess piece."""

    if not is_inside_board(row, col):
        return []

    piece = board[row][col]

    if piece is None:
        return []

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