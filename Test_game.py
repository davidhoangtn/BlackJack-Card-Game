"""
Players involved:
    Player:
    Dealer:
Objective:
    End the hand/round with a hand with higher value than the
    hand the dealer has without going over 21
Card value:
    Ace: 1, 10 or 11
        When Ace is dealt, value depends on which card is dealt 
        (not over 21)
    King, Queen or Jack: 10
    Others: card value
Win/Lose condition:
    Bust: value of your hand over 21 --> immediately lose
    Value: lower than dealer's
Rounds:
    Player places a bet: 
        _between 1 and amount of money the currently have
    Two cards are dealt to both player and dealer
        _player: both cards face up
        _dealer: one dealt face down
    Players turn: Hit or stay
        _Hit: dealt another card (hit as many times as they like
            until exceeds 21 (bust))
            (>=17 they must stay)
        _Stay: their turn is over, value of hand is locked
            may stay at any point during their turn
                (<16 must hit)
    Dealer's turn: Hit or stay (flip over their face down cards)
        _Hit or stay according to rules above
Outcome:
    Player wins: bet is doubled and returned to players
    Dealer wins: bet is taken from player
    Tie: Original bet is returned to player
Special Rule:
    Natural 'blackjack': 
        _If player wins with natural blackjack, get paid x2.5 times bet and returned to them
        _both dealer and player have natural, it is a tie. 
Bet:
    _Player starts with $500, minimum bet will be $1
    _Before asking to bet, you should ask them if they would like to play a hand
        _If choose not to play, game should end and tell player how much money they left with.
        _If player has $0, the game should end and the game restarted for player ot try again
"""

from game import Game, AbstractGame

STARTING_BALANCE = 500
game = Game()
game.start_hand(STARTING_BALANCE)




