class Column:
    def __init__(self, number):
        self.cell_list = []
        self.column_number = number

    def add_cell(self, cell):
        cell.update_column_number(self.column_number)
        self.cell_list.append(cell)
