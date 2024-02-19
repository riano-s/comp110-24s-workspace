"""EX03 - Functional Battleship."""

__author__ = "730403386"


def input_guess(grid_size: int, row_or_col: str) -> int:
    """Player guesses a row or column within the grid size."""
    assert row_or_col == "row" or row_or_col == "column"
    if row_or_col == "row":
        row_input: str = input("Guess a row: ")
        row_guess: int = int(row_input)
        while row_guess > grid_size:
            row_input = str(input("The grid is only " + str(grid_size) + " by " + str(grid_size) + ". Try again: "))
            row_guess = int(row_input)
        while row_guess < 1:
            row_input = str(input("The grid is only " + str(grid_size) + " by " + str(grid_size) + ". Try again: "))
            row_guess = int(row_input)
        return(row_guess)
    if row_or_col == "column":
        column_input = str(input("Guess a column: "))
        column_guess = int(column_input)
        while column_guess > grid_size:
            column_input = str(input("The grid is only " + str(grid_size) + " by " + str(grid_size) + ". Try again: "))
            column_guess = int(column_input)
        while column_guess < 1:
            column_input = str(input("The grid is only " + str(grid_size) + " by " + str(grid_size) + ". Try again: "))
            column_guess = int(column_input)
        return(column_guess)
    

def print_grid(grid_size: int,row_guess: int,column_guess: int,check: bool) -> None:
    """Guesses are being compared to secret row or column and boxes are printed."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"  
    row_counter = 1
    column_counter = 1
    row_str = ""
    while row_counter <= grid_size:
        column_counter = 1
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    if check == True:
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
    row_counter += 1
    return(row_str)


def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Returns if user's guess was correct or not."""
    if row_guess == secret_row and col_guess == secret_col:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Battleship game loop."""
