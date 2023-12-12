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


def try_path_count_step_manager(start_row: int, start_column: int) -> int:
    """figures out which direction is correct and overrides the correct path with "P"-s In theory it would return the
    path length which is irrelevant for 10.2"""
    answer = {"row": start_row - 1, "previous_row": start_row, "column": start_column, "previous_column": start_column,
              "path_length": 0}
    while answer["path_length"] != -1 and (
            answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
        answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                      answer["path_length"])

    if answer["path_length"] != -1:
        answer["row"] -= 1
        answer["path_length"] = 0
        while answer["path_length"] != -1 and (
                answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
            answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                          answer["path_length"], "P")

    if answer["path_length"] == -1:
        answer = {"row": start_row, "previous_row": start_row, "column": start_column + 1,
                  "previous_column": start_column, "path_length": 0}
        while answer["path_length"] != -1 and (
                answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
            answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                          answer["path_length"])

        if answer["path_length"] != -1:
            answer["column"] += 1
            answer["path_length"] = 0
            while answer["path_length"] != -1 and (
                    answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
                answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                              answer["path_length"], "P")

    if answer["path_length"] == -1:
        answer = {"row": start_row + 1, "previous_row": start_row, "column": start_column,
                  "previous_column": start_column, "path_length": 0}
        while answer["path_length"] != -1 and (
                answer["row"] != answer["previous_row"] or answer["column"] != answer["previous_column"]):
            answer = move(answer["row"], answer["previous_row"], answer["column"], answer["previous_column"],
                          answer["path_length"], "P")

    return answer["path_length"]


def first_enclosure_evaluation() -> None:
    """finds out if neigbour is 0 and sets the value to 0 otherwise it might be enclosed and set t0 ?"""
    global data
    if data[0][0] == "P":
        exit("Error top left is part of cycle")

    data[0] = generalMethods.replaceCharacterInString(data[0], 0, "0")
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            if (data[row_index][column_index] != "P" and data[row_index][column_index] != "1"
                    and not (row_index == column_index == 0)):
                if (generalMethods.checkIndex(row_index - 1, data) and generalMethods.checkIndex(column_index -1, data[row_index]) and data[row_index - 1][column_index - 1] == "0") or (
                    generalMethods.checkIndex(row_index - 1, data) and data[row_index - 1][column_index] == "0") or (
                    generalMethods.checkIndex(row_index - 1, data) and generalMethods.checkIndex(column_index + 1, data[row_index]) and data[row_index - 1][column_index + 1] == "0") or (
                    generalMethods.checkIndex(column_index - 1, data[row_index]) and data[row_index][column_index - 1] == "0") or (
                    generalMethods.checkIndex(column_index + 1, data[row_index]) and data[row_index][column_index + 1] == "0") or (
                    generalMethods.checkIndex(row_index + 1, data) and generalMethods.checkIndex(column_index - 1,data[row_index]) and data[row_index + 1][column_index - 1] == "0") or (
                    generalMethods.checkIndex(row_index + 1, data) and data[row_index + 1][column_index] == "0") or (
                    generalMethods.checkIndex(row_index + 1, data) and generalMethods.checkIndex(column_index + 1, data[row_index]) and data[row_index + 1][column_index + 1] == "0"):
                        data[row_index] = generalMethods.replaceCharacterInString(data[row_index], column_index, "0")
                else:
                    data[row_index] = generalMethods.replaceCharacterInString(data[row_index], column_index, "?")


def reintroduce_loop(data_without_loop: list[str], data_with_loop: list[str]) -> list[str]:
    """refills the P values with the loop parts to count wether or not a ? is enclosed"""
    for row_index in range(len(data_without_loop)):
        for column_index in range(len(data_without_loop[row_index])):
            if data_without_loop[row_index][column_index] == "P":
                data_without_loop[row_index] = generalMethods.replaceCharacterInString(data_without_loop[row_index],
                                                                column_index, data_with_loop[row_index][column_index])
    return data_without_loop


def find_out_if_in_loop() -> None:
    """Figures out if ? is in our outside the loop by using Jordans Curve Theorem (edits the global variable data.
    if ? is enclosed ? -> X; else ? -> 0)"""
    global data
    came_from_top = True
    in_loop = False
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            current_char = data[row_index][column_index]
            if current_char == "?":
                if in_loop:
                    data[row_index] = generalMethods.replaceCharacterInString(data[row_index], column_index, "X")
                else:
                    data[row_index] = generalMethods.replaceCharacterInString(data[row_index], column_index, "0")
            elif current_char == "|" or current_char == "S":  # Hardcoded !
                in_loop = not in_loop
            elif current_char == "L":
                came_from_top = True
            elif current_char == "F":
                came_from_top = False
            elif current_char == "7" and came_from_top or current_char == "J" and not came_from_top:
                in_loop = not in_loop







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
    try_path_count_step_manager(start_row, start_column)

    # TODO-2: Fill with 0 and ?, (0=not enclosed, ? maybe enclosed)
    while True:
        before = data.copy()
        first_enclosure_evaluation()
        if before == data:
            break

    # TODO 3: reintroduce_loop
    data = reintroduce_loop(data, generalMethods.getInputArray(day))

    # TODO 4: go thru each row and count if in loop
    find_out_if_in_loop()

    # TODO 5: count enclosed spots
    enclosure_counter = 0
    for row in data:
        enclosure_counter += row.count("X")

    print(enclosure_counter)
    # print(enclosure_counter == 287)


if __name__ == '__main__':
    main(10)
    generalMethods.write_list_to_txt(data, 10)
