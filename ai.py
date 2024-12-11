import numpy as np

def ai_random(board):
    c = ["left", "down", "up", "right"]
    return np.random.choice(c)

def play(board):
    return ai_random(board)
