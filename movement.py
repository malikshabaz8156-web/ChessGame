BOARD_SIZE = 8

def is_inside_board(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

print(is_inside_board(3, 4))
print(is_inside_board(7, 7))
print(is_inside_board(8, 3))

def is_white(piece):
    return piece is not None and piece[0] == 'w'

print(is_white('wP'))
print(is_white('bP'))
print(is_white(None))

def is_black(piece):
    return piece is not None and piece[0] == 'b'

print(is_black('wP'))
print(is_black('bP'))
print(is_black(None))

def is_same_color(piece1, piece2):
    if piece1 is None or piece2 is None:
        return False

    return piece1[0] == piece2[0]

print(is_same_color('wP', 'wR'))
print(is_same_color('bP', 'bR'))
print(is_same_color('wP', 'bR'))
print(is_same_color('wP', None))
print(is_same_color(None, 'bR'))
print(is_same_color(None, None))

