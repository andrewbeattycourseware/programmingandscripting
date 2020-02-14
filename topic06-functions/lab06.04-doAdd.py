students= []
def readModules():
    return []
def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

#test
doAdd()
doAdd()
print (students)