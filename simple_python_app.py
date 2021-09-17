# simple beginner code/program


print("User 1")
name = input("Type your name: ")
age = int(input("Type your age: "))
dob = int(input("Type your date of birth: "))

person1 = {
  "name" : name,
  "age" : age,
  "DOB" : dob
}


print("User 2")

name2 = input("Type your name: ")
age2 = int(input("Type your age: "))
dob2 = int(input("Type your date of birth: "))


person2 = {
  "name" : name2,
  "age" : age2,
  "DOB": dob2
}


if person1["DOB"] < person2["DOB"]:
	print(person1["name"] + " is born earlier than " + person2["name"])
else:
	print(person2["name"] + " is born earlier than " + person1["name"]) 
	

if person1["age"] > person2["age"]:
	print(person1["name"] + " is born earlier than " + person2["name"])
else:
	print(person2["name"] + " is born earlier than " + person1["name"])

  
