"""
epoch: epoch is often used as a starting point to calculate the time intervals or the timestamps.

This reference or epoch value is platform dependent i.e different for the different OS.

This value can be positive if the time is after the epoch time or we can say that after ther starting time.
This value can be negative if the time is before the epoch time or we can say that before the start time.

-----------------
Important functions used in the time module are:
1. time()
2. ctime()
3. sleep()
4. gmtime() or localtime()
5. strftime() and strptime()
6. monotonic()
"""

# time() function
"""
--> Returns the current time since the epoch.
epoch = jan 1 1970, at 00:00:00

syntax:
--> time.time()
"""
import time
current_time=time.time()
print(int(current_time))
# We can use this function to calculate the code execution time by asking time at start and stop using this function and storing that time in varibale to calculate the difference of time or the code execution time.


# Sleep() function.
"""
--> suspends the execution of the current thread for the specified number of seconds.

syntax:
--> time.sleep(seconds)
"""
print("Hello !!")
time.sleep(5)
print("Bye Byee !!")

# ctime() function
"""
--> converts a timestamp(seconds since epoch) into human readable string representing the local time.

syntax:
time.ctime([seconds]) --- default argument is the timestamp
"""
print(time.ctime())
# It is taking the timestamp as the default argument and will provide the current time as of now from the epoch time
print(time.ctime(60))
# Here it is taking 60sec as the argument which will add into the epoch time and resulting time and string will get printed on the console.

# gmtime() and localtime()
"""
--> These functions convert the time stamps into the struct time object representing the utc time and the local time respectively.

synatx:
time.localtime() or time.gmtime()
"""
print(time.gmtime())
# output: time.struct_time(tm_year=2024, tm_mon=1, tm_mday=18, tm_hour=6, tm_min=26, tm_sec=6, tm_wday=3, tm_yday=18, tm_isdst=0)
print(time.localtime())
# output: time.struct_time(tm_year=2024, tm_mon=1, tm_mday=18, tm_hour=11, tm_min=56, tm_sec=6, tm_wday=3, tm_yday=18, tm_isdst=0)
print(time.localtime().tm_year) # to print the year
print(time.localtime().tm_mon)  # to print the month

# strftime() function
"""
-->  struct time object ---> formatted string
syntax:
strftime(format-codes,struct objects)

important formatted codes:
%Y represents the year with century as a decimal number.
%m represents the month as a zero-padded decimal number.
%d represents the day of the month as a zero-padded decimal number.
%H represents the hour (00 to 23).
%M represents the minute.
%b abbrevated month name.
%Z Timezone name.
"""
struct_object=time.localtime()
print(struct_object)
current_time=time.strftime("%d-%m-%Y")
print(f"current time is {current_time}")
print(time.strftime("%H-%M-%S"))
print(time.strftime("%d/%b/%Y %H:%M:%S - %Z"))

# strptime() function
"""
--> formatted string --> strcut time object 

syntax:
strptime(string,timeformat)
"""
struct_object=time.localtime()

string=time.strftime("%d/%b/%Y %H:%M:%S - %Z")
print(string)
print(time.strptime(string,"%d/%b/%Y %H:%M:%S - %Z"))

# monotonic() function--> It is better to use while calculating the program execution time.