
def displayMenu():
    
    print("what would you like to do?")
    print("\t(a) add new student")
    print("\t(v) view students")
    print("\t(q) quit")
    choice = input("type one letter (a/v/q):").strip()

    return choice

def doAdd():
    print("in adding")
def doView():
    print("in viewing")

#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
        
        