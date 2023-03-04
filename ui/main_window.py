import tkinter
from tkinter import *

PLAYING_GRID_NUM_ROWS = 3
PLAYING_GRID_NUM_COLS = 3

main_window = tkinter.Tk()
main_window.title('Tic Tac Toe')

playing_grid = Frame(main_window)
playing_grid.pack()

for row in range(1, PLAYING_GRID_NUM_ROWS):
    for col in range(1, PLAYING_GRID_NUM_COLS):
        button = Button(playing_grid, text='', height=2, width=4)
        button.pack()

main_window.mainloop()
