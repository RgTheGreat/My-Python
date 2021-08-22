# some python programs:


person1 = {
  "name" : "a",
  "age" : 19,
  "DOB" : 1981
}


person2 = {
  "name" : "b",
  "age" : 10,
  "DOB": 2000
}


if person1["DOB"] < person2["DOB"]:
	print(person1["name"] + " is born earlier than " + person2["name"])
else:
	print(person2["name"] + " is born earlier than " + person1["name"])
	
	
	#or:  
	#you can do 'elif' or else 
	
if person1["age"] > person2["age"]:
	print(person1["name"] + " is born earlier than " + person2["name"])
else:
	print(person2["name"] + " is born earlier than " + person1["name"])

  