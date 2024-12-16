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

def add_random(board, t=(2, 4)):
    b = board.copy()
    a = np.argwhere(b == 0)
    c = np.random.randint(len(a))
    b[a[c][0]][a[c][1]] = np.random.choice(t)
    return b

def board_score(board):
    # k = np.max(board)
    return np.sum(board ** 2) #+ k ** len(np.argwhere(board == 0))

def random_walk(board, move=1):
    c = ["left", "down", "up", "right"]
    found = ""
    while len(found) == 0 and len(c) > 0:
        x = np.random.choice(c)
        if np.array_equal(eval("move_" + x + "(board)"), board):
            c.remove(x)
        else:
            found = x
    if len(found) == 0: return board_score(board) * pow(0.95, move), board, move
    b = eval("move_" + found + "(board)")
    b = add_random(b)
    s, bb, m = random_walk(b, move + 1)
    return board_score(board) + s * 0.95, bb, m

def ai_MCTS(board, t=300):
    c = ["left", "down", "up", "right"]
    d = np.array([0, 0, 0, 0])
    for i in range(4):
        b = eval("move_" + c[i] + "(board)")
        if np.array_equal(b, board): continue
        max_k, cnt_k, max_m = 0, 0, 0
        n = 0
        while n < t:
            bb = add_random(b, t=[n % 2 * 2 + 2])
            s, bb, move = random_walk(bb)
            if np.max(bb) > max_k:
                max_k = np.max(bb)
                cnt_k = 1
            elif np.max(bb) == max_k:
                cnt_k += 1
            max_m = max(max_m, move)
            n = n + 1
            d[i] += s * 0.001
        d[i] /= n
        print(c[i] + ":", max_k, "*", cnt_k, "(%d)" % max_m, end=", ")
    print()
    # e = d
    # if np.sum(d) > 0: e = e / np.sum(d)
    # print(e)
    # idx = np.random.choice(range(len(c)), p=e)
    # return c[idx]
    return c[np.argmax(d)]

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
    # if np.max(board) < 256:
    #     return ai_greedy(board)
    # return ai_MCTS(board)
    return ai_random(board)
