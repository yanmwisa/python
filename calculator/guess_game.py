import random
while True:
    print("welcome to ghe Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_guess= random.randint(1,100)
    max_guesses=10
    guesses = 0
    guess=0
    max_guess=5

    user = None
    user_input = input("Choose a difficulty. Type 'easy' or  'hard': ")
    if user_input == 'easy':
            print(f"You have 10 guesses to get it right.")
            
            while user !=number_guess and guesses < max_guesses:
                    user = int(input("Make a guess: "))
                    if user < number_guess:
                            print("Too low!")
                            guesses +=1
                            print(f"you have {guesses}  attempts used")
                    elif user > number_guess:
                            print("Too high!")
                            
                            print(f"you have {guesses}  attempts used")
                    elif user == number_guess :
                            print(f"You got it! the number was {number_guess} congratulation!")
            if guesses != number_guess:
                            print(f"Sorry, you've used all {max_guesses} attempts. The correct number was {number_guess}.")
                                   
                            
    else :
            print(f"You have 5 guesses to get it right.")
            while user !=number_guess and guess < max_guess:
                    user = int(input("Make a guess: "))
                    
                    if user < number_guess:
                            print("Too low! ")
                            guess +=1
                            print(f"you have {guess} attempts used")
                    elif user > number_guess:
                            print("Too high!")
                            
                            print(f"you have {guess}  attempts used")
                            
                    elif user == number_guess :
                            print(f"You got it! the number was {number_guess} congratulation")
            if guess != number_guess:
                            print(f"Sorry, you've used all {max_guess} attempts. The correct number was {number_guess}.")

    play_again= (input("would you like to play again yes or no :")).lower()
    if play_again != "yes":
            print("Thanks for playing!")
            break
        
        
        
                         

                        
               
               

                
                
  
       
        
                

                        



        
            
            
                
                
                
                
            
            
