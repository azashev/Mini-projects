from collections import deque


def main():
    def column_validator(column_to_validate):
        if column_to_validate.lower() in ["restart", "reset", "new"]:
            main()
        valid_cols = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
        }
        if column_to_validate in valid_cols:
            current_column = valid_cols[column_to_validate]
            return current_column
        try:
            current_column = eval(column_to_validate)
        except NameError:
            return False
        except SyntaxError:
            return False

        current_column = int(current_column)
        if 0 <= current_column - 1 < cols:
            return current_column
        return False

    def coordinates_validator(row_to_validate, col_to_validate, play_symbol_to_validate):
        if not 0 <= row_to_validate < rows or not 0 <= col_to_validate < cols or \
                not board[row_to_validate][col_to_validate] == play_symbol_to_validate:
            return False
        return True

    def check_for_win(current_r, current_c, current_coordinates, iterations):
        current_r, current_c = current_r + current_coordinates[0], current_c + current_coordinates[1]

        if not coordinates_validator(current_r, current_c, player_symbol):
            return

        if iterations == 3:
            [print(f"[ {', '.join(str(x) for x in row)} ]") for row in board]
            print(f"\nGame over!\nThe winner is Player {player_number}!")
            raise SystemExit

        check_for_win(current_r, current_c, current_coordinates, iterations + 1)

    directions = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, -1),
        (1, 1),
        (-1, -1),
        (-1, 1),
    )

    player_one_symbol = "1"
    player_two_symbol = "2"

    rows, cols = 6, 7
    moves = 0

    board = [["0"] * cols for _ in range(rows)]
    turn = deque([[1, player_one_symbol], [2, player_two_symbol]])

    print("Welcome to Connect Four!")

    while True:
        [print(f"[ {', '.join(str(x) for x in row)} ]") for row in board]
        player_number, player_symbol = turn[0]
        player_column = input(f"\nPlayer {player_number}, "
                              f"please choose a column (1 to 7; or type restart/reset/new to restart the game): \n")
        validated_column = column_validator(player_column)
        if not validated_column:
            print(f"{player_column} is not a valid column. Please select a valid column "
                  f"(1 to 7; or type restart/reset/new to restart the game)")
            continue
        column = int(validated_column) - 1

        row = 0
        if not board[row][column] == "0":
            print(f"Column {validated_column} does not have any valid slots. Please select a different column")
            continue

        while True:
            if row == rows - 1 or not board[row + 1][column] == "0":
                board[row][column] = player_symbol
                moves += 1
                break
            row += 1

        if moves >= 7:
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == player_symbol:
                        r = row
                        c = col
                        for coordinates in directions:
                            check_for_win(r, c, coordinates, 1)

        turn.append(turn.popleft())


main()
