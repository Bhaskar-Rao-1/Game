import random
while True:
    choices=["scissors","rock","paper"]
    computer=random.choice(choices)
    player=None
    

    while player not in choices:
        player=input("scissors,paper,rock. ").lower().strip()

       
    print("computer:",computer)
    print("player :",player)
    
    if computer==player:
        print ("tie")
    elif player=="rock":
        if computer=="paper":
            print("you lose")
        if computer=="scissors":
            print("you win")
    elif player=="paper":
        if computer=="scissors":
            print ("you lose")
        if computer=="rock":
            print("you win")
    elif player=="scissors":
        if computer=="rock":
            print("you lose")
        if computer=="paper":
            print("you win")
    player_input=input("y for yes and n for no ").lower()
    if player_input!='y':
        break
print("Bye!")
    
        
     
    