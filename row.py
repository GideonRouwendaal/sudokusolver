class Row:
    def __init__(self, number):
        self.cell_list = []
        self.row_number = number

    def add_cell(self, cell):
        cell.update_row_number(self.row_number)
        self.cell_list.append(cell)
