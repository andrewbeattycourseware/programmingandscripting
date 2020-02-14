students= []
def readModules():
    modules = []
    moduleName = input("\tenter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tenter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tenter next module name (blank to quit) :").strip()

    return modules

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

#test
doAdd()
doAdd()
print (students)