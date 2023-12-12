import time

import day11_1
import generalMethods


def expand_data(data: list[str]) -> tuple[list[int], list[int]]:
    """checks for empty rows and columns in data. Collects the indices of these rows and columns, adds them to list
    and returns both of these lists in a tuple, where the expanded rows list sits before the expanded columns list"""
    expanded_rows = []
    expanded_columns = []
    for row_index in range(len(data)):
        if data[row_index].count(".") == len(data[row_index]):
            expanded_rows.append(row_index)

    for column_index in range(len(data[0])):
        expand = True
        for row in data:
            if row[column_index] != ".":
                expand = False
                break

        if expand:
            expanded_columns.append(column_index)

    return expanded_rows, expanded_columns


def main(day, expansion_factor: int) -> None:
    """gets data and finds the expanded rows/columns and collects the coordinate Dictionary. After that it adds
    the distances between all coordinates together and returns the sum. Whilst adding the distances together it
    checks whether a row/column got expanded and if that's the case the distance for this row and column is not
    1 but 1 000 000 instead"""
    data = generalMethods.getInputArray(day)
    coordinateDict = day11_1.get_coordinates(data)

    expanded_rows_and_columns = expand_data(data)
    expanded_rows = expanded_rows_and_columns[0]
    expanded_columns = expanded_rows_and_columns[1]

    # find the shortest path
    shortest_path_sum = 0
    for starting_key_index in range(len(coordinateDict.keys())):
        for finish_key_index in range(starting_key_index, len(coordinateDict.keys())):
            row_coordinates = sorted([coordinateDict[starting_key_index][0], coordinateDict[finish_key_index][0]])
            column_coordinates = sorted([coordinateDict[starting_key_index][1], coordinateDict[finish_key_index][1]])
            shortest_path_sum += (row_coordinates[1] - row_coordinates[0] +
                                  column_coordinates[1] - column_coordinates[0])
            for expanded_row in expanded_rows:
                if row_coordinates[0] < expanded_row < row_coordinates[1]:
                    shortest_path_sum += expansion_factor - 1  # -1 because its counted once in the previous addition
            for expanded_column in expanded_columns:
                if column_coordinates[0] < expanded_column < column_coordinates[1]:
                    shortest_path_sum += expansion_factor - 1  # -1 because its counted once in the previous addition

    print(shortest_path_sum)
    # print(shortest_path_sum in [447073334102, 10228230, 374, 1030, 8410])


if __name__ == '__main__':
    main(day=11, expansion_factor=1_000_000)
