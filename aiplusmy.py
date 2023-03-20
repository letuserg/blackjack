import random

# Define card values
card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
               'K': 10}

# Define deck of cards
deck = list(card_values.keys()) * 4


# Define function to deal cards
def deal_cards(num_cards):
    return random.sample(deck, num_cards)


# Define function to calculate hand value
def hand_sum(hand):
    hand_value = sum([card_values[card] for card in hand])
    # If hand contains an Ace and the value exceeds 21, change Ace value to 1
    if 'A' in hand and hand_value > 21:
        hand_value -= 10
    return hand_value


# Define function to check if hand is a blackjack
def is_blackjack(hand):
    return len(hand) == 2 and hand_sum(hand) == 21


# Define function to play game
def play_game():
    bankroll = 100
    print("Your starting bankroll is " + str(bankroll))
    while True:
        # Placing a bet
        while True:
            bet = int(input("Place your bet: "))
            if bet > bankroll:
                print("Insufficient funds, please try again.")
                print("Your current bankroll is " + str(bankroll))
                continue
            elif bet == 0:
                print("Cannot bet zero, please try again.")
                print("Your current bankroll is " + str(bankroll))
            elif bet < 0:
                print("Cannot bet a negative amount, please try again.")
                print("Your current bankroll is " + str(bankroll))
            else:
                break

        while True:
            # Deal initial cards to player and dealer
            player_hand = deal_cards(2)
            dealer_hand = deal_cards(2)

            # Check if player or dealer has a blackjack
            if is_blackjack(player_hand) and not is_blackjack(dealer_hand):
                print(
                    f"Player's hand: {player_hand}\nPlayer has a blackjack!\nDealer's hand: {dealer_hand}\nDealer's "
                    f"score is {hand_sum(dealer_hand)}\nPlayer wins!")
                bankroll += bet * 0.5
                break
            if is_blackjack(dealer_hand) and not is_blackjack(player_hand):
                print(
                    f"Player's hand: {player_hand}\nPlayer's score is {hand_sum(player_hand)}\nDealer's "
                    f"hand: {dealer_hand}\nDealer has a blackjack!\nDealer wins!")
                bankroll -= bet
                break
            if is_blackjack(player_hand) and is_blackjack(dealer_hand):
                print(
                    f"Player's hand: {player_hand}\nPlayer has a blackjack!\nDealer's hand: {dealer_hand}\nDealer has "
                    f"a blackjack!\nPush.")
                break

            # Player's turn
            bool_double = False
            bool_split = False
            split_bust = False
            right_hand = list
            left_hand = list
            print(f'Player\'s hand: {player_hand}')
            print("Player's score is " + str(hand_sum(player_hand)))
            print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
            if bet <= bankroll / 2 and not player_hand[0][0] == player_hand[1][0]:
                while True:
                    decision = input('1 - hit, 2 - stand, 3 - double down: ')
                    if decision == '1':
                        player_hand += deal_cards(1)
                        print(f'Player\'s hand: {player_hand}')
                        print("Player's score is " + str(hand_sum(player_hand)))
                        if hand_sum(player_hand) > 21:
                            print('Player busts! Dealer wins.')
                            bankroll -= bet
                            break
                        else:
                            print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                            while True:
                                decision = input('1 - hit, 2 - stand: ')
                                if decision == '1':
                                    player_hand += deal_cards(1)
                                    print(f'Player\'s hand: {player_hand}')
                                    print("Player's score is " + str(hand_sum(player_hand)))
                                    if hand_sum(player_hand) > 21:
                                        print('Player busts! Dealer wins.')
                                        bankroll -= bet
                                        break
                                    else:
                                        print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                                elif decision == '2':
                                    print("Player's final score is " + str(hand_sum(player_hand)))
                                    break
                                else:
                                    print("Invalid input, please enter 1 or 2.")
                                    continue
                            break
                    elif decision == '2':
                        print("Player's final score is " + str(hand_sum(player_hand)))
                        break
                    elif decision == "3":
                        bool_double = True
                        player_hand += deal_cards(1)
                        print("Your final bet is " + str(bet * 2))
                        print(f'Player\'s hand: {player_hand}')
                        print("Player's final score is " + str(hand_sum(player_hand)))
                        if hand_sum(player_hand) > 21:
                            print('Player busts! Dealer wins.')
                            bankroll -= bet * 2
                        break
                    else:
                        print("Invalid input, please enter 1, 2 or 3.")
                        continue
            elif player_hand[0][0] == player_hand[1][0] and bet <= bankroll / 2:
                while True:
                    decision = input("1 - hit, 2 - stand, 3 - double down, 4 - split: ")
                    if decision == "1":
                        player_hand += deal_cards(1)
                        print(f'Player\'s hand: {player_hand}')
                        print("Player's score is " + str(hand_sum(player_hand)))
                        if hand_sum(player_hand) > 21:
                            print('Player busts! Dealer wins.')
                            bankroll -= bet
                            break
                        else:
                            print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                            while True:
                                decision = input('1 - hit, 2 - stand: ')
                                if decision == '1':
                                    player_hand += deal_cards(1)
                                    print(f'Player\'s hand: {player_hand}')
                                    print("Player's score is " + str(hand_sum(player_hand)))
                                    if hand_sum(player_hand) > 21:
                                        print('Player busts! Dealer wins.')
                                        bankroll -= bet
                                        break
                                    else:
                                        print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                                elif decision == '2':
                                    print("Player's final score is " + str(hand_sum(player_hand)))
                                    break
                                else:
                                    print("Invalid input, please enter 1 or 2.")
                                    continue
                            break
                    elif decision == "2":
                        print("Player's final score is " + str(hand_sum(player_hand)))
                        break
                    elif decision == "3":
                        bool_double = True
                        player_hand += deal_cards(1)
                        print("Your final bet is " + str(bet * 2))
                        print(f'Player\'s hand: {player_hand}')
                        print("Player's final score is " + str(hand_sum(player_hand)))
                        if hand_sum(player_hand) > 21:
                            print('Player busts! Dealer wins.')
                            bankroll -= bet * 2
                        break
                    elif decision == "4":
                        bool_split = True
                        right_hand = [player_hand[0], deal_cards(1)[0]]
                        print(f"Player's right hand: {right_hand}")
                        print("Player's right hand score is " + str(hand_sum(right_hand)))
                        if player_hand[0] != "A":
                            while True:
                                decision = input("1 - hit, 2 - stand: ")
                                if decision == "1":
                                    right_hand += deal_cards(1)
                                    print(f'Player\'s right hand: {right_hand}')
                                    print("Player's right hand score is " + str(hand_sum(right_hand)))
                                    if hand_sum(right_hand) > 21:
                                        print("Your right hand is bust!")
                                        bankroll -= bet
                                        break
                                    else:
                                        print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                                elif decision == "2":
                                    break
                                else:
                                    print("Invalid input, please enter 1 or 2")
                                    continue
                        left_hand = [player_hand[0], deal_cards(1)[0]]
                        print(f"Player's left hand: {left_hand}")
                        print("Player's left hand score is " + str(hand_sum(left_hand)))
                        if player_hand[0] != "A":
                            while True:
                                decision = input("1 - hit, 2 - stand: ")
                                if decision == "1":
                                    left_hand += deal_cards(1)
                                    print(f'Player\'s left hand: {left_hand}')
                                    print("Player's left hand score is " + str(hand_sum(left_hand)))
                                    if hand_sum(left_hand) > 21:
                                        print("Your left hand is bust!")
                                        bankroll -= bet
                                        break
                                    else:
                                        print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                                elif decision == "2":
                                    break
                                else:
                                    print("Invalid input, please enter 1 or 2")
                                    continue
                        if hand_sum(right_hand) > 21 and hand_sum(left_hand) > 21:
                            print("Both player's hands are bust!")
                            print("Dealer wins.")
                            split_bust = True
                        else:
                            print("Player's values are " + str(hand_sum(right_hand)) + " and " + str(hand_sum(left_hand)))
                        break
                    else:
                        print("Invalid input, please enter 1, 2, 3 or 4.")
                        continue
            else:
                while True:
                    decision = input('1 - hit, 2 - stand: ')
                    if decision == '1':
                        player_hand += deal_cards(1)
                        print(f'Player\'s hand: {player_hand}')
                        print("Player's score is " + str(hand_sum(player_hand)))
                        if hand_sum(player_hand) > 21:
                            print('Player busts! Dealer wins.')
                            bankroll -= bet
                            break
                        else:
                            print(f'Dealer\'s hand: [\'{dealer_hand[0]}\', \'?\']')
                    elif decision == '2':
                        print("Player's final score is " + str(hand_sum(player_hand)))
                        break
                    else:
                        print("Invalid input, please enter 1 or 2.")
                        continue

            # Dealer's turn
            if not hand_sum(player_hand) > 21 and not split_bust:
                print(f'Dealer\'s hand: {dealer_hand}')
                print("Dealer's score is " + str(hand_sum(dealer_hand)))
                while hand_sum(dealer_hand) < 17:
                    dealer_hand += deal_cards(1)
                    print(f'Dealer\'s hand: {dealer_hand}')
                    print("Dealer's score is " + str(hand_sum(dealer_hand)))
                if bool_double:
                    if hand_sum(dealer_hand) > 21:
                        print('Dealer busts! Player wins.')
                        bankroll += bet * 2
                    elif hand_sum(dealer_hand) > hand_sum(player_hand):
                        print('Dealer wins.')
                        bankroll -= bet * 2
                    elif hand_sum(dealer_hand) < hand_sum(player_hand):
                        print('Player wins.')
                        bankroll += bet * 2
                    else:
                        print('Push.')
                elif bool_split and not hand_sum(dealer_hand) > 21:
                    if hand_sum(right_hand) < hand_sum(dealer_hand) > hand_sum(left_hand):
                        bankroll -= bet * 2
                    elif hand_sum(right_hand) > hand_sum(dealer_hand) < hand_sum(left_hand):
                        bankroll += bet * 2
                    elif hand_sum(right_hand) == hand_sum(dealer_hand) > hand_sum(left_hand):
                        bankroll -= bet
                    elif hand_sum(left_hand) == hand_sum(dealer_hand) > hand_sum(right_hand):
                        bankroll -= bet
                    elif hand_sum(right_hand) == hand_sum(dealer_hand) < hand_sum(left_hand):
                        bankroll += bet
                    elif hand_sum(left_hand) == hand_sum(dealer_hand) < hand_sum(right_hand):
                        bankroll += bet
                elif bool_split and hand_sum(dealer_hand) > 21:
                    if hand_sum(right_hand) > 21 and not hand_sum(left_hand) > 21:
                        bankroll += bet
                    elif hand_sum(left_hand) > 21 and not hand_sum(right_hand) > 21:
                        bankroll += bet
                else:
                    if hand_sum(dealer_hand) > 21:
                        print('Dealer busts! Player wins.')
                        bankroll += bet
                    elif hand_sum(dealer_hand) > hand_sum(player_hand):
                        print('Dealer wins.')
                        bankroll -= bet
                    elif hand_sum(dealer_hand) < hand_sum(player_hand):
                        print('Player wins.')
                        bankroll += bet
                    else:
                        print('Push.')
            break

        # Check if the player wants to play again
        print("Your current bankroll is " + str(bankroll))
        if bankroll == 0:
            print("Out of credit, game over.\nBetter luck next time!")
            return
        while True:
            play_decision = input("Would you like to play again? (y/n): ")
            if play_decision.lower() == "y":
                break
            elif play_decision.lower() == "n":
                print("Your final bankroll is " + str(bankroll))
                if bankroll > 100:
                    print("Well played!")
                elif bankroll < 100:
                    print("Better luck next time!")
                return
            else:
                print("Invalid input, please enter 'y' or 'n'")
                continue
        continue


play_game()
