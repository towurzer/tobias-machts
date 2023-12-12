def getInputString(day):
    """returns the input for the day, which needs to be saved in "inputs/dayX" where X is the current day (0=test)"""
    inputFile = open(f"inputs/day{day}")
    return inputFile.read()


def getInputArray(day, separator="\n"):
    """calls the "getInputString(day)" function and returns the input for the day
    formatted as an array, where each item was separated by the separator"""
    return getInputString(day).split(separator)


def returnValidIndex(index: int, list):
    """checks if the given index is a valid index for the list and returns either the given index or the
    nearest possible index (0 / -1)"""
    if index < 0:
        return 0
    elif index > len(list):
        return len(list) - 1
    else:
        return index


def checkIndex(index: int, list):
    """check if given index is a valid index for the given list and returns the according boolean value"""
    if index < 0 or index > len(list) - 1: return False
    return True


def replaceCharacterInString(string: str, index: int, replacement: str):
    """replaces the character at position index from string with replacement.
    string = string[:index] + replacement + string[index + 1:]
        (since strings are immutable string[index] = replacement doesn't work)"""
    return string[:index] + replacement + string[index + 1:]


def insertCharacterInstring(string: str, index: int, char: str):
    return string[:index]+char+string[index:]


def is_prime(num: int) -> bool:
    """calculates whether num is prime or not"""
    if num < 2:
        return False
    for i in range(2, num):
        if i % num == 0:
            return False
    return True


def write_list_to_txt(solution_list, day=None, file_path=None):
    """creates a file (if nothing else specified in the output folder) with the contents of a list seperated by \\\\n"""
    if not file_path:
        file_path = f"outputs/day{day}-solution"

    with open(file_path, 'w') as file:
        for item_index in range(len(solution_list)):
            file.write(str(solution_list[item_index]))
            if item_index < len(solution_list)-1:
                file.write("\n")

