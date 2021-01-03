person1 = {
 "name": "Mike",
 "age": 39,
 "DOB": 2002
}

person2 = {
 "name": "Jack",
 "age": 29,
 "DOB": 1981
}



if person1["DOB"] < person2["DOB"]:
  print(person2["name"] + " is born earlier than " + person1["name"] + ".")
elif person1["DOB"] == person2["DOB"]:
  print(person1["name"] + " and " + person2["name"] + "is born on the same year.")
elif person1["DOB"] != person2["DOB"]:
  print(person1["name"] + " and " + person2["name"] + " is not born on the same year.")
else:
  print(person1["name"] +  " is born earlier than " person2["name"])
