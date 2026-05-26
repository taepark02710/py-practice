import random

def make_card(rank, suit):
    
    shorthand = ""
    
    if rank < 10:
        shorthand = " " + str(rank) + suit[0]
    else:
        shorthand = str(rank) + suit[0]
        
    if rank == 11:
        rank = "Jack"
        
    if rank == 12:
        rank = "Queen"
    if rank == 13:
        rank = "King"
    
    if rank == 14:
        rank = "Ace"

    name = str(rank) + " of " + suit
    
    white = "\033[37m"
    red = "\033[31m"
    blue = "\033[34m"
    
    if suit == "Hearts" or suit == "Diamonds":
        shorthand = red + shorthand + white
    else:
        shorthand = blue + shorthand + white
        
    return (rank, suit, name, shorthand)

def make_deck():
    deck = []
    ranks = [i for i in range(2, 15)]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    for rank in ranks:
        for suit in suits:
            card = make_card(rank, suit)
            deck.append(card)
            
    return deck

def shuffle(deck):
    
    for i in range(0, len(deck)):
        j = random.randint(i, len(deck) - 1)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        
    return deck

def draw(deck, hand):
    
    if len(deck) <= 0:
        return None
    else:
        card = deck.pop()
        hand.append(card)
    
    return card

def deal(deck, num):
    hand1 = []
    hand2 = []
    
    for _ in range(0, num):
        draw(deck, hand1)
        draw(deck, hand2)
        
    return hand1, hand2

def cut(deck):
    first_half = deck[:len(deck) // 2]
    second_half = deck[len(deck) // 2:]
    
    return first_half, second_half


    
def main():
    # print(make_card(2, "Hearts")[3])
    # print(make_card(10, "Diamonds")[3])
    # print(make_card(14, "Spades")[3])
    
    # print(make_deck())
    # print(len(make_deck()))
    # print(shuffle(make_deck()))
    print(deal(shuffle(make_deck()), 5)[0])
    print(deal(shuffle(make_deck()), 5)[1])
    
    
    
if __name__ == "__main__":
    main()
    
    