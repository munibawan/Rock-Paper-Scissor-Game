import random

#Welcome
print("Welcome to Rock, Paper, Scissor game!")

#While loop
while True:
    #User choice
    user_choice = input("Type Rock, Paper or Scissor: ")
    
    #Computer choice
    options = ['rock', 'paper', 'scissor']
    rand = random.randint(0, 2)
    computer_choice = options[rand]
    
    #Result
    if user_choice.lower() ==  computer_choice:
        print("It's a tie")
    elif user_choice.lower() == "rock" and computer_choice == "scissor": 
        print("You Win")
    elif user_choice.lower() == "scissor" and computer_choice == "paper": 
        print("You Win")
    elif user_choice.lower() == "paper" and computer_choice == "rock": 
        print("You Win")
    elif user_choice.lower() == "rock" and computer_choice == "paper": 
        print("You lost")
    elif user_choice.lower() == "scissor" and computer_choice == "rock": 
        print("You lost")
    elif user_choice.lower() == "paper" and computer_choice == "scissor": 
        print("You lost")
    else:
        print("Type only Rock, Paper or Scissor to play this Game")

    print('Computer chose: ' + options[rand])
    
    #If user want's to play again
    again = input("Want to try again? ")
    if again.lower() == "yes":
        continue
    else:
        print("Thank you for playing this game")
        break

#The program have ended