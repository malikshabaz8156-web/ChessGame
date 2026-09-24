# ============================================
# PHASE 4 - PIECE MOVEMENT ENGINE
# ============================================

# Board representation:
# White pieces: WP, WR, WN, WB, WQ, WK
# Black pieces: BP, BR, BN, BB, BQ, BK
# Empty square: None


# ============================================
# 1. BOARD
# ============================================

board = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
]


# ============================================
# 2. BOARD BOUNDARY CHECK
# ============================================

def is_inside_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8


# ============================================
# 3. FRIENDLY / ENEMY PIECE CHECK
# ============================================

def is_friendly(piece1, piece2):
    return piece1[0] == piece2[0]


def is_enemy(piece1, piece2):
    return piece1[0] != piece2[0]


# ============================================
# 4. SLIDING MOVEMENT
# Used by:
# Rook
# Bishop
# Queen
# ============================================

def get_sliding_moves(board, row, col, directions):

    moves = []

    piece = board[row][col]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        while is_inside_board(new_row, new_col):

            target = board[new_row][new_col]

            # Empty square
            if target is None:

                moves.append((new_row, new_col))

            # Friendly piece
            elif is_friendly(piece, target):

                # Cannot move onto friendly piece
                # and cannot move beyond it
                break

            # Enemy piece
            else:

                # Can capture enemy piece
                moves.append((new_row, new_col))

                # Cannot move beyond enemy piece
                break

            new_row += dr
            new_col += dc

    return moves


# ============================================
# 5. PAWN MOVEMENT
# ============================================

def get_pawn_moves(board, row, col):

    moves = []

    piece = board[row][col]

    color = piece[0]

    # White moves upward
    # Black moves downward

    if color == "W":
        direction = -1
        starting_row = 6

    else:
        direction = 1
        starting_row = 1

    # ----------------------------------------
    # ONE-SQUARE FORWARD MOVEMENT
    # ----------------------------------------

    new_row = row + direction

    if is_inside_board(new_row, col):

        # Pawn can move forward only if square is empty
        if board[new_row][col] is None:

            moves.append((new_row, col))

            # --------------------------------
            # TWO-SQUARE FIRST MOVEMENT
            # --------------------------------

            if row == starting_row:

                two_row = row + (2 * direction)

                if (
                    is_inside_board(two_row, col)
                    and board[two_row][col] is None
                ):
                    moves.append((two_row, col))

    # ----------------------------------------
    # DIAGONAL CAPTURE
    # ----------------------------------------

    for dc in [-1, 1]:

        new_col = col + dc

        if is_inside_board(new_row, new_col):

            target = board[new_row][new_col]

            # Pawn can capture only an enemy piece
            if target is not None and is_enemy(piece, target):

                moves.append((new_row, new_col))

    return moves


# ============================================
# 6. ROOK MOVEMENT
# ============================================

def get_rook_moves(board, row, col):

    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    return get_sliding_moves(
        board,
        row,
        col,
        directions
    )


# ============================================
# 7. KNIGHT MOVEMENT
# ============================================

def get_knight_moves(board, row, col):

    moves = []

    piece = board[row][col]

    # All possible L-shaped movements

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

        # Check board boundaries
        if not is_inside_board(new_row, new_col):
            continue

        target = board[new_row][new_col]

        # Empty square
        if target is None:

            moves.append((new_row, new_col))

        # Enemy piece
        elif is_enemy(piece, target):

            moves.append((new_row, new_col))

        # Friendly piece
        # Do nothing

    return moves


# ============================================
# 8. BISHOP MOVEMENT
# ============================================

def get_bishop_moves(board, row, col):

    directions = [
        (-1, -1),   # Up-left
        (-1, 1),    # Up-right
        (1, -1),    # Down-left
        (1, 1)      # Down-right
    ]

    return get_sliding_moves(
        board,
        row,
        col,
        directions
    )


# ============================================
# 9. QUEEN MOVEMENT
# ============================================

def get_queen_moves(board, row, col):

    directions = [

        # Rook-like movement
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),

        # Bishop-like movement
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    return get_sliding_moves(
        board,
        row,
        col,
        directions
    )


# ============================================
# 10. KING MOVEMENT
# ============================================

