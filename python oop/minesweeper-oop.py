from tkinter import * 
import settings
import utils
from cell import Cell

root = Tk() # root is conventional name for the main window

# override the settings of the window
root.configure(bg="black") # set the background color to black
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # set the dimensions of the window
root.title("minesweeper")
root.resizable(False, False) # prevent the window from being resized

top_frame = Frame(
    root, 
    bg="white",
    width=1440,
    height=utils.height_prct(25)

)
top_frame.place(x=0, y=0)

# enter rows & columns
def submit():
    rows = row_var.get()
    columns = col_var.get()

row_var = IntVar()
row_entry = Entry(root, textvariable= row_var, width=10, bg="white")
row_entry.place(x=10, y=10)

left_frame = Frame(
    root, 
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
    relief='raised'
)
left_frame.place(x=0, y=180)

# customisable minefield size & mine count?

center_frame = Frame(
    root, 
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25), 
    y=utils.height_prct(25)
)

# generating minefield
for x in range(settings.GRID):
    for y in range(settings.GRID):
        cell = Cell(x,y)
        cell.create_btn_obj(center_frame)
        cell.cell_btn_object.grid(
            row=x, column=y
        )

# create the label for the cell count
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.grid(row=0, column=0)

# create the label for the mine count
Cell.create_mine_count_label(left_frame)
Cell.mine_count_label_obj.grid(row=1, column=0)

Cell.randomise_mines()

# run the window
root.mainloop() # will keep the window open until we close it

