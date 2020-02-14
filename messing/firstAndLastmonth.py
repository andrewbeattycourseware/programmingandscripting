from datetime import date
import calendar
delimiter = "."

today = date.today()
datesRange = calendar.monthrange(today.year,today.month)
print ("last day of this month is {}".format(datesRange[1]))

# I could create a date with the range[1]
# d1 = today.strftime("%d.%m.%Y")
# print("d1 =", d1)
# but we just want the string

fromDateString = "1" + delimiter + str(today.month) + delimiter + str(today.year)
toDateString   = str(datesRange[1]) + delimiter + str(today.month) + delimiter + str(today.year) 

print ("dates from {} to {} ".format(fromDateString,toDateString))