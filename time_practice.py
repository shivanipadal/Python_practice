from collections import namedtuple
import time
from unittest import result 

# https://www.programiz.com/python-programming/time
#get the current time in seconds since the epoch
seconds = time.time()

print("seconds since epoch", seconds)

local_time = time.ctime(seconds)

print("Local time", local_time)

#sleep function 
# print("imeediately")
# time.sleep(2.4)
# print('printed after 2.4 seconds')

#time.localtime() 
result = time.localtime(seconds)
print("result", result)
print('Year', result.tm_year)
print('Hour', result.tm_hour)

#time.mktime() it takes struct_time(a tuple containing 9 elements)
time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
seconds = time.mktime(time_tuple)
print(seconds) #time in seconds since the epoch

# time.asctime()  converts the time tuple of struct_time( a tuple containing 9 elements) to a human-readable string
time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
result = time.asctime(time_tuple)
print('Result :', result)   #Fri Dec 28 08:44:04 2022

#  time.strftime() 
named_tuple = time.localtime()  #get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

#strptime() function parses a string representing time and returns struct_time

time_string = "14 July, 2023"
result = time.strptime(time_string, "%d %B, %Y")
print(result)