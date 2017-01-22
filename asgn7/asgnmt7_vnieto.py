from asgn7 import VideoPoker as VideoPoker
import random

suits = "C D H S"
suits = suits.split()

Rank = "2 3 4 5 6 7 8 9 T J Q K A"

Rank = Rank.split()

# generates a new random card in the case that there are two cards in a hand
# that are the same
def generate_card():
    rank = random.choice(Rank)
    suit = random.choice(suits)
    card = "{0}{1}".format(rank, suit)
    return card


def rand_hand():
    # empty list where cards will be stored
    hand = []
    # makes a random card by choosing random rank from rank list and
    # by choosing random suit in suit list. Does this 5 times and adds
    # resulting cards to end of hand list. then returns it
    for i in range(5):
        rank = random.choice(Rank)
        suit = random.choice(suits)
        card = "{0}{1}".format(rank, suit)
        hand.append(card)
    # checks list for repeat cards and generates new random card if it finds
    # a repeating card
    for i in range(5):
        for j in range(5):
            if(j != i):
                while(hand[i] == hand[j]):
                  hand[j] = generate_card()
    return hand

# in order to make new hand using held cards I made this function.
def new_hand(held, prev_hand):
    # generates list of 5 random cards
    nhand = rand_hand()

    # checks to see if the new hand generated has cards that were in the
    # previous hand. if so make sure to generate new random card to replace
    # it because new cards dealt must be out of 47 cards that weren't in the
    # previous hand
    for i in range(len(nhand)):
        while(nhand[i] in prev_hand):
            nhand[i] = generate_card()

    # places cards originally held in the same position they were
    # in the previous hand
    for e in held:
        for i in range(len(nhand)):
            # check to see if there are any duplicates, if there are make sure to generate new
            # card that is not a duplicate
            while(nhand[i] == prev_hand[e]):
                ncard = generate_card()
                nhand[i] = ncard
        nhand[e] = prev_hand[e]
    return nhand

# function to test new_hand() function
def testnewhand():
    held = [2, 3]
    prevhand = ['AS', '7C', 'AD', 'AH', '8H']
    newhand = new_hand(held, prevhand)
    print(newhand)

# testnewhand()

# returns list with cards that were held
# will use this to count ranks and count suits of the hand
def get_hand(held, prev_hand):
    chand = []
    for e in held:
        chand.append(prev_hand[e])
    return chand

# takes in hand and makes list using ranks of each card
def count_rank(held_hand):
    rank_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in held_hand:
        rank = card[0]
        if rank == 'T':
            rank_list[8] += 1
        elif rank == 'J':
            rank_list[9] += 1
        elif rank == 'Q':
            rank_list[10] += 1
        elif rank == 'K':
            rank_list[11] += 1
        elif rank == 'A':
            rank_list[12] += 1
        else:
            rank = int(rank)
            rank_list[rank-2] += 1
    return rank_list

# function to test count_rank() function
def testcountr():
    hand = ['TS', 'AD', 'TS', 'AD']
    rank_list = count_rank(hand)
    print(rank_list)

# testcountr()


def determine_payout(hand):
    ranklist = count_rank(hand)
    suitlist = count_suit(hand)
    # sublist of ranklist that only inlcudes the last four elements
    # which are the elements representing how many of each royal
    # card there is
    royal_rank = ranklist[8: ]
    # ace first order ranklist to check for straights
    temp = ranklist[12]
    acerank = ranklist[0 : 12]
    acerank.insert(0, temp)
    flush_count = 0
    payout = ""
    for e in suitlist:
        # checks for a flush in the suitlist
        if e == 5:
            payout = "Flush"
            # if you have a flush check to see if you have a straight flush
            # by checking if there are five 1s in a row in the rank list
            # this can't check for a straight consisting of (A 2 3 4 5)
            for rank in ranklist:
                if flush_count == 5:
                    payout = "Straight flush"
                    break
                if rank == 1:
                    flush_count += 1
                else:
                    flush_count = 0

            # check for straight flush consisting of rank (A 2 3 4 5)
            flush_count = 0
            for rank in acerank:
                if flush_count == 5:
                    payout = "Straight flush"
                    break
                if rank == 1:
                    flush_count += 1
                else:
                    flush_count = 0

            # check for a royal flush by checking if there are 5 1s in a row
            # at the end of rank list. From ranklist[8: ]
            for rank in royal_rank:
                if flush_count == 5:
                    payout = "Royal flush"
                    break
                if rank == 1:
                    flush_count += 1
                else:
                    flush_count = 0
    # if payout is any type of flush then return the payout
    if("lush" in payout):
        return payout
    # check if there is a straight by checking if there are 5
    # consecutive ranks in the ranklist
    straight_count = 0
    # check ranklist in current order; this can't check for a straight consisting of (A 2 3 4 5)
    for rank in ranklist:
        if straight_count == 5:
            payout = "Straight"
            return payout
        if rank == 1:
            straight_count += 1
        else:
            straight_count = 0
    # check ranklist with ace value at index 0 to check for straight (A 2 3 4 5)
    straight_count = 0
    for rank in acerank:
        if straight_count == 5:
            payout = "Straight"
            return payout
        if rank == 1:
            straight_count += 1
        else:
            straight_count = 0

    # check rank list for four of a kind
    if(ranklist.count(4) == 1):
        payout = "Four of a kind"
        return payout
    # check rank list for a Full house
    elif(ranklist.count(2) == 1 and ranklist.count(3) == 1):
        payout = "Full house"
        return payout
    # check rank list for 3 of a kind
    elif(ranklist.count(3)):
        payout = "Three of a kind"
        return payout
    # check rank list for 2 pairs of cards with same rank
    elif(ranklist.count(2) == 2):
        payout = "Two pair"
        return payout
    elif(royal_rank[1: ].count(2) == 1):
        payout = "Pair"
        return payout
    else:
        payout = "None"
        return payout


