class Cell:
    def __init__(self, coordinate):
        self.y_coordinate = coordinate[0]
        self.x_coordinate = coordinate[1]
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.square_number = -1
        self.row_number = -1
        self.column_number = -1

    def update_square_number(self, square_number):
        self.square_number = square_number

    def update_row_number(self, row_number):
        self.row_number = row_number

    def update_column_number(self, column_number):
        self.column_number = column_number

    def update_possible_numbers(self, number):
        number = int(number)
        if number in self.possible_numbers:
            self.possible_numbers.remove(number)

    def final_number(self):
        if len(self.possible_numbers) == 1:
            return self.possible_numbers[0]

