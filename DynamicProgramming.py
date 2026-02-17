import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from copy import deepcopy
import random
from collections import deque
import os

# PATH SETUP 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#  CONSTANTS 

TILE = 160
BOARD_SIZE = 480
BG_COLOR = "misty rose"


class PuzzleApp:
        def find_zero(self, state):
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    return r, c

    def move_user(self, r, c):
        if not self.round_active or self.ai_solving or self.user_finished:
            return

        zr, zc = self.find_zero(self.user_state)

        if abs(r - zr) + abs(c - zc) == 1:
            self.user_state[zr][zc], self.user_state[r][c] = self.user_state[r][c], 0
            self.user_steps += 1
            self.update_boards()

            if self.user_state == self.goal_grid:
                self.user_finished = True
                self.round_active = False
                self.status_lbl.config(text="Status: User solved. Click AI Solve for result.")
                messagebox.showinfo("User Solved", f"You solved it in {self.user_steps} moves.")
