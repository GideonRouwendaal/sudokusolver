import time

from cell import Cell
from square import Square
from row import Row
from column import Column
import basicsudoku
import itertools
import tkinter as tk

board = basicsudoku.SudokuBoard()

ROWS = 9
COLUMNS = 9
SQUARES = 9

# 52
# board [x, y]

#############################Easy#############################
# # http://www.sudokuessentials.com/support-files/sudoku-easy-1.pdf
# # row 1
# board[0, 0] = 8
# board[3, 0] = 9
# board[4, 0] = 3
# board[8, 0] = 2
#
# # row 2
# board[2, 1] = 9
# board[7, 1] = 4
#
# # row 3
# board[0, 2] = 7
# board[2, 2] = 2
# board[3, 2] = 1
# board[6, 2] = 9
# board[7, 2] = 6
#
# # row 4
# board[0, 3] = 2
# board[7, 3] = 9
#
# # row 5
# board[1, 4] = 6
# board[7, 4] = 7
#
# # row 6
# board[1, 5] = 7
# board[5, 5] = 6
# board[8, 5] = 5
#
# # row 7
# board[1, 6] = 2
# board[2, 6] = 7
# board[5, 6] = 8
# board[6, 6] = 4
# board[8, 6] = 6
#
# # row 8
# board[1, 7] = 3
# board[6, 7] = 5
#
# # row 9
# board[0, 8] = 5
# board[4, 8] = 6
# board[5, 8] = 2
# board[8, 8] = 8

#############################Medium#############################
# http://www.mathsphere.co.uk/downloads/sudoku/10202-medium.pdf number 1
# row 1
# board[0, 0] = 6
# board[1, 0] = 5
# board[2, 0] = 9
# board[4, 0] = 1
# board[6, 0] = 2
# board[7, 0] = 8
#
# # row 2
# board[0, 1] = 1
# board[4, 1] = 5
# board[7, 1] = 3
#
# # row 3
# board[0, 2] = 2
# board[3, 2] = 8
# board[7, 2] = 1
#
#
# # row 4
# board[3, 3] = 1
# board[4, 3] = 3
# board[5, 3] = 5
# board[7, 3] = 7
#
# # row 5
# board[0, 4] = 8
# board[3, 4] = 9
# board[8, 4] = 2
#
# # row 6
# board[2, 5] = 3
# board[4, 5] = 7
# board[5, 5] = 8
# board[6, 5] = 6
# board[7, 5] = 4
#
#
# # row 7
# board[0, 6] = 3
# board[2, 6] = 2
# board[5, 6] = 9
# board[8, 6] = 4
#
# # row 8
# board[5, 7] = 1
# board[6, 7] = 8
#
# # row 9
# board[2, 8] = 8
# board[3, 8] = 7
# board[4, 8] = 6

############################Hard#############################
# # https://www.7sudoku.com/view-solution?date=20200618
# # row 1
# board[0, 0] = 7
# board[4, 0] = 8
# board[5, 0] = 6
#
# # row 2
# board[0, 1] = 1
# board[1, 1] = 5
# board[3, 1] = 7
# board[5, 1] = 3
#
# # row 3
# board[0, 2] = 9
# board[4, 2] = 4
# board[7, 2] = 7
#
# # row 4
# board[1, 3] = 4
# board[5, 3] = 7
# board[6, 3] = 8
# board[7, 3] = 6
#
# # row 6
# board[1, 5] = 7
# board[2, 5] = 5
# board[3, 5] = 8
# board[7, 5] = 2
#
# # row 7
# board[1, 6] = 9
# board[4, 6] = 1
# board[8, 6] = 2
#
# # row 8
# board[3, 7] = 3
# board[5, 7] = 2
# board[7, 7] = 5
# board[8, 7] = 6
#
# # row 9
# board[3, 8] = 6
# board[4, 8] = 7
# board[8, 8] = 3


################################Evil#############################
# https://www.websudoku.com/?level=8
# row 1
board[7, 0] = 7

# row 2
board[3, 1] = 9
board[8, 1] = 1

# row 3
board[1, 2] = 1
board[2, 2] = 5
board[3, 2] = 4
board[6, 2] = 2
board[8, 2] = 3

