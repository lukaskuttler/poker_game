import random
class PlayingCard:
    SUITS = ["♠", "♡", "♦", "♤", "♣"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.suit} {self.rank}"
    def __repr__(self):
        return self.__str__()

    class Deck:
        """
        Deck of cards, 52 of PlayingCard
        """
        def __init__(self):
            self._cards = []
            for suit in PlayingCard.SUITS:
                for rank in PlayingCard.RANKS:
                    card = PlayingCard(suit, rank)
                    self._cards.append(card)

        def __str__(self):
            return self._cards
        def shuffle(self):
            random.shuffle(self._cards)

card = PlayingCard("♠", "2")
card2 = PlayingCard("♣", "A")
print(card)
print(card2)