import math

import generalMethods


def main(day) -> None:
    """holt sich den Datensatz und erstellt pro ticket ein tupel, bestehend aus [id, winners, yourNumbers]
     anschließend wird durch jedes tupel durchiteriert, ermittelt welche werte gewonnen haben und ein score berechnet.
      ist dies geschehen wird der tupel ersetzt durch einen neuen tupel bestehend aus
      [id, winners, yourNumbers, yourWinners, points] und zusätzlich werden die Punkte zu den gesamtpunkten gezählt,
      welche anschließend ausgegeben werden."""
    data = [(int(scratchcard[scratchcard.find(" ") + 1:scratchcard.find(":")]),  # id
             (scratchcard[scratchcard.find(":") + 2:scratchcard.find("|") - 1]).split(" "),  # winners
             (scratchcard[scratchcard.find("|") + 2:]).split(" "))  # your numbers
            for scratchcard in generalMethods.getInputArray(day)]

    pointSum = i = 0
    for scratchcard in data:
        won = []

        for winners in scratchcard[1]:
            if winners in scratchcard[2] and winners != "":
                won.append(winners)

        data[i] = (scratchcard[0], scratchcard[1], scratchcard[2],  # won [list], winners [list], yourNumber [list]
                   won, int(math.pow(2, len(won) - 1)))  # your winners [list], points [int]
        pointSum += data[i][-1]
        i += 1

    print(pointSum)


if __name__ == '__main__':
    main(4)
