import generalMethods


def format_input(datastr: str) -> list:
    """formats the input string to a list of tupels where there first value represents the race length,
    and the second value represents the max distance measured. returns this list of tuples"""
    dataList = datastr.split("\n")
    dataList = dataList[0].split(" ") + dataList[1].split(" ")
    intList = [int(n) for n in dataList if n.isdigit()]
    dataTuples = [(intList[i], intList[i+int(len(intList)/2)]) for i in range(int(len(intList)/2))]
    return dataTuples


def getMargin(t: int, max_score: int, wait=0) -> int:
    """returns the number of times for wait element N, where the press of a button for wait out of t seconds
    would result in a distance greater than max; The distance function can be written as follows:
    s(wait) = (t-wait)*wait; Since the curve is a symmetrical quadratic function it more efficient to just look
    at the first half of a function and double the count (additionally one needs to be added if there are odd
    cases to test and the middle one also result in a new record)"""
    margin = 0
    if (t - wait)*wait > max_score:
        margin += 2
    if wait+1 < t/2:
        margin += getMargin(t, max_score, wait+1)
    elif t % 2 == 0 and t*t/4 > max_score:
        margin += 1
    return margin


def main(day):
    """main function. formats the input and gets the Margin for every race. Calculates the product and prints it to
    console"""
    data = format_input(generalMethods.getInputString(day))
    solution = 1

    for race in data:
        solution *= getMargin(race[0], race[1])

    print(solution)


if __name__ == '__main__':
    main(0)