# row 4
board[1, 3] = 6
board[4, 3] = 1
board[5, 3] = 2

# row 5
board[0, 4] = 3
board[8, 4] = 2

# row 6
board[3, 5] = 5
board[4, 5] = 6
board[7, 5] = 8

# row 7
board[0, 6] = 4
board[2, 6] = 8
board[5, 6] = 6
board[6, 6] = 9
board[7, 6] = 2

# row 8
board[0, 7] = 7
board[5, 7] = 5

# row 9
board[1, 8] = 9


def create_list_empty_cells(board):
    empty_cell_list = []
    for i in range(COLUMNS):
        for j in range(ROWS):
            if board[j, i] == ".":
                empty_cell = Cell([i, j])
                fill_row_list(empty_cell, j)
                fill_column_list(empty_cell, i)
                empty_cell_list.append(empty_cell)
    return empty_cell_list


def create_square_list():
    square_list = []
    for number in range(SQUARES):
        square_list.append(Square(number))
    return square_list


def create_row_list():
    row_list = []
    for number in range(ROWS):
        row_list.append(Row(number))
    return row_list


def create_column_list():
    column_list = []
    for number in range(COLUMNS):
        column_list.append(Column(number))
    return column_list


def fill_row_list(cell, row_number):
    row_list[row_number].add_cell(cell)


def fill_column_list(cell, column_number):
    column_list[column_number].add_cell(cell)


def fill_square_list(square_list, empty_cell_list):
    for empty_cell in empty_cell_list:
        if empty_cell.x_coordinate in range(3):
            if empty_cell.y_coordinate in range(3):
                square_list[0].add_cell(empty_cell)
                empty_cell.update_square_number(0)
            elif empty_cell.y_coordinate in range(3, 6):
                square_list[1].add_cell(empty_cell)
                empty_cell.update_square_number(1)
            elif empty_cell.y_coordinate in range(6, 9):
                square_list[2].add_cell(empty_cell)
                empty_cell.update_square_number(2)
        elif empty_cell.x_coordinate in range(3, 6):
            if empty_cell.y_coordinate in range(3):
                square_list[3].add_cell(empty_cell)
                empty_cell.update_square_number(3)
            elif empty_cell.y_coordinate in range(3, 6):
                square_list[4].add_cell(empty_cell)
                empty_cell.update_square_number(4)
            elif empty_cell.y_coordinate in range(6, 9):
                square_list[5].add_cell(empty_cell)
                empty_cell.update_square_number(5)
        elif empty_cell.x_coordinate in range(6, 9):
            if empty_cell.y_coordinate in range(3):
                square_list[6].add_cell(empty_cell)
                empty_cell.update_square_number(6)
            elif empty_cell.y_coordinate in range(3, 6):
                square_list[7].add_cell(empty_cell)
                empty_cell.update_square_number(7)
            elif empty_cell.y_coordinate in range(6, 9):
                square_list[8].add_cell(empty_cell)
                empty_cell.update_square_number(8)
    return square_list


def which_row_range(cell):
    if cell.x_coordinate % 3 == 0:
        return [0, 1, 2]
    elif cell.x_coordinate == 1 or cell.x_coordinate == 4 or cell.x_coordinate == 7:
        return [-1, 0, 1]
    elif cell.x_coordinate == 2 or cell.x_coordinate == 5 or cell.x_coordinate == 8:
        return [0, -1, -2]


def which_column_range(cell):
    if cell.y_coordinate % 3 == 0:
        return [0, 1, 2]
    elif cell.y_coordinate == 1 or cell.y_coordinate == 4 or cell.y_coordinate == 7:
        return [-1, 0, 1]
    elif cell.y_coordinate == 2 or cell.y_coordinate == 5 or cell.y_coordinate == 8:
        return [-2, -1, 0]


def check_row(cell):
    for x in range(ROWS):
        number_on_board = board[x, cell.y_coordinate]
        if number_on_board != ".":
            cell.update_possible_numbers(number_on_board)


def check_column(cell):
    for y in range(COLUMNS):
        number_on_board = board[cell.x_coordinate, y]
        if number_on_board != ".":
            cell.update_possible_numbers(number_on_board)


