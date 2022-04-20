# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:26:42 2021

@author: Brandon Chamberlain

Rock Paper Scissors
"""
# sys module is to break the loop when 'stop' is entered by the user and exit the program
import sys

# random module is for the computer to randomly choose one of the elements in a list
import random

# time module is for effect and delayed output for easier readability
import time

# Used Global variables
player_choice = str()
computer_choice = str()
player_score = 0
number_of_games = 0
possible_inputs = ['rock', 'paper', 'scissors', 'stop', 'stats']
history_player_choice = []
history_computer_choice = []
history_win_loss = []


# game function is passed the player_choice variable after verified as valid option
def game(player_choice):
    
    # Reset game result to 0 for each iteration
    game_result = 0
    
    # Randomly choose an element from the list
    computer_choice = str(random.choice(['rock', 'paper', 'scissors']))
    print('Rock...')
    time.sleep(1)
    print('Paper...')
    time.sleep(1)
    print('Scissors...')
    time.sleep(1)
    print('SHOOT!')
    time.sleep(0.5)
    print('You chose {} - The computer chose {}'.format(player_choice, computer_choice))
    
    if player_choice == 'rock':
        if computer_choice == 'rock':
            game_result += 0
        if computer_choice == 'paper':
            game_result += -1
        if computer_choice == 'scissors':
            game_result += 1
            
    if player_choice == 'paper':
        if computer_choice == 'rock':
            game_result += 1
        if computer_choice == 'paper':
            game_result += 0
        if computer_choice == 'scissors':
            game_result += -1
    
    if player_choice == 'scissors':
        if computer_choice == 'rock':
            game_result += -1
        if computer_choice == 'paper':
            game_result += 1
        if computer_choice == 'scissors':
            game_result += 0
                   
    if game_result == 0:
        print('Tie Game!')
        history_win_loss.append('Tie')
    if game_result == 1:
        print('You WIN!')
        history_win_loss.append('Win')
    if game_result == -1:
        print('Computer Wins')
        history_win_loss.append('Loss')
    
    # Add player and computer choices to historical list since lists are global
    history_player_choice.append(player_choice)
    history_computer_choice.append(computer_choice)
            
    time.sleep(2)
    return game_result

# valid_choice function is passed the user input to verify as a valid selection
# this function also stops the program when 'stop' is entered by the user
def valid_choice(player_choice):
    while player_choice not in possible_inputs:
        print('You must choose rock, paper, scissors, or stop. Please retry your selection')
        player_choice = str.lower(input('Please re-enter your selection: '))
    
    if player_choice == 'stop':
        sys.exit()
        
    return player_choice
  
if __name__ == '__main__':  
      
    print("Welcome to Brandon Chamberlain's Rock, Paper, Scissors!!")

    # Intentional infinite loop only broken by the user entering 'stop'
    while 0 == 0:
        print('\nPlease choose one of the following:')
        print('"Rock", "Paper", or "Scissors" to play')
        print('"Stop" to quit playing')
        print('"Stats" to see your stats for this session')
        
        # User input - player_choice and call the valid_choice function to confirm validity
        player_choice = str.lower(input('Make your selection: '))
        
        # player_choice input may need updated if an invalid selection was made intially. This is returned from the valid_choice function
        player_choice = valid_choice(player_choice)
        
        # Stats printout if 'stats' is entered then returns to beginning of loop
        if player_choice == 'stats':
            print('Number of games: ', number_of_games)
            print('Overall Score: ', player_score)
            print("Player's Choices: {}".format(', '.join(map(str, history_player_choice))))
            print("Computer's Choices: {}".format(', '.join(map(str, history_computer_choice))))
            print('Win/Loss History: {}'.format(', '.join(map(str, history_win_loss))))
            time.sleep(2)
        
        # If not stats, then proceed with the game using the input variable and record number of games and score
        else:
            number_of_games += 1
            player_score += game(player_choice)    