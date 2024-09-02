import random
import create_deck as cdk
import dist_cards as dcs
import play_round as prd

def play_match():
    
    global_score = [0,0]
    result_round = ()
    partial_score = [0,0]
    match_count = 0
    multiplier = 1

    while max(global_score) <= 12:
        print(f"\n Rodada: {match_count} \n Global Score: {global_score}")
        result_round = prd.play_round()
        partial_score = result_round[0]
        multiplier = result_round[1]
                
        if partial_score[0] > partial_score[1]: 
            global_score[0] += 1*multiplier
            multiplier = 1
            return global_score
        elif partial_score[1] > partial_score[0]:
            global_score[1] += 1*multiplier
            multiplier = 1
            return global_score
