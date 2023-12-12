import generalMethods

data = []


def move(row: int, previous_row: int, column: int, previous_column: int, step_counter=0, try_symbol=None) -> dict:
    """find symbol at position and returns dictionary with instructions on how to act (which way to go) depending
    on the symbol and the direction you are coming from. (oh and it counts the length of the path)
    If given it even replaces the pipe wit a different symbol"""
    global data
    pipe_type = data[row][column]
    if try_symbol:
        data[row] = generalMethods.replaceCharacterInString(data[row], column, try_symbol)

    if pipe_type == "S":
        return {"row": row, "previous_row": row, "column": column, "previous_column": column,
                "path_length": step_counter + 1}
    elif pipe_type == ".":
        return {"path_length": -1}  # invalid path
    elif pipe_type == "|":  # test - situation a - situation b
        if previous_column != column:
            return {"path_length": -1}  # invalid path
        elif previous_row == row - 1:
            return {"row": row + 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
        else:  # previous_row == row+1
            return {"row": row - 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
    elif pipe_type == "-":
        if previous_row != row:
            return {"path_length": -1}
        elif previous_column == column - 1:
            return {"row": row, "previous_row": row, "column": column + 1, "previous_column": column,
                    "path_length": step_counter + 1}
        else:
            return {"row": row, "previous_row": row, "column": column - 1, "previous_column": column,
                    "path_length": step_counter + 1}
    elif pipe_type == "L":
        if previous_row == row + 1 or previous_column == column - 1:
            return {"path_length": -1}
        elif previous_column == column + 1:
            return {"row": row - 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
        else:
            return {"row": row, "previous_row": row, "column": column + 1, "previous_column": column,
                    "path_length": step_counter + 1}
    elif pipe_type == "J":
        if previous_row == row + 1 or previous_column == column + 1:
            return {"path_length": -1}
        elif previous_column == column - 1:
            return {"row": row - 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
        else:
            return {"row": row, "previous_row": row, "column": column - 1, "previous_column": column,
                    "path_length": step_counter + 1}
    elif pipe_type == "7":
        if previous_row == row - 1 or previous_column == column + 1:
            return {"path_length": -1}
        elif previous_column == column - 1:
            return {"row": row + 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
        else:
            return {"row": row, "previous_row": row, "column": column - 1, "previous_column": column,
                    "path_length": step_counter + 1}
    elif pipe_type == "F":
        if previous_row == row - 1 or previous_column == column - 1:
            return {"path_length": -1}
        elif previous_column == column + 1:
            return {"row": row + 1, "previous_row": row, "column": column, "previous_column": column,
                    "path_length": step_counter + 1}
        else:
            return {"row": row, "previous_row": row, "column": column + 1, "previous_column": column,
                    "path_length": step_counter + 1}
    exit("Error, Symbol unbekannt")


def main(day) -> None:
    """get data, find starting position go every possible way. If path is invalid, try different starting direction,
    else find circle and count steps"""
    global data
    data = generalMethods.getInputArray(day)
    # TODO-1: find loop
    # TODO-1.1: find starting position
    start_row = start_column = -1
    for row_index in range(len(data)):
        if "S" in data[row_index]:
            start_row = row_index
            start_column = data[row_index].index("S")

    # TODO-1.2: Try path and count steps. (if path length == -1 invalid path, else path length found)
    answer = {"row": start_row - 1, "previous_row": start_row, "column": start_column, "previous_column": start_column,
              "path_length": 0}
    while answer["path_length"] != -1 and (
            answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
        answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                      answer["path_length"])

    if answer["path_length"] == -1:
        answer = {"row": start_row, "previous_row": start_row, "column": start_column + 1,
                  "previous_column": start_column, "path_length": 0}
        while answer["path_length"] != -1 and (
                answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
            answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                          answer["path_length"])

    if answer["path_length"] == -1:
        answer = {"row": start_row + 1, "previous_row": start_row, "column": start_column,
                  "previous_column": start_column, "path_length": 0}
        while answer["path_length"] != -1 and (
                answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
            answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                          answer["path_length"])

    # TODO-2: Evaluate length/2
    print(int(answer["path_length"] / 2))
    # print(int(answer["path_length"] / 2) == 6870)


if __name__ == '__main__':
    main(10)
