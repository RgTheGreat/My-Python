import pygal

z = input("Name of first pie: ")
y = input("Name of second pie: ")
x = input("Name of third pie: ")
a = input("Name of fourth pie: ")
b = input("Name of fifth pie: ")
c = input("Name of sixth pie: ")


z1 = input("Value of first pie: ")
y1 = input("Value of second pie: ")
x1 = input("Value of third pie: ")
a1 = input("Value of fourth pie: ")
b1 = input("Value of fifth pie: ")
c1 = input("Value of sixth pie: ")


piechart = pygal.Pie()
piechart.add(z, int(z1))
piechart.add(y, int(y1))
piechart.add(x, int(x1))
piechart.add(a, int(a1))
piechart.add(b, int(b1))
piechart.add(c, int(c1))
piechart.render()
