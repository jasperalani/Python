def inputKey(prompt):
    print(prompt, end='', file=sys.stderr)
    return sys.stdin.readline()

c = input("Add new key (a)\nRead existing keys (r)\nClear keyring (c)\n");
c = str.lower(c);

if(c == "a"):
    x = input("Private or Public key? (pr) (pb)\n");
    x = str.lower(x);


    key = "";
    while True:
        try:
            line = input("Enter key:\n");
        except EOFError:
            break;
        key = key + line;


    
    if(x == "pr"):
        privKeyring = open("privKeyring", "a");
        privKeyring.write(key);
        privKeyring.close();
        print("Successful");
    elif(x == "pb"):
        pubKeyring = open("pubKeyring", "a");
        pubKeyring.write(key);
        pubKeyring.close();
        print("Successful");
elif(c == "r"):
    x = input("Private or Public key? (pr) (pb)\n");
    if(x == "pr"):
        privKeyring = open("privKeyring", "r");
        print(privKeyring.readlines());
        privKeyring.close();
    elif(x == "pb"):
        pubKeyring = open("pubKeyring", "r");
        print(pubKeyring.readlines());
        pubKeyring.close();
elif(c == "c"):
    privKeyring = open("privKeyring", "w");
    privKeyring.close();
    privKeyring = open("privKeyring", "r");
    privKeyring.close();
    print("Successful");
