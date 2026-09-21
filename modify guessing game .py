import random
win_num=random.randint(1,100)
user_num=int(input("enter the number between 1 to 100 :"))
guess_num=1
game_over=False
while not game_over:
    if win_num==user_num:
        print(f"you win, you guessed in {guess_num} time")
        game_over=True

    else:
        if user_num<win_num:
            print("too low")
            guess_num+=1
            user_num=int(input("guess again:"))

        else:
            print("too high")
            guess_num+=1
            user_num=int(input("guess again:"))
            
