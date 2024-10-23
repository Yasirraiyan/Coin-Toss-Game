import random
Cointoss=["Head","Tail"]
Computer_choosen_toss=random.choice(Cointoss)
score=0
chances=10
print("Welcome to our coin toss game!")
while(chances>0):
    player_guess=input("Guess a cointoss").strip().lower()
    if player_guess==Computer_choosen_toss:
        print("Your guess is correct!")
        score+=1
        print(f"Your Score is:{score}")
    else:
            print("Wrong Guess!!")
            chances-=1
            if chances==0:
                print("Game Over!")
                print(f"Your final score is:{score}")
