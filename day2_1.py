import generalMethods

cubes = {"red": 12, "green": 13, "blue": 14}
counter = 0

data = generalMethods.getInputArray(2)
games = [(int(game[game.find(" ") + 1:game.find(":")]), [n for n in game[game.find(":") + 2:].split("; ")])
         for game in data]  # game = (id[int], hands[2 D list of tuples (colour, amount)]) [tuple]

for current_game in games:
    for draw in range(len(current_game[1])):  # create the 2D tuple list from list
        current_game[1][draw] = [(colour[colour.find(" ") + 1:], int(colour[:colour.find(" ")]))
                                 for colour in current_game[1][draw].split(", ")]

    is_possible = True
    for draw in current_game[1]:
        for colour_tuple in draw:
            if colour_tuple[1] > cubes[colour_tuple[0]]:
                # test if needed cubes for each tuple are more than provided in cubes
                is_possible = False
                break

    if is_possible:
        counter += current_game[0]

print(counter)
