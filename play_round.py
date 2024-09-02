import random
import create_deck as cdk
import dist_cards as dcs

def play_round():
    
    #0.creating a list of 4 players hands
    hands = dcs.dist_cards()
    
    #1.initializing the score of this round, table state and a carrier variable "card"
    partial_score = [0,0]
    table = []
    card = []

    #2.distributing cards to players
    player1a, player3a = hands[0], hands[2] #team1
    player2b, player4b = hands[1], hands[3] #team2
    
    #3.defining player position based on table state
    position = len(table)
    
    #4.multiplier depends on the strategy employed
    multiplier = 1
    
    while max(partial_score) < 2: #play a best of three
        print(f"\n Score parcial {partial_score}")

        #5.each player drops 1 card on table
        print("\n Cartas player1a:", player1a)
        choice = int(input("\n Qual carta deseja jogar? [0,1,2]"))
        card = player1a.pop(choice)
        table.append(card)
        card = []
        print("\n Mesa:", table)
    
        print("\n Cartas player2b", player2b)
        choice = 0 
        card = player2b.pop(choice)
        table.append(card) 
        print("\n Mesa:", table)
        
        print("\n Cartas player3a", player3a)
        choice = 0
        card = player3a.pop(choice)
        table.append(card)
        print("\n Mesa:", table)

        print("\n Cartas player4b", player4b)
        choice = 0
        card = player4b.pop(choice)
        table.append(card) 
        print("\n Mesa:", table)
        
        #6.defining the winner of this round 
        winner = table.index(max(table))
        if winner == 0 or winner == 2:
            partial_score[0] += 1
            print("\n Equipe 1 VENCEU a rodada!")
        else:
            partial_score[1] += 1
            print("\n Equipe 2 VENCEU a rodada!")
        
        #7.reset table
        table = []

    #8.return the partial_score and the multiplier for points of this round
    return list(partial_score), int(multiplier)