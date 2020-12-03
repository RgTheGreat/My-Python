#Strings
RGstr = "CODING"
RGit = iter(RGstr)

print(next(RGit))
print(next(RGit))
print(next(RGit))
print(next(RGit))
print(next(RGit))
print(next(RGit))

#Iterator with loop
mystr = "coding"

for x in mystr:
  print(x)
  
  
  #numerals
  for i in range(100):
	print(i)
  
  #Scope
  def Myfunc():
    x = 300
print(x)

myfunc()

#function inside a function
def Rgfunc():
  x = 789
  
def Rginnerfunc():
print(x)
Rginnerfunc()

Rgfunc()

#Global scope
x = 298
 def MYfunc():
 print(x)
 
MYfunc()
 
 print(x)
 
 
