import random
from asgn7 import VideoPoker as VideoPoker

# suits = "C D H S"
# suits = suits.split()
#
# Rank = "2 3 4 5 6 7 8 9 T J Q K A"
#
# Rank = Rank.split()
#
# def rand_hand():
#     hand = []
#     for i in range(5):
#         rank = random.choice(Rank)
#         suit = random.choice(suits)
#         card = "{0}{1}".format(rank, suit)
#         hand.append(card)
#     return hand
#
# hand = rand_hand()
#
# x = Rank[0: 12]
# x.insert(0, 'A')
#
# print(x)
v = VideoPoker.VideoPoker()
x = v.VP_payoff_information["Three of a kind"]
print(x)
