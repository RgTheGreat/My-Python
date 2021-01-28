import datetime
import random

date = datetime.datetime.now()

print(date.strftime("%D"))

x = input("Type elements by space: ")


print("\n\n")
data = x.split()
print("list is ", data)
print("\n\n")


y = input("type 'help' to use: ")


dt = {
  "type": "id",
  "get": "id",
  "content": data
}


# add a while if needed

def main(len):
    if y == "check":
      print(random.choice(data))
    elif y == "help":
        print("check = do the main thing \n\nget id = get a unique id for your list")
    elif y == "get id":
        print(id(data))
    elif y == "save id ":
      print(dt)
    x = len(data)
main(len)
