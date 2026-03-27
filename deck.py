
import random

class PlayingCard:
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS= ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError("ivalid suit")
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        self._suit= suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __lt__(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

    def __str__(self):
        return f"{self._rank}{self._suit}"
    def __repr__(self):
        return self.__str__()

class Deck :
    """"
    Deck of cards, 52 of playing cards
    """
    def __init__(self):
        self._cards= []
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                card= PlayingCard(suit, rank)
                self._cards.append(card)

    def __str__(self):
        return str(self._cards)
    def shuffle(self):
        #mix cards in the deck
        random.shuffle(self._cards)

    def deal(self):
        #take out hr first card from the deck
        return self._cards.pop(0)
if __name__== "__main__":
    card= PlayingCard("♠", "2")
    print(card)
    deck=Deck()
    print(deck)
    print(deck)
    print(deck.deal())
