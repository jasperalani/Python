a = input("Welcome to the program\n" + "Select (1) for calculator\n");
print(a);
while(a == "1"):
    c = input("\nAddition (1)\nSubtraction (2)\nMultiplication (3)\nDivision (4)\n");
    if (c == "1"):
        fn = input("\nAddition selected\nInput first number: ");
        sn = input("Input second number: ");
        output = int(fn) + int(sn);
        print("\nOutput: " + str(output));
        r = input("Again? (y) (n)\n");
        if (r == "y"):
            a == "1";
        elif (r == "n"):
            break;
    elif (c == "2"):
        fn = input("\nSubtraction selected\nInput first number: ");
        sn = input("Input second number: ");
        output = int(fn) - int(sn);
        print("\nOutput: " +str(output));
        r = input("Again? (y) (n)\n");
        if (r == "y"):
            a == "1";
        elif (r == "n"):
            break;
    elif (c == "3"):
        fn = input("\nMultiplication selected\nInput first number: ");
        sn = input("Input second number: ");
        output = int(fn) * int(sn);
        print("\nOutput: " +str(output));
        r = input("Again? (y) (n)\n");
        if (r == "y"):
            a == "1";
        elif (r == "n"):
            break;
    elif (c == "4"):
        fn = input("\nDivision selected\nInput first number: ");
        sn = input("Input second number: ");
        output = int(fn) / int(sn);
        print("\nOutput: " +str(output));
        r = input("Again? (y) (n)\n");
        if (r == "y"):
            a == "1";
        elif (r == "n"):
            break;
