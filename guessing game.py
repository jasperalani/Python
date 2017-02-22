import random
x = 1;
while x:
    diff = input("Choose difficulty:\nEasy (e)\nMedium (m)\nHard (h)\n");
    diff = str.lower(diff);
    if(diff == "e"):
        break;
    elif(diff == "m"):
        break;
    elif(diff == "h"):
        break;

def game(d):
    if(d == "e"):
        tries = 10;
        maxNum = 10;
        print("\nEasy selected.");
    elif(d == "m"):
        tries = 5;
        maxNum = 20;
        print("\nMedium selected.");
    elif(d == "h"):
        tries = 3;
        maxNum = 30;
        print("\nHard selected.");

    num = random.randrange(1, maxNum);
    x = 0;
    while x < tries:
        guess = input("Guess a number below " + str(maxNum) + ": ");
        if(int(guess) > maxNum):
            print("That is not below " + str(maxNum) + ".\n");
        else:
            if(int(guess) == num):
                print("Correct");
                break;
            else:
                print("Wrong");
                x = x + 1;

        if(x == tries):
            print("You've run out of guesses.");
            break;
        
game(diff);