def check_square(cell):
    row_range = which_row_range(cell)
    column_range = which_column_range(cell)
    for x in row_range:
        for y in column_range:
            number_on_board = board[cell.x_coordinate + x, cell.y_coordinate + y]
            if number_on_board != ".":
                cell.update_possible_numbers(number_on_board)


def update_square(square_number, number):
    for cell in square_list[square_number].cell_list:
        cell.update_possible_numbers(number)


def update_row(row_number, number):
    for cell in row_list[row_number].cell_list:
        cell.update_possible_numbers(number)


def update_column(column_number, number):
    for cell in column_list[column_number].cell_list:
        cell.update_possible_numbers(number)


def fill_cell(cell, number):
    board[cell.x_coordinate, cell.y_coordinate] = number
    square_list[cell.square_number].cell_list.remove(cell)
    update_square(cell.square_number, number)
    row_list[cell.row_number].cell_list.remove(cell)
    update_row(cell.row_number, number)
    column_list[cell.column_number].cell_list.remove(cell)
    update_column(cell.column_number, number)
    empty_cells_list.remove(cell)


def hidden_single_square(cell, possible_number):
    square = square_list[cell.square_number]
    for to_check_cell in square.cell_list:
        if possible_number in to_check_cell.possible_numbers:
            return None
    fill_cell(cell, possible_number)


def hidden_single_row(cell, possible_number):
    row = row_list[cell.row_number]
    for to_check_cell in row.cell_list:
        if possible_number in to_check_cell.possible_numbers:
            return None
    fill_cell(cell, possible_number)


def hidden_single_column(cell, possible_number):
    column = column_list[cell.column_number]
    for to_check_cell in column.cell_list:
        if possible_number in to_check_cell.possible_numbers:
            return None
    fill_cell(cell, possible_number)


def hidden_singles(cell):
    for possible_number in cell.possible_numbers:
        hidden_single_square(cell, possible_number)
        hidden_single_row(cell, possible_number)
        hidden_single_column(cell, possible_number)


def check_pair_square(combination, square_number):
    square = square_list[square_number]
    candidates = []
    for cell in square.cell_list:
        if len(cell.possible_numbers) == len(combination) and all(elem in combination for elem in cell.possible_numbers):
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in square.cell_list:
            if cell not in candidates:
                for number in combination:
                    cell.update_possible_numbers(number)


def check_pair_row(combination, row_number):
    row = row_list[row_number]
    candidates = []
    for cell in row.cell_list:
        if len(cell.possible_numbers) == len(combination) and all(elem in combination for elem in cell.possible_numbers):
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in row.cell_list:
            if cell not in candidates:
                for number in combination:
                    cell.update_possible_numbers(number)


def check_pair_column(combination, column_number):
    column = column_list[column_number]
    candidates = []
    for cell in column.cell_list:
        if len(cell.possible_numbers) == len(combination) and all(elem in combination  for elem in cell.possible_numbers):
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in column.cell_list:
            if cell not in candidates:
                for number in combination:
                    cell.update_possible_numbers(number)


def naked_multiples(cell):
    for i in range(len(cell.possible_numbers)):
        combinations = itertools.combinations(cell.possible_numbers, i + 2)
        for combination in combinations:
            check_pair_square(combination, cell.square_number)
            check_pair_row(combination, cell.row_number)
            check_pair_column(combination, cell.column_number)


def check_omission_row(cell, possible_number, cell_list):
    check = True
    for to_check_cell in cell_list:
        if to_check_cell.row_number != cell.row_number:
            if possible_number in to_check_cell.possible_numbers:
                check = False
                return check
    return check


def check_omission_column(cell, possible_number, cell_list):
    check = True
    for to_check_cell in cell_list:
        if to_check_cell.column_number != cell.column_number:
            if possible_number in to_check_cell.possible_numbers:
                check = False
                return check
    return check


def check_omission_square(cell, possible_number, cell_list):
    check = True
    for to_check_cell in cell_list:
        if to_check_cell.square_number != cell.square_number:
            if possible_number in to_check_cell.possible_numbers:
                check = False
                return check
    return check


