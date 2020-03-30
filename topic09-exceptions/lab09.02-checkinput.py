# 
# Read in a number from the keyboard and subtract 10% from the number
# throw an exception if the input is less then 0
percent = 0.90 # 1 - 0.10
number = float(input("enter number :"))
# The easiest way is to do an assert, 
# which is fine, but it does not give much information to  
# work out what happen
#assert (number >= 0) # will throw an AssertError
# another way would be to raise an exception
# this way you can put in more information
if (number < 0 ):
    raise ValueError("input should be less than 0 ({})".format(number))

newNumber = number * percent
print (" {} minus 10% is {} ".format(number,newNumber))