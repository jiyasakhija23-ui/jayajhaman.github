# print ("HELLO world")
# print("*" * 10)

#boolen values
from argparse import Namespace


students_count = 1000
rating = 4.99
is_published = True
course_name = "python programming"
print(students_count)

#Ternary operators
age = 12
if age >= 18:
    Message ="Eligible"
else:
    message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

#logical operators
high_income = True
good_credit = True
student = False

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

#chaining comparison operators
# age should be between 18 and 65
age = 22
if age >= age < 65:
    print("Eligible")

#for loops
for number in range(1, 10, 4):
    print("Attemp", number , number * ".")

successful = True 
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed") 
  
#nested loops

 