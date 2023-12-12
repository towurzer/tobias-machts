import generalMethods


def format_input_day_8(data: list) -> tuple[list[int], dict]:
    """extracts the needed information out of data and transforms / categoryses it before returning a tuple consisting
    of (instructions[list], steps[dict])"""
    # extract and transform instructions
    instructions = [{"L": 0, "R": 1}[instruction] for instruction in data[0]]

    # extract steps
    steps = {}
    for element in data[1].split("\n"):
        key = element[:element.find("=") - 1]
        go_left = element[element.find("(") + 1:element.find(",")]
        go_right = element[element.find(",") + 2:element.find(")")]
        steps[key] = (go_left, go_right)

    return instructions, steps


def main(day):
    """gets the input data, extracts instructions (first line) and extracts a dictionary which nodes lead to
    which other nodes depending on whether you are going left or going right (from 3rd line onwards).
    All set the steps to get from AAA to ZZZ are counted"""
    # get instructions list and steps dictionary
    data = generalMethods.getInputArray(day, separator="\n\n")
    formatted_input = format_input_day_8(data)
    instructions = formatted_input[0]
    steps = formatted_input[1]

    # count the steps and go from element to element by looking in the dictionary under your current spot and
    # find the next spot by looking at the first or second tuple, depending on the instructions
    counter = 0
    element = "AAA"
    while element != "ZZZ":
        element = steps[element][instructions[counter % len(instructions)]]
        counter += 1
    print(counter)
    # print(counter == 19199)


if __name__ == '__main__':
    main(8)
