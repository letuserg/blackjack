import random

# Define card values
card_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Define deck of cards
deck = list(card_values.keys()) * 4

# Define function to deal cards
def deal_cards(num_cards):
    return random.sample(deck, num_cards)

# Define function to calculate hand value
def calculate_hand_value(hand):
    hand_value = sum([card_values[card] for card in hand])
    # If hand contains an Ace and the value exceeds 21, change Ace value to 1
    if 'Ace' in hand and hand_value > 21:
        hand_value -= 10
    return hand_value

# Define function to check if hand is a blackjack
def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

# Define function to play game
def play_game():
    # Deal initial cards to player and dealer
    player_hand = deal_cards(2)
    dealer_hand = deal_cards(2)

    # Check if player or dealer has a blackjack
    if is_blackjack(player_hand):
        print('Player has a blackjack! Player wins.')
        return
    if is_blackjack(dealer_hand):
        print('Dealer has a blackjack! Dealer wins.')
        return

    # Player's turn
    while True:
        print(f'Player\'s hand: {player_hand}')
        print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
        decision = input('Do you want to hit or stand? ')
        if decision.lower() == 'hit':
            player_hand += deal_cards(1)
            if calculate_hand_value(player_hand) > 21:
                print('Player busts! Dealer wins.')
                return
        else:
            break

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand += deal_cards(1)
    print(f'Player\'s hand: {player_hand}')
    print(f'Dealer\'s hand: {dealer_hand}')
    if calculate_hand_value(dealer_hand) > 21:
        print('Dealer busts! Player wins.')
    elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
        print('Dealer wins.')
    elif calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
        print('Player wins.')
    else:
        print('It\'s a tie!')

# Start game
play_game()
