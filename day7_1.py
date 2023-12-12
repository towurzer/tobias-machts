import math
import generalMethods


class Hand:
    score_of_card = {"A": 13,
                     "K": 12,
                     "Q": 11,
                     "J": 10,
                     "T": 9,
                     "9": 8,
                     "8": 7,
                     "7": 6,
                     "6": 5,
                     "5": 4,
                     "4": 3,
                     "3": 2,
                     "2": 1}
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
        a = sorted_cards[0]
        b = sorted_cards[1]
        c = sorted_cards[2]
        d = sorted_cards[3]
        e = sorted_cards[4]
        if a == b == c == d == e:
            return "FiveOAKind"
        elif a == b == c == d or b == c == d == e:
            return "FourOAKind"
        elif (a == b and d == e) and (b == c or c == d):
            return "FullHouse"
        elif (a == b == c) or (b == c == d) or (c == d == e):
            return "ThreeOAKind"
        elif (a == b and c == d) or (a == b and d == e) or (b == c and d == e):
            return "TwoPair"
        elif a == b or b == c or c == d or d == e:
            return "OnePair"
        return "HighCard"


def debug(data, total_winnings) -> None:
    for i in range(len(data)):
        hand = data[i]
        print(f"{hand.final_score}: {hand.hand_type} ({hand.card_scores})")
        if data[(i + 1) % len(data)].card_scores[0] != hand.card_scores[0] and __name__ == '__main__':
            print("")

    print(total_winnings, total_winnings == 253205868 or total_winnings == 6440 or
          total_winnings == 253907829 or total_winnings == 5905)


def main(day):
    data = [hand.split(" ") for hand in generalMethods.getInputArray(day)]
    data = [Hand(hand[0], int(hand[1])) for hand in data]
    data.sort(key=lambda hand: hand.final_score)

    total_winnings = 0
    for i in range(len(data)):
        total_winnings += (i + 1) * data[i].bet
    print(total_winnings)
    # debug(data, total_winnings)


if __name__ == '__main__':
    main(7)
