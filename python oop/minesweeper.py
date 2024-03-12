from tkinter import *

root = Tk() # root is conventional name for the main window
root.configure(bg="black") # set the background color to black
root.geometry("1440x720") # set the dimensions of the window
root.title("minesweeper")
root.resizable(False, False) # prevent the window from being resized
root.mainloop() # will keep the window open until we close it

