
#Arrays
lan = ["HTML", "Python", "Javascript"]
print(lan)

#Array with elements
lan = ["HTML", "Python", "Javascript"]

s = lan[1]
print(s)

#Array with length
lan = ["HTML", "Python", "Javascript"]

l = len(lan)
print(l)


#Classes
class FirstClass:
  x = 3
print(FirstClass)

#Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rigved", 36)
p1.myfunc()


#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("R", "G")
x.printname()

#iterators
firsttuple = ("Apple", "grape", "Melon")
firstit = iter(firsttuple)

print(next(firstit))
print(next(firstit))
print(next(firstit))
