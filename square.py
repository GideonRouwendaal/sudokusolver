class Square:
    def __init__(self, number):
        self.cell_list = []
        self.square_number = number

    def add_cell(self, cell):
        cell.update_square_number(self.square_number)
        self.cell_list.append(cell)
