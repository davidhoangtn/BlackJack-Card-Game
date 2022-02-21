import random as rd
class Deck:
    current_deck = []
    @classmethod
    def shuffle_deck(cls):
        suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        cls.current_deck = [value+suit for suit in suits for value in values]
        rd.shuffle(cls.current_deck)
        return cls.current_deck
    
    @staticmethod
    def card_value(card):
        card_value = None
        if card[0].isdigit():
            card_value = int(card[0])
        elif card[0] in ['J', 'Q', 'K', 'T']:
            card_value = 10
        else: 
            card_value = [1, 10, 11]
        return card_value
    
    def hit(cls, hand):
        card_dealt = cls.current_deck.pop(0)
        hand[card_dealt] = cls.card_value(card_dealt)
        return hand

    @classmethod
    def get_hand(cls):
        hand = {}
        for i in range (2):
            card_dealt = cls.current_deck.pop(0)
            hand[card_dealt] = cls.card_value(card_dealt)
            # print(card_dealt)
        return hand

    @staticmethod
    def get_total_value(hand=[]):
        total_value = 0
        for card_value in hand.values():
            if isinstance(card_value, int):
                total_value += card_value
            elif isinstance(card_value, list):
                potential_value = []
                for value in card_value:
                    if total_value + value <= 21:
                        potential_value.append(value)
                total_value += max(potential_value)  
        return total_value



