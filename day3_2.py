import math
import generalMethods


def getBoundarysOfInt(r_index, c_index, getStart, datacopy):
    """a method that takes coordinates of an integer and returns the starting or ending index of that integer.
     As an input it takes two coordinate integers, a bool value to differenciate
      between the process of finding the beginning or ending (index) of that integer,
      and it also takes a two-dimensional array, where the integers are located in."""
    if getStart:
        step = -1
    else:
        step = +1

    valid_index = generalMethods.checkIndex(r_index, datacopy) and generalMethods.checkIndex(c_index, datacopy[r_index])
    if valid_index and datacopy[r_index][c_index].isdigit():  # if char is number continue, if not we found the end
        boundary_index = getBoundarysOfInt(r_index, c_index + step, getStart, datacopy)
    else:
        return c_index-step

    return boundary_index


def replaceDigit(rc, cc, datacopy):
    """function that takes the coordinates of an integer and recursively deletes the whole number integer by integer.
    to find and edit the number a 2D list is also needed, which gets edited and returned for further actions"""

    valid_index = generalMethods.checkIndex(rc, datacopy) and generalMethods.checkIndex(cc, datacopy[rc])
    if valid_index and datacopy[rc][cc].isdigit():  # char is integer go left
        replaceDigit(rc, cc - 1, datacopy)
    else:  # if not, the start was found and now the number can get erased.
        cc += 1
        if generalMethods.checkIndex(rc, datacopy) and generalMethods.checkIndex(cc, datacopy[rc]):
            if datacopy[rc][cc].isdigit():
                datacopy[rc] = generalMethods.replaceCharacterInString(datacopy[rc], cc, ".")
                replaceDigit(rc, cc, datacopy)

    return datacopy


def returnGearratio(r_index, c_index, datacopy):
    """takes two indices and a 2D array as input figures out which numbers a touching the given coordinates and returns
    the product of the numbers if there are exactly 2 Numbers touching, otherwise it returns 0"""
    numbers_touching = []

    for r2 in range(r_index - 1, r_index + 2):
        for c2 in range(c_index - 1, c_index + 2):
            valid_index = generalMethods.checkIndex(r2, datacopy) and generalMethods.checkIndex(c2, datacopy[r2])

            if valid_index:
                if datacopy[r2][c2].isdigit():  # at this position there is a digit, so the number
                    # ... of which the digit is a part of, gets evaluated and saved
                    numbers_touching.append(int(datacopy[r2][getBoundarysOfInt(r2, c2, True, datacopy):
                                                             getBoundarysOfInt(r2, c2, False, datacopy)+1]))
                    # after that the number gets replaced, in order to make sure it isn't counted 2 times
                    datacopy = replaceDigit(r2, c2, datacopy)

    if len(numbers_touching) == 2:
        return math.prod(numbers_touching)
    else:
        return 0


"""Main Part of the program"""
data = generalMethods.getInputArray(3)
gearRatioSum = 0

# Cycle through list and if current char is "*" figure out how many numbers are reaching into the 3x3 area around it
# if there are exactly two, add the product of these 2 numbers to the gearRatio Sum
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == "*":
            gearRatioSum += returnGearratio(r, c, data.copy())

print(gearRatioSum)
