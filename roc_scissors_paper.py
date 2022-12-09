import random
while True: 
    user_action = input("Make your choice - rock, scissors or paper: ")
    possible_actions = ["rock", "scissors", "paper"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choosed {user_action}, computer  choosed {computer_action}.\n")
    if user_action == computer_action:
        print(f"Dead heat")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You won!")
        else:
            print("You lost.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You won!")
        else:
            print("You lost.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You won!")
        else:
            print("You lost.")

    play_again = "" 
    play_again = input("Let's play again? (yes/no): ") 
    if play_again.lower() != "yes": 
        break 
      
