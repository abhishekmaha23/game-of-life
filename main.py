import tkinter as tk
import numpy as np
from time import sleep
import random


class Simulation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        self.canv, self.rect_array = self.initialize_window(self.root)
        self.canv.pack()
        tk.Button(self.root, text="Step", command=lambda: self.change_colour(self.rect_array[5][5], self.canv)).pack()
        self.step()
        # tk.mainloop()
        end_timer = 300
        i = 0
        while i < end_timer:
            sleep(0.3)
            self.step()
            self.root.update_idletasks()
            self.root.update()
            i += 1

    def initialize_window(self, win_root):
        init_state_array = np.zeros(shape=(30, 30))
        canvas = tk.Canvas(win_root, height=903, width=903, bg='white')
        rect_main_array = []
        for row, row_val in enumerate(init_state_array):
            rect_row_list = []
            for col, col_val in enumerate(row_val):
                x1 = (row * 30) + 3
                x2 = (x1 + 30)
                y1 = (col * 30) + 3
                y2 = (y1 + 30)
                rect_row_list.append(
                    canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='grey', width='3'))
            rect_main_array.append(rect_row_list)
        return canvas, rect_main_array

    def change_colour(self, rectangle, canvas, target_color=None):
        if target_color is None:
            target_color = 'black'
        canvas.itemconfig(rectangle, fill=target_color)

    def step(self):
        # Check the rules
        print('Stepping')
        self.change_colour(self.rect_array[5][5], self.canv, target_color=random.choice(['green', 'blue']))


if __name__ == '__main__':
    simulation = Simulation()
    end_timer = 30
    i = 0
