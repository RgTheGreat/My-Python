a = input("Enter your name: ")
b = input("Enter your password: ")
c = input("Enter your age(in letters): ")

data = {
	"username": a,
	"password": b,
    "age": c
}


class fail:
    def __init__(self, exception, prevent):
        self.exception = exception
        self.prevent = prevent

    def printError(self):
        print("Exception: " + self.exception + " Prevention: " + self.prevent) 


class success:
    def __init__(self, statement):
        self.statement = statement

    def printSuccess(self):
        print(self.statement)


for x in data:
    if data[x] == None or data[x] == '':
        error = fail("name/pswd/age not entered", "You have to enter all the inputs") 
        error.printError()
    else:
        succes = success("Loged in!")
        succes.printSuccess()

