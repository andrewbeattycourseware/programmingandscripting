try:
    #this code does not through a name error
    b = 2
    a = b
    # but does throw a TypeError here
    b[10] = 'this is not good'
#catch name errors
except NameError as ne:
    print("a Name error occured")
    print(ne)

#catch all other errors (this is NOT good programming practice)
# it makes your code very hard to debug
# where did it go wrong? what was the type of error?   
except Exception as e: 
    print("whoops something went wrong")
    print (e)