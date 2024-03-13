from tkinter import Button, Label
import random
import settings

class Cell:
    all = []
    cell_count_label_obj = None
    mine_count_label_obj = None
    cell_count = settings.GRID ** 2
    mine_count = 10

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x 
        self.y = y
        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=10,
            height=5,
            text=""        
            )
        btn.bind("<Button-1>", self.left_click) # left click
        btn.bind("<Button-3>", self.right_click) # right click
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f'Cells Left: {Cell.cell_count}',
            width=12,
            height=5,
            font=("Arial", 20)
        )
        Cell.cell_count_label_obj = lbl

    @staticmethod
    def create_mine_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f'Mines Left: {Cell.mine_count}',
            width=12,
            height=5,
            font=("Arial", 20)
        )
        Cell.mine_count_label_obj = lbl

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:  
            if self.surrounding_cells_mines == 0:
                for cell in self.surrounding_cells:
                    cell.show_adjacent_mines()
            self.show_adjacent_mines()
    
    def get_cell(self, x, y): # return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        return None

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x, self.y + 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_cells_mines(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_adjacent_mines(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.config(text=self.surrounding_cells_mines)
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.config(
                    text=f'Cells Left: {Cell.cell_count}'
                )
        # mark cell as opened
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.config(text="X")

    def right_click(self, event):
        if self.cell_btn_object["bg"] != "red":
            self.cell_btn_object.config(bg="red")
            Cell.mine_count -= 1
            if Cell.mine_count_label_obj:
                Cell.mine_count_label_obj.config(
                    text=f'Mines Left: {Cell.mine_count}'
                )
        else:
            self.cell_btn_object.config(bg="SystemButtonFace")
            Cell.mine_count += 1
            Cell.mine_count_label_obj.config(text=f'Mines Left: {Cell.mine_count}')

    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(Cell.all, 10)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell at {self.x},{self.y}"