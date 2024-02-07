"""EX02 - One Shot Battleship."""

__author__ = "730403386"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_input: str = input("Guess a row: ")
row_number: int = int(row_input)
while row_number > grid_size:
    row_input = str(input("The grid is only 4 by 4. Try again: "))
    row_number = int(row_input)
while row_number < 1:
    row_input = str(input("The grid is only 4 by 4. Try again: "))
    row_number = int(row_input)

column_input = str(input("Guess a column: "))
column_number = int(column_input)
while column_number > grid_size:
    column_input = str(input("The grid is only 4 by 4. Try again: "))
    column_number = int(column_input)
while column_number < 1:
    column_input = str(input("The grid is only 4 by 4. Try again: "))
    column_number = int(column_input)


row_counter = 1
column_counter = 1
row_str = ""
while row_counter <= grid_size:
    column_counter = 1
    if row_number == row_counter:
        while column_counter <= grid_size:
            if column_number == column_counter:
                if row_number == 3:
                    if column_number == 2:
                        row_str += RED_BOX
                    else: 
                        row_str += WHITE_BOX
                else:
                    row_str += WHITE_BOX
            else:
                row_str += BLUE_BOX
            column_counter += 1 
    else:
        while column_counter <= grid_size:
            row_str += BLUE_BOX
            column_counter += 1
    print(row_str)
    row_str = ""
    row_counter += 1

if row_number == 3:
    if column_number == 2:
        print("Hit!")
    else:
        print("Miss!")
        print("Close! Correct row, wrong column.")
elif column_number == 2:
    print("Miss!")
    print("Close! Correct column, wrong row.")
else: 
    print("Miss!")