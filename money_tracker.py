#Creating a time related money tracker. Importing the datetime function.

import datetime
import csv

# Nana is our client who seeks to calculate the wages per hour.


while True:
    try:
        text = int(input("Hello Nana, enter password to log in:  "))
    except ValueError:
        print("Enter correct password to log in.  ")
        continue
    else:
        break
if text != 1234:
     print("You did not enter correct password.")

else:

    print("Your login time and date is\n")
    x  = datetime.datetime.now()
    print(x)

# Generating the input function for Nana to insert time in and time out.

print("\n")
login = int(input('enter start time in hours: '))
login2 =int(input('enter start time in minutes: '))


# The start time for Nana's task

start_time = datetime.time(login,login2)
print(start_time)
print("\n")
logout = int(input('enter end time in hours: '))
logout2 =int(input('enter end time in minutes: '))


# The stop time for Nana's task

stop_time = datetime.time(logout,logout2)
print(stop_time)
print("\n")
date = datetime.date(1, 1, 1)
time1 = datetime.datetime.combine(date, start_time)
time2 = datetime.datetime.combine(date, stop_time)



time_elapsed = time2 - time1



# Calculating time spent and money earning per hour and overtime.

time_spent = time_elapsed.total_seconds()/3600

print("Your time spent working is: ")
print(round(time_spent,2))
wages = time_spent * 5
print("\n")
print("Your total wages is: ")
print("$" + str(round(wages, 2) ))

# Creating csv file archieve.



r = open("Nana's_Money_Tracker.csv", "a" )


writer = csv.writer(r)
writer.writerow(["Hours_worked", "Wages"])

r.close()
