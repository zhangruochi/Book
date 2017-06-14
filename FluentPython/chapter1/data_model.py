#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import collections

Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck:
    ranks = [ str(n) for n in range(2,11) ] + list("JQKA")
    suit = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suit]

    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spades_high(card):
    rank_value  = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]




if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck)) 

    #排序
    for card in sorted(deck, key=spades_high, reverse = True):
        print(card)       





