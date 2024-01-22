# The date class in the datetime class is used to represent a date(Year, Month, Day) without any time information.
import datetime

date_obj= datetime.date.today()
print(date_obj,type(date_obj))
print(f"Year is : {date_obj.year}")
print(f"Month is : {date_obj.month}")
print(f"Day is : {date_obj.day}")
string_obj=date_obj.strftime("%Y-%m-%d")
print(string_obj,type(string_obj))

