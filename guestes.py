import random
print("welcome to ghe Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_guess= random.randint(1,100)
guesses = 10

user_input = input("Choose a difficulty. Type 'easy' or  'hard': ")
if user_input == 'easy':
        while True:
         
            print(f"You have 10 guesses to get it right.")
            user=int(input("Make a guess :"))
            if user < number_guess:
                print("Too low!")
                guesses -= 1
                print(f" You have {guesses} guesses left.")
                user=int(input("Make a guess :"))
            elif user > number_guess:
                print("Too high!")
                guesses -= 1
                print(f" You have {guesses} guesses left.")
                user=int(input("Make a guess :"))
            
            else:
                
                print(f"Yay! You got it right! The number was {number_guess}.") 
                break
                
                
            
            