def get_king_moves(board, row, col):

    moves = []

    piece = board[row][col]

    directions = [
        (-1, -1),   # Up-left
        (-1, 0),    # Up
        (-1, 1),    # Up-right

        (0, -1),    # Left
        (0, 1),     # Right

        (1, -1),    # Down-left
        (1, 0),     # Down
        (1, 1)      # Down-right
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        # Board boundary
        if not is_inside_board(new_row, new_col):
            continue

        target = board[new_row][new_col]

        # Empty square
        if target is None:

            moves.append((new_row, new_col))

        # Enemy piece
        elif is_enemy(piece, target):

            moves.append((new_row, new_col))

        # Friendly piece
        # Do nothing

    return moves


# ============================================
# 11. MAIN MOVE GENERATOR
# ============================================

def get_possible_moves(board, row, col):

    # Check whether coordinates are valid

    if not is_inside_board(row, col):
        return []

    piece = board[row][col]

    # Empty square
    if piece is None:
        return []

    piece_type = piece[1]

    # Pawn
    if piece_type == "P":
        return get_pawn_moves(board, row, col)

    # Rook
    elif piece_type == "R":
        return get_rook_moves(board, row, col)

    # Knight
    elif piece_type == "N":
        return get_knight_moves(board, row, col)

    # Bishop
    elif piece_type == "B":
        return get_bishop_moves(board, row, col)

    # Queen
    elif piece_type == "Q":
        return get_queen_moves(board, row, col)

    # King
    elif piece_type == "K":
        return get_king_moves(board, row, col)

    return []


# ============================================
# 12. DISPLAY BOARD
# ============================================

def display_board(board):

    print("\n    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for row in range(8):

        print(
            8 - row,
            "|",
            end=" "
        )

        for col in range(8):

            piece = board[row][col]

            if piece is None:
                piece = "  "

            print(piece, "|", end=" ")

        print(8 - row)

        print(
            "  +---+---+---+---+---+---+---+---+"
        )

    print("    a   b   c   d   e   f   g   h")


# ============================================
# 13. CONVERT COORDINATES TO CHESS NOTATION
# ============================================

def position_to_notation(row, col):

    files = "abcdefgh"

    file = files[col]

    rank = str(8 - row)

    return file + rank


# ============================================
# 14. DISPLAY POSSIBLE MOVES
# ============================================

def display_possible_moves(board, row, col):

    piece = board[row][col]

    if piece is None:

        print("There is no piece at this position.")
        return

    moves = get_possible_moves(
        board,
        row,
        col
    )

    print(
        "\nPiece:",
        piece
    )

    print(
        "Current position:",
        position_to_notation(row, col)
    )

    print(
        "Possible moves:"
    )

    if len(moves) == 0:

        print("No possible moves.")

    else:

        for move in moves:

            move_row, move_col = move

            print(
                position_to_notation(
                    move_row,
                    move_col
                )
            )


# ============================================
# 15. TESTING
# ============================================

if __name__ == "__main__":

    # Display initial board

    display_board(board)

    # ----------------------------------------
    # Example 1
    # White pawn at e2
    # ----------------------------------------

    print("\n--- TEST 1: WHITE PAWN ---")

    display_possible_moves(
        board,
        6,
        4
    )


    # ----------------------------------------
    # Example 2
    # White knight at b1
    # ----------------------------------------

    print("\n--- TEST 2: WHITE KNIGHT ---")

    display_possible_moves(
        board,
        7,
        1
    )


    # ----------------------------------------
    # Example 3
    # White bishop at c1
    # ----------------------------------------

    print("\n--- TEST 3: WHITE BISHOP ---")

    display_possible_moves(
        board,
        7,
        2
    )


    # ----------------------------------------
    # Example 4
    # White rook at a1
    # ----------------------------------------

    print("\n--- TEST 4: WHITE ROOK ---")

    display_possible_moves(
        board,
        7,
        0
    )


    # ----------------------------------------
    # Example 5
    # White queen at d1
    # ----------------------------------------

    print("\n--- TEST 5: WHITE QUEEN ---")

    display_possible_moves(
        board,
        7,
        3
    )


    # ----------------------------------------
    # Example 6
    # White king at e1
    # ----------------------------------------

    print("\n--- TEST 6: WHITE KING ---")

    display_possible_moves(
        board,
        7,
        4
    )