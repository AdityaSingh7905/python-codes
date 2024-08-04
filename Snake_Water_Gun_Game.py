import random
dict={'W':"Water",'S':"Snake",'G':"Gun"}
i=0
comp_won=0#Takes number of points won by computer
user_won=0#Takes number of points won by user
while(i<10):
        key=random.choice(list(dict.keys()))
        #print(key)
        print("Welcome!! in the Snake Water and Gun game...")
        choice=input("Press 'W' for Water,'S' for Snake,'G' for Gun:\n")
        inp=choice.upper()
        print(inp)
        if inp=='W' or inp=='S' or inp=='G':
           if key == 'S' and inp == 'W': comp_won +=2
           elif key == 'W' and inp == 'G': comp_won +=2
           elif key == 'G' and inp == 'S': comp_won +=2
           if key == 'W' and inp == 'S': user_won += 2
           elif key == 'G' and inp == 'W': user_won += 2
           elif key == 'S' and inp == 'G': user_won += 2
           elif key == inp :
             comp_won+=1
             user_won+=1
        else:
            print("Wrong Input!!Please try again..")
            break
        i=i+1

if  comp_won>user_won:
       print("Points earned by computer:",comp_won)
       print("Points earned by user:",user_won)
       print("Computer Won!!Better Luck Next Time.")
elif comp_won<user_won:
       print("Points earned by computer:",comp_won)
       print("Points earned by user:",user_won)
       print("You Won!!Well Played.")
elif comp_won==user_won and comp_won>0 and user_won>0:
       print("Points earned by computer:",comp_won)
       print("Points earned by user:",user_won)
       print("Game Draw!!!")


