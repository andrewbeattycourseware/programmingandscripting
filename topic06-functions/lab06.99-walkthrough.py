students=[]

def displayMenu():
    print("MENU")
    print("\ta) Add Student")
    print("\tv) View student")
    print("\tq) quit")
    choice = input("select one:")
    return choice

def readModules():
    modules = []
    currentName = input("\t\tEnter Module name (blank to end):")
    while currentName != '':
        module = {}
        module['name']=currentName
        module['grade'] = input("\t\tEnter grade:")
        modules.append(module)

        currentName = input("\t\tEnter next Module name(blank to end):")

    return modules

def doAdd():
    global students
    #print("in do Add")
    student = {}
    student["name"] = input("\tEnter student name:")
    student["modules"]=readModules()
    students.append(student)


def displayModules(modules):
    print("\t\tName\tGrade")
    for module in modules:
        print("\t\t{}\t{}".format(module['name'], module['grade']))

def doView():
    print ("all students")
    for student in students:
        print ("\t{}".format(student['name']))
        displayModules(student['modules'])

#main
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice =='q':
        pass
    else:
        print("please select a, v or q ")

    choice = displayMenu()