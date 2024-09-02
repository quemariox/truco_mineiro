import create_deck as cdk

def dist_cards():

    #0.inputs
    hands = []
    hand = []
    n_players = 4

    deck = cdk.create_deck()

    #1.creatind 4 hands with 3 cards each:
    for player in range(n_players):
        hand = []
        for card in range(3):
            hand.append(deck.pop())
        hands.append(hand)
        
    #2.return
    return list(hands)