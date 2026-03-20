class PlayingCard:
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self, suit, rank):
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




