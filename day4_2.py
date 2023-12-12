import generalMethods


class Scratchcard:
    def __init__(self, cardID, scratchbib: dict):
        """holt sich das tuple mit der id aus dem dictionary und erstellt ein neues Objekt mit den werten"""
        self.id = scratchbib[cardID][0]
        self.winners = scratchbib[cardID][1]
        self.numbers = scratchbib[cardID][2]
        self.ticketWinners = scratchbib[cardID][3]

    def ticketsWon(self) -> list[int]:
        """returns a list with ticket IDs. These tickets are won with this ticket"""
        won = []
        additionalTicketCounter = 0
        while len(won) < len(self.ticketWinners):
            won.append(self.id+1+additionalTicketCounter)
            additionalTicketCounter += 1

        return won


def createScratchbib(day) -> dict:
    """creates the dictionary, containing each scratch-ticket with its values
    (key = id): (id, winners, numbers, ticketWinners)[tuple]"""
    scratchBib = {}
    data = [(int(scratchcard[scratchcard.find(" ") + 1:scratchcard.find(":")]),
             (scratchcard[scratchcard.find(":") + 2:scratchcard.find("|") - 1]).split(" "),
             (scratchcard[scratchcard.find("|") + 2:]).split(" "))
            for scratchcard in generalMethods.getInputArray(day)]

    for scratchcard in data:
        won = []
        for winners in scratchcard[1]:
            if winners in scratchcard[2] and winners != "":
                won.append(winners)

        scratchBib[scratchcard[0]] = (scratchcard[0], scratchcard[1], scratchcard[2], won)

    return scratchBib


def main(day) -> None:
    """Erstellt ein Dictionary mit allen möglichen Scratchcards und eine liste an tickets die du besitzt.
    Evaluiert anschließend jedes Ticket und fügt gegebenenfalls neu gewonnene Tickets zu deiner Ticketliste hinzu.
    Gibt anschließend die Menge an Tickets, die du besitzt aus"""

    scratchbib = createScratchbib(day)

    # starting Tickets
    myTickets = []
    for ticket in scratchbib.keys():
        myTickets.append(Scratchcard(ticket, scratchbib))

    # evaluates ticket wins and adds them to your ticket collection
    for currentTicket in myTickets:
        for wonTicketID in currentTicket.ticketsWon():
            myTickets.append(Scratchcard(wonTicketID, scratchbib))

    # how many tickets do you have in the end?
    print(len(myTickets))


if __name__ == '__main__':
    main(4)
