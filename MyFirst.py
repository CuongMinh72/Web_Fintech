""" 
*** To get python version
import sys
print("Python version")
print(sys.version)
print("Version info")6
print(sys.version_info)

*** To get date and time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


*** Radius of the circle
from math import pi
r = float(input ("input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + "is: " + str(pi * r**2))


*** To get the name
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello " + lname + " " + fname)


*** To print out tuple and list 
Values = input("Input the numbers: ")
list = Values.split(",")
tuple = tuple(list)
print('list : ',list)
print('tuple : ',tuple)


*** To split the type of file from the file name
filename = input("Input the file name: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


*** To get info out of a list
color_list = ["Red","Grenn","White","Black"]
print("%s %s"%(color_list[0],color_list[-1]))

*** To get the exam date
exam_st_date = (11, 12, 2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


*** multiply a number 
a = int(input("input the number: "))
n1 = int( "%s" %a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print(n1 + n2 + n3)


*** return the doc of a function
print(abs.__doc__)


*** To get the date in a month
import calendar
y = int(input("input the year : "))
m = int(input ("input the month : "))
print(calendar.month(y, m))


*** To calculate the dates
from datetime import date
first_date = date(2014, 7, 2)
second_date = date(2014, 7, 11)
delta = second_date - first_date 
print(delta.days)


*** To calculate volume of the sphere
from math import pi
radius = 6
vol_of_sphere = 4/3 * pi * radius**3
print (vol_of_sphere) 


*** To find the difference between 2 number
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))


*** The sum of 3 
def sum_thrice(x, y, z):
  sum = x + y + z
  if x == y == z:
    sum = sum * 3
  return sum 

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


*** Add is to a string 
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))


*** Print out copy of the given string
def larger_string(str, n):
  result = ""
  for i in range(n):
    result = result + str
  return result

print(larger_string('abd', 2))
print(larger_string(' py', 3))  


n = int(input("input the number: "))
mod = n % 2
if mod > 0:
  print ("This is an odd number")
else:
  print ("This is an even number")


def list_count_4(nums):
  count = 0 
  for num in nums:
      if num == 4:
        count += 1
  return count
print(list_count_4([1, 4 ,6 ,7 ,4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
"""


