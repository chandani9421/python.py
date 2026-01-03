from random import randint
easy_level_turns = 10
hard_level_turns = 5
turns = 0

#function to check_answer
def check_answer(user_guess, actual_answer, turns):
    """check_answer against guess, returns the number of turns remaning"""
    if user_guess < actual_answer:
        print ("Too low.")
        return turns - 1
    elif user_guess > actual_answer:
        print ("Too hight.")
        return turns - 1
    else:
        print(f"You got it! the answe was {actual_answer}")

# function to set diffecultiy
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    # choose a random number between 1 and 100
    print("Welcome to the No guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # set difficulty
    turns = set_difficulty() 
    print(f"You have {turns} attempts to guess the number.")

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
         print(f"You have {turns} attempts to guess the number.")
        # Lets the user guess the number
         guess = int(input("Make a guess:"))
         turns = check_answer(guess, answer, turns)
         if turns == 0:
             print("You've run out of guesses, you lose.")
             return
         elif guess != answer:
             print("Guess again.")

    # Track the number of turns and reduce by 1 if they get it wrong

game()