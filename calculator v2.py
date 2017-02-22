def calculate(m):
    
    fn = input("\nInput first number: ");
    sn = input("Input second number: ");
    fn = int(fn);
    sn = int(sn);
    
    if(m == "1"):
        output = (fn + sn);
    elif(m == "2"):
        output = (fn - sn);
    elif(m == "3"):
        output = (fn * sn);
    elif(m == "4"):
        output = (fn / sn);

    return(output);


    
while(1 == 1):
    c = input("Calculator v2\n\nAddition (1)\nSubtraction (2)\nMultiplication (3)\nDivision (4)\n");
    print(calculate(c));
    r = input("\nAgain? (y) (n)\n");
    if(r != "y"):
        break;
