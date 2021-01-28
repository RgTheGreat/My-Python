
while 1:
  a = input("Enter a name for a task: ")
  print("1.", a)
  b = input("Enter a new task : ")
  if b == 'cut':
    del a
  print("1.",a + "\n2.",b)
  c = input("Enter a new task : ")
  print("1.",a + "\n2.",b + "\n3.",c)
  d = input("Enter a new task : ")
  print("1.",a + "\n2.",b + "\n3.",c + "\n4.",d)
