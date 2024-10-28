import random
#imports the function to randomize the deck shuffling process



# defines the created deck (suits & ranks) and shuffles it
def create_deck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck



# defines and deals cards from the deck
def deal_cards(deck):
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


# defines variable to calculate the value of cards
# applies value to ace, jack, queen and king
def card_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        if rank == 'Ace':
            ace_count += 1
            value += 11
        elif rank in ['King', 'Queen', 'Jack']:
            value += 10
        else:
            value += int(rank)
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return 

#displays the card handed
def display_hand(hand):
    for card in hand:
        print(card[0], 'of', card[1])

# defines the blackjack game
def blackjack():
    deck = create_deck()
    player_hand = deal_cards(deck)
    dealer_hand = deal_cards(deck)
    player_score = card_value(player_hand)
    dealer_score = card_value(dealer_hand)
    print('Player hand:')
    display_hand(player_hand)  #The first cards picked for the game
    print('Player score:', player_score) #starting score
    print('Dealer showing:', dealer_hand[0][0])
    while player_score < 21: 
        action = input('Do you want to (H)it or (S)tay? ') #prompts user if they want to cointue
        if action.lower() == 'h': #h continues blackjack
            card = deck.pop()
            player_hand.append(card)
            player_score = card_value(player_hand)
            print('Player drew:', card[0], 'of', card[1])
            print('Player score:', player_score)
            if player_score == 21:
                print('Blackjack! Player wins!')
                return
            elif player_score > 21:
                print(' Player loses!')
                return
        elif action.lower() == 's': #end the game
            break
    print('Dealer hand:')
    display_hand(dealer_hand)
    print('Dealer score:', dealer_score)
    while dealer_score < 17:
        card = deck.pop()
        dealer_hand.append(card)
        dealer_score = card_value(dealer_hand)
        print('Dealer drew:', card[0], 'of', card[1])
        print('Dealer score:', dealer_score)
        if dealer_score > 21:   #determine whether play wins
            print('Dealer busted! Player wins!')
            return
    if player_score > dealer_score:
        print('Player wins!')
    elif dealer_score > player_score:
        print('Dealer wins!')
    else:
      print('Tie! Dealer wins!')

#function to run the actual blackjack game
blackjack()

