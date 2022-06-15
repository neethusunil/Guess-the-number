from random import randint, random
import art

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")
number = randint(1,100)


if(level == "easy"):
    
    for i in range(10,0,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(guess<number):
            if(i==1):
                print("Too Low!\nYou Lose")
            else:
                print("Too Low! Guess Again")
        elif(guess>number):
            if(i==1):
                print("Too high!\nYou Lose")
            else:
                print("Too high! Guess Again")
        elif(guess==number):
            print("You win")
            break

if(level == "hard"):
    
    for i in range(2,0,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(guess<number):
            if(i==1):
                print("Too Low!\nYou Lose")
            else:
                print("Too Low! Guess Again")
        elif(guess>number):
            if(i==1):
                print("Too high!\nYou Lose")
            else:
                print("Too high! Guess Again")
        elif(guess==number):
            print("You win")
            break        