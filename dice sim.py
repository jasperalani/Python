import random
rolls = [];
x = 1;
while x:
    die = input("How many sides on die: ");
    side = random.randrange(1,int(die));
    print("You rolled a " + str(side));
    rolls.append(side);
    print(rolls);
    again = input("Again? (y) (n)\n");
    if(again != "y"):
        break;
    
