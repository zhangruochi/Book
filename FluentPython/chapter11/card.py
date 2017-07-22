#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import collections

Card = collections.namedtuple("Card", ["rank","suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]    



deck = FrenchDeck()
for _ in deck:
    print(_.rank,_.suit)   

from random import shuffle

try:
    print(shuffle(deck))    
except:
    print("error")

#猴子补丁
def set_card(deck,position,values):
    deck._cards[position] = values

a  = set(dir(deck))
FrenchDeck.__setitem__ = set_card    
b = set(dir(deck))
c = set(dir(FrenchDeck))

print(b - a)
print(b - c)

shuffle(deck)

for _ in deck:
    print(_.rank,_.suit)  


