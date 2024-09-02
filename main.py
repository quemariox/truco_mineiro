import random
import create_deck as cdk
import dist_cards as dcs
import play_round as prd
import play_match as pmt

def main():
    global_score = [0,0]
    play = str(input("Deseja jogar um 'Truquinho Mineiro' ??? [s/n]"))

    while play.lower() == 's':
        result_match = pmt.play_match()
        if result_match[0] > result_match[1]:
            return print("Parabéns, você é um campeão, nego !!!")
        else:
            return print("Try again... and again... over and over again !!!")

main()
