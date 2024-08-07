year= input("enter year you were born (eg. 1991)")
month= input("enter the month you were born")
day= input("enter your birth day")

x=2024-int(year)
from datetime import date
print(date.now())

print("you are" ,x, "years old!!")