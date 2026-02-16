import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from copy import deepcopy
from collections import deque
import random
import os

# CONSTANTS 

TILE = 160
BOARD_SIZE = 480
BG_COLOR = "misty rose"

GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DP (BFS) SOLVER 

def state_to_string(state):
    return ''.join(str(cell) for row in state for cell in row)

def string_to_state(s):
    nums = list(map(int, s))
    return [nums[i:i+3] for i in range(0, 9, 3)]

def find_zero(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

