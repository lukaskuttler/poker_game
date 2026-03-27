
from deck import Deck
class PokerHand:
    """"
    class representing a pokeck hand
    we will wornk yo rank the hand and determn trips full house, 4 of a kid,etc
    """
    def __init__(self):
        deck= Deck()
        deck.shuffle()
        _cards= []
        for i in range(5):
             _cards.append(deck.deal())
        self._cards = _cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        first_card_suit= self._cards[0].suit
        for i in range(1, 5):
            if first_card_suit != self._cards[i].suit:
                return False
        return True
    @property
    def matches(self):
        # need to compare each card against all the others and count matches
        matches = 0
        for card1 in self._cards:
            for card2 in self._cards:
                if card1 == card2:
                    continue
                if card1.rank == card2.rank:
                    matches += 1
        return matches

    @property
    def is_fullhouse(self):
        return self.matches == 8

    @property
    def is_4kind(self):
        return self.matches == 12

    @property
    def is_straight(self):
        if self.matches != 0:
            return False
        self._cards.sort()
        ranks = self._cards[0].RANKS
        if ranks.index(self._cards[0].rank) + 4 == ranks.index(self._cards[4].rank):
            return True
        return False

iterations = 0
hits = 0
while True:
    hand = PokerHand()
    iterations += 1
    if hand.is_straight:
        # print(hand)
        # print("Done it in ", iterations)
        hits += 1
    if hits == 1000:
        prob = hits / iterations * 100
        print(f"probability of a straight is {prob}%")
        break
