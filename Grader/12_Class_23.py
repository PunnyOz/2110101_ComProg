class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    def next1(self):
        temp = ["club", "diamond", "heart", "spade"]
        temp2 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        nextnum = temp2.index(self.value)
        nextsuit = temp.index(self.suit) + 1
        if nextsuit > 3:
            nextsuit %= 4
            nextnum += 1
        if nextnum > 12:
            nextnum %= 13
        return Card(temp2[nextnum], temp[nextsuit])

    def next2(self):
        temp = ["club", "diamond", "heart", "spade"]
        temp2 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        nextnum = temp2.index(self.value)
        nextsuit = temp.index(self.suit) + 1
        if nextsuit > 3:
            nextsuit %= 4
            nextnum += 1
        if nextnum > 12:
            nextnum %= 13
        self.value = temp2[nextnum]
        self.suit = temp[nextsuit]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
