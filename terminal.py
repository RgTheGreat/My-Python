import pickle
import os
import shutil
commands = {
    "ls": os.listdir()
}

username = input("Enter username:")

while 1:
    cmd = input("C/Users/~~ ")
    if cmd in commands.keys():
        print(os.listdir())
    else:
        pass

def savepickle(username):
    with open("username.pkl", "wb") as userpickle:
        pickle.dump(username, userpickle)

