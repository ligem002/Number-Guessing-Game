import random

def random_num():
    return random.randint(1,100)

def difficulty(choice):
    match choice:
        case 1:
            print("\nYou have selected the easy difficulty\n")
            return 10
        case 2:
            print("\nYou have selected the medium difficulty\n")
            return 5
        case 3:
            print("\nYou have selected the hard difficulty\n")
            return 3
        case _:
            print("\nThe default is the medium difficulty\n")
            return 5
 
def game(rounds,number):
    for i in range(rounds):
        x = int(input("Enter your guess: "))
        compare = ""
        answer = False
        if (i == rounds -1) and (x != number):
            print(f"Incorrect! The number was {number}.\n")
        elif x != number:
            if x > number:
                compare = "less"
            else:
                compare = "greater"
            print(f"Incorrect! The number is {compare} than {x}.\n")
        else:
            print(f"Congratulations! You guessed the correct number in {i+1} attempts.\n")
            answer = True
            break
    if answer == False:
        print("Tough luck you ran out of chances")
    replay = input("Do you want to play again (Y/N)? (Default is Y) ")
    play(replay)
    
def intro():
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n""")
    play()
    
def play(choice = "Y"):
    if choice is "Y":
        selection = int(input("Please Select the difficulty level\n \n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n \nEnter your choice: "))
        game(difficulty(selection),random_num())
    elif choice is "N":
        print("Thank you for playing!")

intro()
