import random

def create_deck(SHUFFLE = True):
    
    #0. inputs:
    PIPS_POWER = {'4':4,'5':5,'6':6,'7':7,'J':8,'Q':9,'K':10,'A':11,'2':12,'3':13}
    EMOJI_SUITS = {'Hearts': "\u2665", 'Diamonds': "\u2666", 'Spades': "\u2660", 'Clubs': "\u2663"}
    SHUFFLE = True

    playing_cards = []
    
    #1.creating a 40 cards deck:
    for suit in EMOJI_SUITS.values():
        for pip in PIPS_POWER:
            name = [int(PIPS_POWER[pip]), pip + suit]
            playing_cards.append(name)  

    #2.changing high card values:
    for card in playing_cards:
        if   card[1] == '7♦': card[0] = 14
        elif card[1] == 'A♠': card[0] = 15
        elif card[1] == '7♥': card[0] = 16
        elif card[1] == '4♣': card[0] = 17
        else: card[0] = card[0]
        
    #3.shuffling deck:
    if SHUFFLE == True:
        random.shuffle(playing_cards)
    else:
        playing_cards.sort()
        
    #4.return "DECK"
    return list(playing_cards)