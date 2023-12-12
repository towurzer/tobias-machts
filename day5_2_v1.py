import day5_1
import generalMethods


def create2DSeedIndexList(indexString: str) -> list:
    """takes a string input which represents a compact form of a two-dimensional list, where the first number is
    the starting number, and the second number represents the amount of following numbers in that list.
    creates the according two-dimensional lis and returns it"""
    indexList = list(map(int, indexString.split(" ")))
    tupelList = [(indexList[i], indexList[i + 1]) for i in range(0, len(indexList) - 1, 2)]
    twoDIndexList = [[seedPair[0] + i for i in range(seedPair[1])] for seedPair in tupelList]
    return twoDIndexList


def main(day) -> None:
    """Main programm code. Divides the input data in a dictionary and a list.
    The list contains a single string which is a compacted representation of a list of numbers.
     The Dictionary contains sub Dictionaries where the key is the map that the dictionary covers and the values
     are formatted as a list of tuples with following meaning: (min value, max value, reference starting point).
    After that a list of Seed Objects is created, where each object upon creation iterates through the all the sub
    dictionaries to get its final location value. After that the list of Seeds gets sorted ascending regarding their
    location values and the lowest location value gets printed to console."""

    data = [map_i.split("\n") for map_i in generalMethods.getInputString(day).split("\n\n")]
    # create a sub dictionary for each map in the main dict maps
    maps = {}
    for i in range(1, len(data)):
        dict_tuple = day5_1.createMapDictionary(data[i])
        maps[dict_tuple[0]] = dict_tuple[1]

    # create list of Seed objects (data[0]) is a list with only one big string of seeds and useless text in it
    seeds = []
    seedString = data[0][0]
    seedString = seedString[seedString.find(":") + 2:]
    for sublist in create2DSeedIndexList(seedString):
        for seed in sublist:
            seeds.append(day5_1.Seed(seed, maps))

    seeds.sort(key=lambda x: x.location)

    print(seeds[0].location)


if __name__ == '__main__':
    main(5)
