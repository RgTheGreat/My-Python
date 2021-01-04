# dates
import datetime

a = datetime.datetime.now()
# year:
print(a.year)
# only a:
print(a)
# what you see on your pc:
print(a.strftime("%D"))
# or:
print(a.strftime("%A  %Y"))
