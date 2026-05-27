import cards
import activities   


def hand_score(hand):
    
    score = 0
    
    for card in hand:
        rank = card[0]
        try:
            if int(rank):
                score += int(rank)
        except ValueError:
            if rank == "Jack":
                score += 11
            elif rank == "Queen":
                score += 12
            elif rank == "King":
                score += 13
            elif rank == "Ace":
                if score + 11 > 21:
                    score += 1
                else:
                    score += 11
            
    return score

def print_hand_and_score(name, hand):
    
    print(name + ":")
    
    sort_cards(hand)
    
    s = ""
    
    for card in hand:
        s += card[3] + " "
        
    score = hand_score(hand)
    
    print(s + "-" + " score:", score)
    
    if score > 21:
        print("(busted)")

    
def sort_cards(hand):
    hand.sort(key=suit_key)
    
def suit_key(card):
    if card[0] == "Jack":
        return 11
    elif card[0] == "Queen":
        return 12
    elif card[0] == "King":
        return 13
    elif card[0] == "Ace":
        return 1
    else:
        return int(card[0])
    
def win_lose_or_draw(player_score, dealer_score):
    
    if player_score > 21 and dealer_score > 21:
        print("The game is draw!")
    elif player_score > 21:
        print("Dealer wins!")
    elif dealer_score > 21:
        print("Player wins!")
    elif player_score == dealer_score:
        print("The game is draw")
    else:
        if player_score > dealer_score:
            print("Player wins!")
        else:
            print("Dealer wins!")
            
def dealer_hit_or_stand(player_hand, dealer_hand):
    
    hit = False
    
    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    
    if player_score > dealer_score or dealer_score < 17:
        print("Dealer hits...")
        hit = True
    
    return hit

def player_hit_or_stand(player_hand, dealer_hand):
    
    proper = True
    is_hit = False
    
    while proper:
        try:
            hit = input("Enter “H” (or “h”) to hit or “S” (or “s”) to stand: ")
            if hit == "H" or hit == "h":
                print("Player hits...")
                is_hit = True
                proper = False
            else:
                proper = False
        except:
            print("Please type again...")
            continue
    
    return is_hit


    

def main():
    dealer = "Dealer"
    player = input("Enter your name: ")
    
    deck = cards.make_deck()
    cards.shuffle(deck)
    
    half1, half2 = cards.cut(deck)
    
    player_hand, dealer_hand = cards.deal(half2, 2)
    
    print_hand_and_score(player, player_hand)
    print_hand_and_score(dealer, dealer_hand)
    
    player_hit = player_hit_or_stand(player_hand, dealer_hand)
    
    if player_hit:
        card = cards.draw(half2, player_hand)
        print_hand_and_score(player, player_hand)
    
    dealer_hit = dealer_hit_or_stand(player_hand, dealer_hand)
    
    if dealer_hit:
        card = cards.draw(half2, dealer_hand)
        print_hand_and_score(dealer, dealer_hand)
    
    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    
    win_lose_or_draw(player_score, dealer_score)
    
    
    
    
if __name__ == "__main__":
    main()

            
            