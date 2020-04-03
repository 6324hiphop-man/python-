import os
def make_another_file():
    if os.path.isfile('text.txt'):
        print("You are trying to create a file that already exists!")
    else:
        f = open('text.txt',"w")
        f.write("This is how you create a new text file")
    print(make_another_file)