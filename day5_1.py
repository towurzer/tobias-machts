import generalMethods


class Seed:
    def __init__(self, seed: int, maindict: dict):
        """Initializes a new Seed object using a starting seed and a dictionary consisting of all the necessary sub-
        dictionaries to evaluate all the other aspects of the seed originating from the starting seed. To do that,
        it calls the .@extractValueFromMainDict(self, maindict, mainKey, subKey) function."""
        self.seed = seed
        self.soil = self.extractValueFromMainDict(maindict=maindict, mainKey="seed-to-soil map", subKey=self.seed)
        self.fertilizer = self.extractValueFromMainDict(maindict, "soil-to-fertilizer map", self.soil)
        self.water = self.extractValueFromMainDict(maindict, "fertilizer-to-water map", self.fertilizer)
        self.light = self.extractValueFromMainDict(maindict, "water-to-light map", self.water)
        self.temperature = self.extractValueFromMainDict(maindict, "light-to-temperature map", self.light)
        self.humidity = self.extractValueFromMainDict(maindict, "temperature-to-humidity map", self.temperature)
        self.location = self.extractValueFromMainDict(maindict, "humidity-to-location map", self.humidity)

    def printRoadMap(self) -> None:
        """for debugging purposes, prints the steps how the original seed got referenced to its location."""
        print(f"Seed: {self.seed} -> Soil: {self.soil} -> fertilizer: {self.fertilizer} -> water: {self.water} -> "
              f"light: {self.light} -> temp: {self.temperature} -> humidity{self.humidity} -> "
              f"location: {self.location}")

    @staticmethod
    def extractValueFromMainDict(maindict: dict, mainKey: str, subKey: int) -> int:
        """evaluates all the values of the object using the maindict which is transferred by the initialising process,
        the mainKey which is a fixed string for each variable and a subKey, which is an already initialised variable
        of the object.
        Everything delivered. The subkey gets compared to the keyValues of the sub dictionary and if there is a match,
        the according reference gets calculated by
        (reference starting point + difference of key and the key starting point). If there isn't a match, the new
        reference is definded to have the same value as the subkey. """
        for valueTuple in maindict[mainKey]:
            if valueTuple[0] <= subKey <= valueTuple[1]:
                return valueTuple[2] + subKey - valueTuple[0]
        return subKey


def createMapDictionary(current_map: list) -> tuple:
    """takes a list and edits it, so that it can be used as a dictionary. The first item in the list is the future key
    (with some additional ":" in it). The rest of the items are Strings of numbers, which get typecast to integers
    and rearranged to be used.
    The rearrangement goes as follows: "reference starting, index starting, count of references" -> ["rs", "is", "cr"]
    -> (index starting point, index ending point, reference starting point).
    Is that done, the method returns a tuple consisting of (key, list of tuples)"""
    current_key = current_map[0]
    current_key = current_key[:current_key.find(":")]
    current_map = [list(map(int, current_map[content].split(" "))) for content in range(1, len(current_map))]
    return current_key, [(data[1], data[1] + data[2], data[0]) for data in current_map]


def main(day) -> None:
    """Main programm code. Divides the input data in a dictionary and a list.
    The list contains all seeds that need to be evaluated. The Dictionary contains sub Dictionaries where the key
    is the map that the dictionary covers and the values are formatted as a list of tuples with following meaning:
    (min value, max value, reference starting point).
    After that a list of Seed Objects is created, where each object upon creation iterates through the all the sub
    dictionaries to get its final location value. After that the list of Seeds gets sorted ascending regarding their
    location values and the lowest location value gets printed to console."""

    data = [map_i.split("\n") for map_i in generalMethods.getInputString(day).split("\n\n")]
    # create a sub dictionary for each map in the main dict maps
    maps = {}
    for i in range(1, len(data)):
        dict_tuple = createMapDictionary(data[i])
        maps[dict_tuple[0]] = dict_tuple[1]

    # create list of Seed objects (data[0]) is a list with only one big string of seeds and useless text in it
    seedString = data[0][0]
    seedString = seedString[seedString.find(":") + 2:]
    seeds = list(map(int, seedString.split(" ")))
    seeds = [Seed(seed, maps) for seed in seeds]
    seeds.sort(key=lambda x: x.location)

    print(seeds[0].location)


if __name__ == '__main__':
    main(5)
