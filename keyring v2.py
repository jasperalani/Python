print("PGP Keyring v2");

def newKey(kT):
    print("Enter key (CTRL-D to finish):");
    key = "";
    while True:
        try:
            line = input("");
        except EOFError:
            break;
        key = key + line;
    if(kT == "pr"):
        privKeyring = open("keyring/privKeyring", "a");
        privKeyring.write(key);
        privKeyring.close();
        print("Successful");
    elif(kT == "pb"):
        pubKeyring = open("keyring/pubKeyring", "a");
        pubKeyring.write(key);
        pubKeyring.close();
        print("Successful");

def readKey(kT):
    if(kT == "pr"):
        privKeyring = open("keyring/privKeyring", "r");
        print(privKeyring.readlines());
        privKeyring.close();
    elif(kT == "pb"):
        pubKeyring = open("keyring/pubKeyring", "r");
        print(pubKeyring.readlines());
        pubKeyring.close();
        
def clearKey(kT):
    if(kT == "pr"):
        privKeyring = open("keyring/privKeyring", "w");
        privKeyring.close();
        print("Successful");
    elif(kT == "pb"):
        pubKeyring = open("keyring/pubKeyring", "w");
        pubKeyring.close();
        print("Successful");

def start():
    c = input("\nAdd a new key (a)\nRead existing key (r)\nClear keyring (c)\n");
    c = str.lower(c);
    
    keyType = input("Private or Public key? (pr) (pb)\n");
    keyType = str.lower(keyType);

    if(c == "a"):
        newKey(keyType);
    elif(c == "r"):
        readKey(keyType);
    elif(c == "c"):
        clearKey(keyType);

start();
