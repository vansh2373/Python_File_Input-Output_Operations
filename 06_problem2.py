"""
1. there is a game() function which returns hi score of game 
2. Hi-Score file contains previous either previous high score or blank 
3. you need to update the High Score whenever A new high score breaks..
"""
import random 

def game():
    print("You are playing the game..")
    score = random.randint(1,50)

    with open("Hi-Score.txt","r") as f:
       highscore =f.read()
       if (highscore!=""):
           highscore = int(highscore)
       else:
           highscore = 0 

    print(f"Your Score:{score}")
    if(score>highscore):
        with open("Hi-Score.txt","w") as file:
            file.write(str(score))
    
    return score

game()



