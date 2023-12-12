import generalMethods
import math

power_sum = 0

data = generalMethods.getInputArray(2)
games = [(int(game[game.find(" ") + 1:game.find(":")]), [n for n in game[game.find(":") + 2:].split("; ")])
         for game in data]  # game = (id[int], hands[2 D list of tuples (colour, amount)]) [tuple]

for current_game in games:
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for draw in range(len(current_game[1])):  # create the 2D tuple list from list
        current_game[1][draw] = [(colour[colour.find(" ") + 1:], int(colour[:colour.find(" ")]))
                                 for colour in current_game[1][draw].split(", ")]

    for draw in current_game[1]:
        for colour_tuple in draw:
            if colour_tuple[1] > min_cubes[colour_tuple[0]]:
                min_cubes[colour_tuple[0]] = colour_tuple[1]

    power_sum += math.prod(min_cubes.values())


print(power_sum)
