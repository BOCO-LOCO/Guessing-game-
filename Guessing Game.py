import random


def play():
    print("__"*31)
    print("----------Hello and welcome to Number Guessing game----------")
    print("__"*31)
    number = random.randint(1,100)
    score = 5
    while score > 0:
        #get the user input
        guess = input("\n-Guess a number between 1 and 100: ").strip()
        #check if the input is a number
        if not guess.isdigit():
            print("-----Please enter a Number-----")
            continue
        #convvert the guess to int
        guess = int(guess)
        
        #check the range of the input
        if guess < 1 or guess > 100:
            print("-----Please enter a number between 1 and 100-----")
            continue
        
        #check if the guess is correct
        if guess == number:
            print("-----Congratulations! You guessed the number-----")
            break
        
        elif guess < number:
            score -= 1
            print(f"\n-----Too Low, You have a {score} guesses left-----")
            
        elif guess > number:
            score -= 1
            print(f"\n-----Too High, You have a {score} guesses left-----")
            
        #check the score of the guessing
        if score == 0:
            print("\n-----Game Over! You have run out of guesses-----")
            print(f"\n-----The number was {number}-----")
            break
        else:
            print("__"*40)  #seperator
    
# playing loop
while True:
    play()
    choise = input("\nDo you wanna play again? (y/n)").lower()
    if choise != 'y':
        print("\nThanks for playing and good bye.")
        break