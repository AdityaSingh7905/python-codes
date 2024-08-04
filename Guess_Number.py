#Guessing the number
#You can only try 5 times
var=18
i=1  # i holds record of number of times man is guessing
while(1):
     if i<=5:
        num=int(input("Enter your number:\n"))
        if num==var:
            print("Congratulations! You won.You took",i,"guesses to win this game..")
            break
        elif num<var:
            print("Try another time!Try to input number greater than this!")
            print("No. of guesses left:",5-i)
        else:
            print("Try another time!Try to input number lesser than this!")
            print("No. of guesses left:",5-i)

     else:
         print("Game Over!Better Luck Next Time!!")
         break

     i=i+1

