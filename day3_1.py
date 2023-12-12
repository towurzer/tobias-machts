import generalMethods


def sumOfNumbersInData(data):
    """returns the sum of all digits in the data string list."""
    nSum = 0
    for row in data:
        for item in row.split("."):
            if item.isdigit():
                nSum += int(item)

            elif len(item) > 1:  # Ausnahmen: &123$; &%; 12%456
                for index in range(len(item)):
                    if not item[index].isdigit():
                        item = generalMethods.replaceCharacterInString(item, index, ".")
                item = item.split(".")  # &123$; &%; 12%456 -> ["","123",""]; ["","",""]; ["123","456"]

                for c in item:
                    if c.isdigit():
                        nSum += int(c)

    return nSum


def replaceDigit(rc, cc):
    """recursive funktion to replace numbers with "."
    if character at position is a number, go one spot to the left. else, go one spot to the right
    if that's a number replace digit with ".", if it isn't, every digit got replaced and we are finished"""
    global data
    valid_index = generalMethods.checkIndex(rc, data) and generalMethods.checkIndex(cc, data[rc])

    if valid_index and data[rc][cc].isdigit():
        replaceDigit(rc, cc - 1)
    else:
        cc += 1
        if generalMethods.checkIndex(rc, data) and generalMethods.checkIndex(cc, data[rc]):
            if data[rc][cc].isdigit():
                data[rc] = generalMethods.replaceCharacterInString(data[rc], cc, ".")
                replaceDigit(rc, cc)

    return


def markSpotsAsOk(r: int, c: int):
    """recursive funktion that manages the replacement of a 3 by 3 area with "." (center is (r,c))
    at first the center gets replaced, to make sure its marked as done, now we cycle through the area.
    If there's a digit, that's needed to be replaced, the replaceDigit function gets called to make sure, that the
    whole number gets replaced and not just the digits in the area. If we would be replacing another character,
    that would be the source of a replacement, the function calls itself to first replace the area of this character,
    so that it can be overwritten safely."""
    global data
    data[r] = generalMethods.replaceCharacterInString(string=data[r], index=c, replacement=".")



    for r2 in range(r - 1, r + 2):
        for c2 in range(c - 1, c + 2):
            valid_index = generalMethods.checkIndex(r2, data) and generalMethods.checkIndex(c2, data[r2])

            if valid_index:
                if data[r2][c2].isdigit():
                    replaceDigit(r2, c2)  # replace whole number

                if data[r2][c2] != ".":
                    markSpotsAsOk(r2, c2)
    return


"""Main Part of the program"""
data = generalMethods.getInputArray(3)
startSum = sumOfNumbersInData(data)

# Cycle through list and replace every number, that touches a symbol (if symbol touch -> replace number)
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] != "." and not data[r][c].isdigit():
            markSpotsAsOk(r, c)

endSum = sumOfNumbersInData(data)
print(startSum - endSum)
