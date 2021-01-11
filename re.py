import re


txt = "I live in India"
x = re.search("^I.*India$", txt)

if x:
  print("YES! I live in India!!")
else:
  print("No I don't live in India!")
