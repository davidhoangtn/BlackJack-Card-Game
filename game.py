import sys
from player import Player
from deck import Deck
from dealer import Dealer

class AbstractGame:
    def play(self):
        raise NotImplementedError
    def reset(self):
        raise NotImplementedError
class Game(AbstractGame):
    def start_hand(self, current_balance):
        while True:
            start = input(f"You are starting ${current_balance}. Would you like to play a hand? ")
            if start.lower() == 'yes':
                break
            elif start.lower() == 'no':
                print(f'Game ended. You are left with ${current_balance}')
                sys.exit()
        self.play(current_balance)

    def play(self, current_balance):
        # generate deck and shuffle deck
        current_deck = Deck()
        current_deck.shuffle_deck()
        starting_balance = current_balance
        bet = float(input("Place your bet: "))
        # while loop to get valid input
        while bet < 1: 
            print("The minimum bet is $1.")
            bet = float(input("Place your bet: "))

        while bet > current_balance:
            print(f'You do not have sufficient funds.')
            bet = float(input("Place your bet: "))

        # Get player's hand and total value
        player_hand = current_deck.get_hand()
        current_balance -= bet
        player = Player(current_balance, player_hand, current_deck.get_total_value(player_hand))
        
        # Get Dealer's hand and total value
        dealer_hand = current_deck.get_hand()
        dealer = Dealer(dealer_hand, current_deck.get_total_value(dealer_hand))

        # Print dealer's hand (with Unknown) and player's hand
        print(f"You are dealt: {player.get_cards()[:]}")
        print(f"The dealer is dealt: {dealer.get_cards()[-3]}, Unknown")
        
        # Hit or stay sequence for players
            # if player.total_hand_value > 21:
            #     break
        if player.total_hand_value == 21 and dealer.total_hand_value == 21:
            print("You tie, Your bet has been returned")
            player.current_balance += bet
        elif player.total_hand_value == 21 and dealer.total_hand_value != 21:
            print(f"Blackjack! You win ${bet}")
            player.current_balance += bet*2.5
        else:
            hit_or_stay = input("Would you like to hit or stay? ")  
            while True:
                if hit_or_stay == 'hit' or hit_or_stay == 'stay':
                    break
                else: 
                    print('That is not a valid option.')
                    hit_or_stay = input("Would you like to hit or stay? ")  

            while hit_or_stay.lower() == "hit":
                player.current_hand = current_deck.hit(player.current_hand)
                player.total_hand_value = current_deck.get_total_value(player.current_hand)
                print(player.total_hand_value)
                print(f"You now have {player.get_cards()[:-1]}")
                if player.total_hand_value > 21:
                    print(f"Your hand value is over 21 and you lose ${bet}")
                    break
                hit_or_stay = input("Would you like to hit or stay? ") 

            while hit_or_stay.lower() == 'stay':
                print(f"The dealer has {dealer.get_cards()}")
                if dealer.total_hand_value < 16:
                    dealer.current_hand = current_deck.hit(dealer.current_hand)
                    print(f"The dealer hits and is dealt: {dealer.get_cards()}")
                    dealer.total_hand_value = current_deck.get_total_value(dealer.current_hand)
                    if dealer.total_hand_value > 21:
                        print(f"The dealer busts, you win ${bet}")
                        player.current_balance += bet*2
                        break
                else: 
                    print(f"The dealer stays.")
                    if dealer.total_hand_value > 21:
                        print(f"The dealer busts, you win ${bet}")
                        player.current_balance += bet*2
                        break
                    elif dealer.total_hand_value > player.total_hand_value:
                        print(f"The dealer wins, you lose ${bet}")
                        break
                    elif dealer.total_hand_value < player.total_hand_value:
                        print(f"You win {bet}")
                        player.current_balance += bet*2
                        break
                    else:
                        print("You tie. Your bet has been returned.")
                        player.current_balance += bet
                        break 
                
        if player.current_balance > 0:
            self.start_hand(player.current_balance)
        else:
            print("You've ran out of money. Please restart this program to try again. Goodbye.")
            sys.exit()
