import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from copy import deepcopy
import random
from collections import deque
import os

# PATH SETUP 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CONSTANTS 

TILE = 160
BOARD_SIZE = 480
BG_COLOR = "misty rose"

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#  DP TABLE 

dp_table = {}


def build_dp_table():
    if dp_table:
        return

    queue = deque([GOAL_STATE])
    dp_table[GOAL_STATE] = None

    while queue:
        curr = queue.popleft()

        idx = curr.index(0)
        r, c = divmod(idx, 3)

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                ni = nr * 3 + nc
                nxt = list(curr)
                nxt[idx], nxt[ni] = nxt[ni], nxt[idx]
                nxt = tuple(nxt)

                if nxt not in dp_table:
                    dp_table[nxt] = curr
                    queue.append(nxt)

