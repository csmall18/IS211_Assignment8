# Cameron Small
# Week 8

import time
import random
from abc import ABC, abstractmethod
random.seed(0) # remove for random play, but keep for testing purposes

class Player(object): # create player class with initialized values
    def __init__(self, player_num, score=0):
        self.player_num = player_num
        self.score = score

class Computer(Player): # create computer player class that inherits from player class
    def __init__(self, player_num, score=0):
        super().__init__(player_num, score)
        print(f"Computer will play as player {self.player_num}.")



class PlayerFactory(object): # create player factory class to create players
    @staticmethod
    def create_player(self, player_type, player_num, score=0):
        type_clean = player_type.strip().lower()
        if type_clean == "human":
            return Player(player_num, score)
        elif type_clean == "computer":
            return Computer(player_num, score)
        else:
            raise ValueError("Invalid player type. Must be 'human' or 'computer'.")

def play_turn(curr_player):
    win = False
    valid_input = False
    roll = 0
    print(f"Player {curr_player.player_num}'s turn. Current score: {curr_player.score}")
    choice = input("Would you like to roll ('r') or hold ('h')? ")
    while not valid_input:
        if choice == 'r':
            valid_input = True
            while choice == 'r' and curr_player.score < 100:
                roll = random.randint(1, 6)
                if roll == 1:
                    print("You rolled a 1. Your turn is over.")
                    return False, 0 # return no result and no winner
                elif roll != 1:
                    print(f"You rolled a {roll}")
                    curr_player.score += roll
                    if curr_player.score >= 100:
                        win = True
                        return win, curr_player.player_num
                    print(f"Your score is: {curr_player.score}")
                    choice = input("Would you like to roll ('r') or hold ('h')? ")
        elif choice == 'h':
            valid_input = True
            print("You chose to hold. Your current score is:", curr_player.score)
            return False, 0
        else:
            choice = input("Invalid input. Please enter 'r' to roll or 'h' to hold: ")
    return False, 0 # return no result and no winner if the loop ends without a win
def main():
    start_time = time.perfect_counter()
    print("Welcome to the Pig Game!")
    player1 = Player(player_num=1)
    player2 = Computer(player_num=2)
    turn_count = 0
    outcome = False
    winner = 0
    timed_out = False

    while not outcome: # until there is a winner or time runs out, keep playing turns
        outcome,winner = play_turn(player1)
        turn_count += 1
        if outcome:
            break
        outcome,winner = play_turn(player2)
        turn_count += 1
        if outcome:
            break

    print(f"Player {winner} wins!")
    print(f"Total turns: {turn_count}")
    return 0

#main()