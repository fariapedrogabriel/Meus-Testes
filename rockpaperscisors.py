def play_game():
    import random

    play = True

    while play:

        choices = ("rock", "paper", "scissors")

        player_choice = input('Choose between Rock, Paper, and Scissors: ').lower()
        pc_choice = random.choice(choices)

        while player_choice not in choices:
            player_choice = input('Invalid Choice! Please select Rock, Paper, or Scissors!').lower()

        if player_choice == pc_choice:
            print(f'You picked "{player_choice}" and the computer picked "{pc_choice}". This is a draw!')
        elif (player_choice == "paper" and pc_choice == "rock") or \
             (player_choice == "rock" and pc_choice == "scissors") or \
             (player_choice == "scissors" and pc_choice == "paper"):
            print(f'You picked "{player_choice}" and the computer picked "{pc_choice}". You win!')
        else:
            print(f'You picked "{player_choice}" and the computer picked "{pc_choice}". You lose!')
                
        answer = input('Play again? Say YES or NO: ').lower()
        while answer not in ("yes", "no"):
            answer = input('Please choose only YES if you want to play again or NO to exit: ')
        
        if answer == "no":
            play = False

if __name__ == "__main__":
    play_game()
        
            
               
