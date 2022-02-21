class Dealer:
    def __init__(self, current_hand, total_hand_value):
        self.current_hand = current_hand
        self.total_hand_value = total_hand_value
    def get_cards(self):
        ret = ''
        for card in list(self.current_hand.keys()):
            ret += card + ', '
        return ret[:-1]