import tkinter as tk
import numpy as np
import random


def initialize_window(win_root):
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


def change_colour(rectangle, canvas, target_color=None):
    if target_color is None:
        target_color = 'black'
    canvas.itemconfig(rectangle, fill=target_color)


class Simulation:
    def __init__(self):
        self.root = tk.Tk()
        self.step_count = 0
        self.root.geometry('1000x1000')
        self.canv, self.rect_array = initialize_window(self.root)
        self.canv.pack()
        self.main_button = tk.Button(
            self.root, text="Start", command=lambda: self.start())
        self.main_button.pack(side=tk.LEFT)
        tk.Button(self.root, text="Step", command=lambda: change_colour(
            self.rect_array[5][5], self.canv)).pack(side=tk.RIGHT)
        tk.mainloop()

    def start(self):
        global interrupt
        interrupt = False
        self.main_button.configure(text="Stop", command=lambda: self.stop())
        self.step()
        tk.mainloop()

    def step(self):
        global interrupt
        if interrupt:
            return
        # Check the rules
        self.step_count += 1
        print('Stepping', self.step_count)
        # To include processing of neighbours and all colour changes based on the rules.
        change_colour(self.rect_array[5][5], self.canv,
                      target_color=random.choice(['green', 'blue']))
        self.canv.after(10, self.step)

    def stop(self):
        self.main_button.configure(text="Start", command=lambda: self.start())
        global interrupt
        interrupt = True


if __name__ == '__main__':
    interrupt = False
    simulation = Simulation()
    # end_timer = 30
    # i = 0
