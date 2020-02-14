currentBook = {
    "title" : "Harry Potter eats his dinner",
    "author": "Just Kidding Rowling",
    "price" : 12
}
#print dictionary object
print (currentBook)

# print just the author
print (currentBook["author"])

# create and set attribute ISBN
currentBook["ISBN"] = "123455"

# user for loop to iterate through the currentBook's values
# notice the order the for loop gives the values.
print ("the current book has these values:")
for value in currentBook.values():
    print ("  => {}".format(value))