def omission_square(cell, possible_number):
    square = square_list[cell.square_number]
    row = row_list[cell.row_number]
    column = column_list[cell.column_number]
    omission_row_check = check_omission_row(cell, possible_number, square.cell_list)
    omission_column_check = check_omission_column(cell, possible_number, square.cell_list)
    if omission_row_check:
        for to_update_cell in row.cell_list:
            if to_update_cell.square_number != cell.square_number:
                to_update_cell.update_possible_numbers(possible_number)
    if omission_column_check:
        for to_update_cell in column.cell_list:
            if to_update_cell.square_number != cell.square_number:
                to_update_cell.update_possible_numbers(possible_number)


def omission_row(cell, possible_number):
    square = square_list[cell.square_number]
    row = row_list[cell.row_number]
    column = column_list[cell.column_number]
    omission_square_check = check_omission_square(cell, possible_number, row.cell_list)
    omission_column_check = check_omission_column(cell, possible_number, row.cell_list)
    if omission_square_check:
        for to_update_cell in square.cell_list:
            if to_update_cell.row_number != cell.row_number:
                to_update_cell.update_possible_numbers(possible_number)
    if omission_column_check:
        for to_update_cell in column.cell_list:
            if to_update_cell.row_number != cell.row_number:
                to_update_cell.update_possible_numbers(possible_number)


def omission_column(cell, possible_number):
    square = square_list[cell.square_number]
    row = row_list[cell.row_number]
    column = column_list[cell.column_number]
    omission_square_check = check_omission_square(cell, possible_number, column.cell_list)
    omission_row_check = check_omission_row(cell, possible_number, column.cell_list)
    if omission_square_check:
        for to_update_cell in square.cell_list:
            if to_update_cell.column_number != cell.column_number:
                to_update_cell.update_possible_numbers(possible_number)
    if omission_row_check:
        for to_update_cell in row.cell_list:
            if to_update_cell.column_number != cell.column_number:
                to_update_cell.update_possible_numbers(possible_number)


def omission(cell):
    for possible_number in cell.possible_numbers:
        omission_square(cell, possible_number)
        omission_row(cell, possible_number)
        omission_column(cell, possible_number)


def check_hidden_square(combination, square_number):
    square = square_list[square_number]
    candidates = []
    for cell in square.cell_list:
        check = False
        for number in combination:
            if number in cell.possible_numbers:
                check = True
                break
        if check:
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in candidates:
            for possible_number in cell.possible_numbers:
                if possible_number not in combination:
                    cell.update_possible_numbers(possible_number)


def check_hidden_row(combination, row_number):
    row = row_list[row_number]
    candidates = []
    for cell in row.cell_list:
        check = False
        for number in combination:
            if number in cell.possible_numbers:
                check = True
                break
        if check:
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in candidates:
            for possible_number in cell.possible_numbers:
                if possible_number not in combination:
                    cell.update_possible_numbers(possible_number)


def check_hidden_column(combination, column_number):
    column = column_list[column_number]
    candidates = []
    for cell in column.cell_list:
        check = False
        for number in combination:
            if number in cell.possible_numbers:
                check = True
                break
        if check:
            candidates.append(cell)
    if len(combination) == len(candidates):
        for cell in candidates:
            for possible_number in cell.possible_numbers:
                if possible_number not in combination:
                    cell.update_possible_numbers(possible_number)


def hidden_multiples(cell):
    for i in range(len(cell.possible_numbers)):
        combinations = itertools.combinations(cell.possible_numbers, i + 2)
        for combination in combinations:
            check_hidden_square(combination, cell.square_number)
            check_hidden_row(combination, cell.row_number)
            check_hidden_column(combination, cell.column_number)


def update_swordfish(possible_number, cell_list):
    for cell in cell_list:
        row = row_list[cell.row_number]
        column = column_list[cell.column_number]
        for to_update_cell in row.cell_list:
            if to_update_cell not in cell_list:
                to_update_cell.update_possible_numbers(possible_number)
        for to_update_cell in column.cell_list:
            if to_update_cell not in cell_list:
                to_update_cell.update_possible_numbers(possible_number)


