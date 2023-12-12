import generalMethods
import math


class Hand:
    score_of_card = {"A": 13,
                     "K": 12,
                     "Q": 11,
                     "J": 1,
                     "T": 10,
                     "9": 9,
                     "8": 8,
                     "7": 7,
                     "6": 6,
                     "5": 5,
                     "4": 4,
                     "3": 3,
                     "2": 2}
    score_of_type = {"FiveOAKind": 70700_000_000,
                     "FourOAKind": 60600_000_000,
                     "FullHouse": 50500_000_000,
                     "ThreeOAKind": 40400_000_000,
                     "TwoPair": 30300_000_000,
                     "OnePair": 20200_000_000,
                     "HighCard": 10100_000_000
                     }

    def __init__(self, cards: str, bet: int):
        self.cards: list = [card for card in cards[:5]]
        self.bet = bet
        self.card_scores: list = self.returnScore(sort=False)
        self.hand_type: str = self.return_hand_type()
        self.final_score: int = self.evaluateFinalScore()

    def returnScore(self, sort: bool) -> list:
        score = [Hand.score_of_card[card] for card in self.cards]
        if sort:
            score.sort(reverse=True)
        return score

    def evaluateFinalScore(self) -> int:
        final_score = 0
        for i in range(len(self.card_scores)):
            final_score += self.card_scores[i] * math.pow(100, 4 - i)
        final_score += Hand.score_of_type[self.hand_type]
        return final_score

    def return_hand_type(self):
        sorted_cards = self.returnScore(sort=True)
        j_counter = sorted_cards.count(Hand.score_of_card["J"])
        a = sorted_cards[0]
        b = sorted_cards[1]
        c = sorted_cards[2]
        d = sorted_cards[3]
        e = sorted_cards[4]

        if sorted_cards.count(a) + j_counter >= 5:
            return "FiveOAKind"
        elif sorted_cards.count(a) + j_counter == 4 or sorted_cards.count(b) + j_counter == 4:
            return "FourOAKind"
        elif ((a == b and d == e) and (b == c or c == d)) or (a == b and c == d and j_counter == 1):
            return "FullHouse"
        elif (sorted_cards.count(a) + j_counter == 3 or sorted_cards.count(b) + j_counter == 3
              or sorted_cards.count(c) + j_counter == 3):
            return "ThreeOAKind"
        elif (a == b and c == d) or (a == b and d == e) or (b == c and d == e):
            return "TwoPair"
        elif (sorted_cards.count(a) + j_counter == 2 or sorted_cards.count(b) + j_counter == 2
              or sorted_cards.count(c) + j_counter == 2 or sorted_cards.count(d) + j_counter == 2):
            return "OnePair"
        return "HighCard"


def main(day):
    data = [hand.split(" ") for hand in generalMethods.getInputArray(day)]
    data = [Hand(hand[0], int(hand[1])) for hand in data]
    data.sort(key=lambda hand: hand.final_score)

    total_winnings = 0
    for i in range(len(data)):
        total_winnings += (i + 1) * data[i].bet
    print(total_winnings)
    # day7_1.debug(data, total_winnings)


if __name__ == '__main__':
    main(7)
