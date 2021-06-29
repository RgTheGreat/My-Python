#this is edited from projects.raspberrypi.com
import pygal

#values that are going to be in pie chart
z = input("Name of first pie: ")
y = input("Name of second pie: ")
x = input("Name of third pie: ")
a = input("Name of fourth pie: ")
b = input("Name of fifth pie: ")
c = input("Name of sixth pie: ")




#render
piechart = pygal.Pie()
piechart.add(z, 5)
piechart.add(y, 5)
piechart.add(x, 5)
piechart.add(a, 5)
piechart.add(b, 5)
piechart.add(c, 5)
piechart.render()
