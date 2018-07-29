from random import randint
pla=input("player, make your choice: ").lower()
ran=randint(0,2)
if ran==0:
    comp="rock"
elif ran==1:
    comp="paper"
else:
    comp="scissors"  

print("the computer played: {}".format(comp))

if pla==comp:
    print("it's a tie")
elif pla=="rock":
    if comp=="paper":
        print("the computer won")
    else: 
        print("you won")    
elif pla=="paper":
    if comp=="scissors":
        print("the computer won")
    else:
    	print("you won")
elif pla=="scissors":
    if comp=="rock":
    	print("the computer won")
    else:
        print("you won")
else:
	print("you have mistyped")