# function to test the determine_payout function
def testpayout():
    hand = ['AS', '7C', 'AD', 'AH', '8H']
    payout = determine_payout(hand)
    print(payout)



def count_suit(held_hand):
    # empty suit list where 1 will be added if suit is seen
    # [Clubs, Diamonds, Hearts, Spades]
    suit_list = [0, 0, 0, 0]
    # checks suit of each card and adds 1 to
    # specific index value if suit matches value
    for e in held_hand:
        suit = e[1]
        if suit == 'C':
            suit_list[0] += 1
        elif suit == 'D':
            suit_list[1] += 1
        elif suit == 'H':
            suit_list[2] += 1
        else:
            suit_list[3] += 1
    return suit_list

def get_credits(payout, bet):
    # dictionary with the amount of credits earned for each payout
    payoffs = {
    "Royal flush" : 250,
    "Straight flush" : 50,
    "Four of a kind" : 25,
    "Full house" : 9,
    "Flush" : 6,
    "Straight" : 4,
    "Three of a kind" : 3,
    "Two pair" : 2,
    "Pair" : 1,
    "None" : 0
    }
    if(payout == "Royal flush" and bet == 5):
        return 4000
    mult = payoffs[payout]
    # return number of credits earned for payout multiplied by the bet the user made
    return mult * bet

def testgetcredits():
    x = get_credits("Three of a kind", 5)
    print(x)

# testgetcredits()

# function to test count_suit() function
def testsuitlist():
    hand = ['6S', '7D', '8S']
    print(count_suit(hand))
# testsuitlist()
# testpayout()

def main():
    # asks user for starting number of credits. only accepts int 10-1000
    while(True):
        start_credits = int(input("How many credits do you want to start with (10 - 1000): "))
        if 10 <= start_credits <= 1000:
            break
        else:
            print("You must choose number from 10 to 1000")

    # sets number of credits equal to users input
    num_credits = start_credits
    v = VideoPoker.VideoPoker()
    credits = 0
    while(num_credits != 0):
        # display number of credits user has
        v.display_credits(num_credits)
        # grabs users bet
        bet = v.get_credits_bet()
        # subtract users bet from number of credits and display new numbr of credits
        num_credits -= bet
        v.display_credits(num_credits)
        # set the hand shown equal to random hand
        hand = rand_hand()
        v.set_cards(hand)
        # ask user to hold the cards they want
        held = v.get_held_cards()
        # if the user holds all cards, then this means the user had a win locked up
        # and you want to determine the payout right away
        if held == [0, 1, 2, 3, 4]:
            payout = determine_payout(hand)
            credits = get_credits(payout, bet)
        else:
            # if the user did not hold all cards then you want to generate cards for the
            # cards that the user did not hold and determine the payout for the new hand
            newhand = new_hand(held, hand)
            v.set_cards(newhand)
            payout = determine_payout(newhand)
            credits = get_credits(payout, bet)

        # after wait button is pushed show status message saying if you won any credits
        if(credits > 0):
            v.set_status("You got a winning hand! You won {0} credits".format(credits))
        else:
            v.set_status("You got a losing hand. No credits won")
        # set the new number of credits by adding the number of credits won
        num_credits += credits

        v.await_continue_button()
        v.set_status("")
        # if user runs out of credits than say game is over
        if(num_credits == 0):
            v.set_status("No more credits. Game Over")
main()