def check_swordfish(cell, possible_number):
    row_number = cell.row_number
    row = row_list[row_number]
    row_candidates = []
    column_number = cell.column_number
    column = column_list[column_number]
    column_candidates = []
    counter = 0
    for cell1 in row.cell_list:
        if counter < 2:
            if cell1 != cell and possible_number in cell1.possible_numbers:
                row_candidates.append(cell1)
                counter += 1
        else:
            return None
    if counter == 0:
        return None
    counter = 0
    for cell2 in column.cell_list:
        if counter < 2:
            if cell2 != cell and possible_number in cell2.possible_numbers:
                column_candidates.append(cell2)
        else:
            return None
    if counter == 0:
        return None
    cell1 = row_candidates[0]
    cell2 = column_candidates[0]
    final_4_cells = [cell, cell1, cell2]
    for cell3_pos in column_list[cell1.column_number].cell_list:
        if cell3_pos.row_number == cell2.row_number and possible_number in cell3_pos.possible_numbers:
            final_4_cells.append(cell3_pos)
            update_swordfish(possible_number, final_4_cells)


def swordfish(cell):
    for possible_number in cell.possible_numbers:
        check_swordfish(cell, possible_number)


def update_unique_rectangle(possible_numbers, to_update_cell):
    for number in possible_numbers:
        to_update_cell.update_possible_numbers(number)


def check_unique_rectangle(cell, possible_numbers):
    row = row_list[cell.row_number]
    row_candidates = []
    column = column_list[cell.column_number]
    column_candidates = []
    for cell1 in row.cell_list:
        if cell1 != cell and all(elem in cell1.possible_numbers for elem in possible_numbers):
            row_candidates.append(cell1)
    for cell2 in column.cell_list:
        if cell2 != cell and all(elem in cell2.possible_numbers for elem in possible_numbers):
            column_candidates.append(cell2)
    for cell1_pos in row_candidates:
        for cell3_pos in column_list[cell1_pos.column_number].cell_list:
            for cell2_pos in column_candidates:
                if cell3_pos.row_number == cell2_pos.row_number and all(elem in cell3_pos.possible_numbers for elem in possible_numbers):
                    if len(cell1_pos.possible_numbers) == 2 and len(cell2_pos.possible_numbers) == 2:
                        update_unique_rectangle(possible_numbers, cell3_pos)
                    elif len(cell2_pos.possible_numbers) == 2 and len(cell3_pos.possible_numbers) == 2:
                        update_unique_rectangle(possible_numbers, cell1_pos)
                    elif len(cell1_pos.possible_numbers) == 2 and len(cell3_pos.possible_numbers) == 2:
                        update_unique_rectangle(possible_numbers, cell2_pos)


def unique_rectangle(cell):
    if len(cell.possible_numbers) == 2:
        check_unique_rectangle(cell, cell.possible_numbers)


def check_possible_numbers(cell):
    if len(cell.possible_numbers) == 1:
        fill_cell(cell, cell.possible_numbers[0])
        return
    check_row(cell)
    check_column(cell)
    check_square(cell)
    hidden_singles(cell)
    naked_multiples(cell)
    omission(cell)
    hidden_multiples(cell)
    swordfish(cell)
    unique_rectangle(cell)
    if len(cell.possible_numbers) == 1:
        fill_cell(cell, cell.possible_numbers[0])
        return


def solve():
    for empty_cell in empty_cells_list:
        check_possible_numbers(empty_cell)


def update_visual_board():
    for widget in frame.winfo_children():
        widget.destroy()
    updated_board = tk.Label(frame, text=board, height=250, width=250)
    updated_board.config(font=("Courier", 20))
    updated_board.pack()



row_list = create_row_list()
column_list = create_column_list()
empty_cells_list = create_list_empty_cells(board)
square_list = fill_square_list(create_square_list(), empty_cells_list)
total_time = 0


def solve_sudoku():
    start_time = time.perf_counter()
    while len(empty_cells_list) != 0:
        solve()
    finished_time = time.perf_counter()
    total_time = finished_time - start_time
    update_visual_board()
    tk.Label(root, text="This Sudoku has been solved in %.2f seconds" %total_time).pack()


root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
empty_board = tk.Label(frame, text=board, height=250, width=250)
empty_board.config(font=("Courier", 20))
empty_board.pack()

solve_button = tk.Button(root, text="Solve the Sudoku", padx=10, pady=5, fg="white", bg="black", command=solve_sudoku)
solve_button.pack()

root.mainloop()