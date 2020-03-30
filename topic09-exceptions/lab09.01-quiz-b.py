try:
    a-b
except NameError as ne:
    print(ne)
else:
    print("How now")
finally:
    print("brown cow")