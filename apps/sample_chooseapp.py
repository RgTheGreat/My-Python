import datetime
import random

date = datetime.datetime.now()

id = ["126705gh9320GJ", "jhkf56820pokl", "98hy12m#jfdl", "912%ndlpo(8ks//"]

print(date.strftime("%D"))

x = input("Type elements by space: ")


print("\n\n")
data = x.split()
print("list is ", data)
print("\n\n")


y = input("type 'help' to use: ")


dt = {
  "type": id,
  "content": data
}


# add a while if needed

def main(len):
  while 1:
    if y == "check":
      print(random.choice(data))
    elif y == "help":
        print("check = do the main thing \n\nget id = get a unique id for your list \nuse id = use a unique id: ")
    elif y == "get id":
        print(random.choice(id))
    elif y == "use id":
        z = input("id: ")
        if z in id:
          print("used!")
    x = len(data)
main(len)
