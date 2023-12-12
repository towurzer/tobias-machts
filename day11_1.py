import day11_2
import generalMethods


def expand_data(data: list[str]) -> list[str]:
    """checks for empty rows and columns in data. Adds one additional row/column after an empty one and returns the
    edited data list"""
    row_index = 0
    while row_index < len(data):
        if data[row_index].count(".") == len(data[row_index]):
            data.insert(row_index, data[row_index])
            row_index += 1
        row_index += 1
    column_index = 0
    while column_index < len(data[0]):
        expand = True
        for row in data:
            if row[column_index] != ".":
                expand = False
        if expand:
            row_index = 0
            while row_index < len(data):
                data[row_index] = generalMethods.insertCharacterInstring(data[row_index], column_index, ".")
                row_index += 1
            column_index += 1
        column_index += 1
    return data


def get_coordinates(data: list[str]) -> dict:
    """searches for coordinates in data, returns a dictionary with the ids of the coordinates as keys and the
    row_coordinates and column_coordinates in a tuple"""
    coordinateDict = {}
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            if data[row_index][column_index] == "#":
                coordinateDict[len(coordinateDict.keys())] = (row_index, column_index)
    return coordinateDict


def main(day) -> None:
    """gets data, expands it and collects the coordinate Dictionary. After that it adds the distances between all
    coordinates together and returns the sum"""
    data = generalMethods.getInputArray(day)
    data = expand_data(data)
    coordinateDict = get_coordinates(data)
    # find the shortest path
    shortest_path_sum = 0
    for starting_key_index in range(len(coordinateDict.keys())):
        for finish_key_index in range(starting_key_index, len(coordinateDict.keys())):
            row_coordinates = sorted([coordinateDict[starting_key_index][0], coordinateDict[finish_key_index][0]])
            column_coordinates = sorted([coordinateDict[starting_key_index][1], coordinateDict[finish_key_index][1]])
            shortest_path_sum += (row_coordinates[1] - row_coordinates[0] +
                                  column_coordinates[1] - column_coordinates[0])
    print(shortest_path_sum)
    # print(shortest_path_sum == 10228230)


if __name__ == '__main__':
    # main(11)
    day11_2.main(11, 2)
