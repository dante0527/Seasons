import os

# Clears screen
def clear():
    os.system('cls' if os.name == 'cls' else 'clear')


# Outputs which season the date is in
def szn(season):
    print(f"\n{month} {day}{suffix} is in {season}")


# Determines which season the date is in
def print_season():
    if month in spring:
        if (month == "March") and (day < 20):
            szn("Winter")
        elif (month == "June") and (day > 20):
            szn("Summer")
        else:
            szn("Spring")
    elif month in summer:
        if (month == "June") and (day < 21):
            szn("Spring")
        elif (month == "September") and (day > 21):
            szn("Autumn")
        else:
            szn("Summer")
    elif month in autumn:
        if (month == "September") and (day < 22):
            szn("Summer")
        elif (month == "December") and (day > 20):
            szn("Winter")
        else:
            szn("Autumn")
    elif month in winter:
        if (month == "December") and (day < 21):
            szn("Autumn")
        elif (month == "March") and (day > 19):
            szn("Spring")
        else:
            szn("Winter")


def valiDate():
    while True:
        if len(date) != 2:
            return False
        if type(date[0]) != str:
            return False
        if type(date[1]) != int:
            return False


# Months in each season
spring = ("March", "April", "May", "June")
summer = ("June", "July", "August", "September")
autumn = ("September", "October", "November", "December")
winter = ("December", "January", "February", "March")

# Number of days in each month
months = {"January": 31,
          "February": 28,
          "March": 31,
          "April": 30,
          "May": 31,
          "June": 30,
          "July": 31,
          "August": 31,
          "September": 30,
          "October": 31,
          "November": 30,
          "December": 31}

# Prompts user for date
date = input("Enter a date (ex. 'May 27'):\n>>").split()

while len(date) != 2:
    clear()
    date = input("Invalid date.\nEnter a date (ex. 'May 27')\n>>").split()

month = str(date[0].title())
day = int(date[1])

# Determines suffix for day numbers
if str(day) in ("11", "12", "13"):
    suffix = "th"
elif str(day)[-1] == "1":
    suffix = "st"
elif str(day)[-1] == "2":
    suffix = "nd"
elif str(day)[-1] == "3":
    suffix = "rd"
else:
    suffix = "th"

# Exception handling
if len(date) != 2:
    print("An error occurred")
else:
    if month not in months:
        print(f"\n\"{month}\" is not a valid month")
    if (day < 1) or (day > 31):
        print(f"\n{month} does not have a {day}{suffix} day")

# Runs tests and produces output
if (month in months) and (1 <= day < months[month]) and (len(date) == 2):
    print_season()
