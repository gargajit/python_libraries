import random

cards = ["ace", "king", "queen", "jack", "nine", "eight"]
variety = ["spades", "hearts", "diamond", "club"]
for i in range(random.randint(1, 5)):
    random.shuffle(variety)
    random.shuffle(cards)
    print(f"{cards[0]} of", end=" ")
    print(f"{variety[0]}")
