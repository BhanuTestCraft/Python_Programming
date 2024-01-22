# import the datetime module.
import datetime

# There is datetime class in the datetime module so we will create the object of the class.
datetime_obj=datetime.datetime(2024,1,18,7,52,0) #Year Month Day Hour Minute Second
print(datetime_obj,type(datetime_obj))

# create the datetime object using the current date and time.

datetime_obj=datetime.datetime.now()
# Here we have not created the class object but we have accessed the now function.
print(datetime_obj)
print(f" Year is {datetime_obj.year}")
print(f" Month is {datetime_obj.month}")
print(f" Day is {datetime_obj.day}")

# Let us consider we need to conver the date time object into the string.
string_datetime=datetime_obj.strftime("%Y-%m-%d, %H:%M:%S")
print(string_datetime,type(string_datetime))

# How to get the current date or time only.
# Method 1: 
datetime_obj = datetime.datetime.now()
print(datetime_obj,type(datetime_obj))
datetime_str=datetime_obj.strftime("%d-%m-%Y %H:%M:%S")
print(datetime_str,type(datetime_str))
current_date=datetime_str.split()[0]
print(current_date)
current_time=datetime_str.split()[-1]
print(current_time)

# Method 2:
datetime_obj=datetime.datetime.now()
current_date=datetime_obj.date()
current_time=datetime_obj.time()
print(current_date)
print(current_time)