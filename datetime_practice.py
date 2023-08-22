import datetime
from time import localtime 

# Get Current Date and Time
now = datetime.datetime.now()
print(now)

#  Get Current Date
current_date = datetime.date.today()

print(current_date)

#Attributes of datetime Module
print(dir(datetime))

# datetime.datetime - represents a single point in time, including a date and a time.
# datetime.date - represents a date (year, month, and day) without a time.
# datetime.time - represents a time (hour, minute, second, and microsecond) without a date.
# datetime.timedelta - represents a duration, which can be used to perform arithmetic with datetime objects.

# Date object to represent a date
date = datetime.date(2022,3,1)
print(date)  #2022-03-01


# Print today's year, month and day
today = datetime.date.today()
print('Current year:', today.year)
print('Current Date:', today.day)
print('Current_month:', today.month)

# Time object to represent time

#time(hour=0, minute=0, second =0)
a=datetime.time()
print(a)

#time(hour, minute, second)
b = datetime.time(5,11,45)
print(b)

#time(hour, minute, second, microsecond)
d=datetime.time(11,34, 56, 23456)
print(d)


# Print hour, minute, second and microsecond
#1
today = datetime.datetime.today()
print(today)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)

#2
a = datetime.time(11,34, 56)
print(a.hour, a.minute, a.second, a.microsecond)

# Python datetime object
#datetime.datetime(year.month, date)
a=datetime.datetime(2022,12,8)
print(a)

#datetime(year,month, date, hour, minute, second, microsecond)
b = datetime.datetime(2022,12,8, 5, 44, 43, 34230)
print(b)
print(b.year, b.month, b.day, b.hour, b.minute, b.second, b.microsecond)

#Python datetime.timedelta class 
from datetime import datetime, date, timedelta, tzinfo

#using date()
t1=date(2023,12,22)
t2=date(2023,1,10)

t3 = t1- t2

print("t3 =", t3)

#using datetime()
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("Type of t3 =", type(t3)) 
print("Type of t6 =", type(t6))  

# 12: Difference between two timedelta objects

from datetime import datetime 
t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)

t3 = t1-t2
print(t3)

# Python has strftime() and strptime() methods
# The method strftime() creates a formatted string from a given date, datetime or time object.
# The strptime() method creates a datetime object from a given string

now = datetime.now()
t= now.strftime('%H:%M:%S')
print('Time', t)

s1= now.strftime('%m/%d/%Y %H:%M:%S')
print(s1)

s2 = now.strftime('%d/%m/%y %H:%M:%S')
print(s2)

date_string = '25 December, 2023'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)


# Handling timezone in Python
import pytz

localtime = datetime.now()
print('Local time', localtime.strftime('%m/%d/%Y %H:%M:%S'))

tz_NY = pytz.timezone('America/New_York')
datetime_ny = datetime.now(tz_NY)
print(datetime_ny)

tz_London = pytz.timezone('Europe/London')
date_London = datetime.now(tz_London)
print(date_London)

