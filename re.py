import re


statment = "I live in India"
x = re.search("^I.*India$", statment)

if x:
  print("YES! I live in India!!")
else:
  print("No I don't live in India!")
