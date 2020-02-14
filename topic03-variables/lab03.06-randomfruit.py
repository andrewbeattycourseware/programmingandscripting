# This program prints out a random fruit

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# we want a random number between 0 and lenght-1
#index = random.randint(0,len(fruits)-1)
#fruit = fruits[index]
fruits.append('Tomato')

# I got this from https://pynative.com/python-random-choice/
fruit = random.choice(fruits)
print("A Random Fruit:{}".format(fruit))