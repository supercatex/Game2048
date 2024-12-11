import numpy as np

def move_left(board):
    b = board.copy()
    for i in range(4):
        for j in range(1, 4):
            kk = j
            for k in range(j - 1, -1, -1):
                if b[i][k] == 0:
                    kk = k
                elif b[i][k] == b[i][j]:
                    kk = k
                    break
                else:
                    break
            if kk != j:
                if b[i][kk] == 0:
                    b[i][kk] = b[i][j]
                    b[i][j] = 0
                else:
                    b[i][kk] = b[i][j] * 2
                    b[i][j] = 0
    return b

def move_right(board):
    b = board.copy()
    for i in range(4):
        for j in range(2, -1, -1):
            kk = j
            for k in range(j + 1, 4, 1):
                if b[i][k] == 0:
                    kk = k
                elif b[i][k] == b[i][j]:
                    kk = k
                    break
                else:
                    break
            if kk != j:
                if b[i][kk] == 0:
                    b[i][kk] = b[i][j]
                    b[i][j] = 0
                else:
                    b[i][kk] = b[i][j] * 2
                    b[i][j] = 0
    return b

def move_up(board):
    b = board.copy()
    for j in range(4):
        for i in range(1, 4):
            kk = i
            for k in range(i - 1, -1, -1):
                if b[k][j] == 0:
                    kk = k
                elif b[k][j] == b[i][j]:
                    kk = k
                    break
                else:
                    break
            if kk != i:
                if b[kk][j] == 0:
                    b[kk][j] = b[i][j]
                    b[i][j] = 0
                else:
                    b[kk][j] = b[i][j] * 2
                    b[i][j] = 0
    return b

def move_down(board):
    b = board.copy()
    for j in range(4):
        for i in range(2, -1, -1):
            kk = i
            for k in range(i + 1, 4, 1):
                if b[k][j] == 0:
                    kk = k
                elif b[k][j] == b[i][j]:
                    kk = k
                    break
                else:
                    break
            if kk != i:
                if b[kk][j] == 0:
                    b[kk][j] = b[i][j]
                    b[i][j] = 0
                else:
                    b[kk][j] = b[i][j] * 2
                    b[i][j] = 0
    return b

def ai_random(board):
    c = ["left", "down", "up", "right"]
    return np.random.choice(c)

def ai_greedy(board):
    if not np.array_equal(move_left(board), board):
        return "left"
    elif not np.array_equal(move_down(board), board):
        return "down"
    elif not np.array_equal(move_up(board), board):
        return "up"
    else:
        return "right"

def play(board):
    return ai_greedy(board)
