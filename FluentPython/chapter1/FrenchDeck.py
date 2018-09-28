import collections
Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.__cards = [Card(rank,suit) for suit in FrenchDeck.suits for rank in FrenchDeck.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self,index):
        return self.__cards[index]


if __name__ == '__main__':
    deck = FrenchDeck()    
    # 可以使用 len() 函数查看一共多少张纸牌
    print(len(deck))
    
    # 可以使用索引和切片
    print(deck[-1])
    print(deck[1:3])
    
    # 可以随机抽取纸牌
    from random import choice
    print(choice(deck))

    # 支持迭代
    for card in deck:
        print(card)


