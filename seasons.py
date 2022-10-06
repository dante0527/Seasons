import os

# Clears screen
def clear():
    os.system('cls' if os.name == 'cls' else 'clear')


# Outputs which season the date is in
def print_szn(season):
    print(f"\n{month} {day}{suffix(day)} is in {season}")


# Determines which season the date is in
def calc_season():
    if month in spring:
        if (month == "March") and (day < 20):
            print_szn("Winter")
        elif (month == "June") and (day > 20):
            print_szn("Summer")
        else:
            print_szn("Spring")
    elif month in summer:
        if (month == "June") and (day < 21):
            print_szn("Spring")
        elif (month == "September") and (day > 21):
            print_szn("Autumn")
        else:
            print_szn("Summer")
    elif month in autumn:
        if (month == "September") and (day < 22):
            print_szn("Summer")
        elif (month == "December") and (day > 20):
            print_szn("Winter")
        else:
            print_szn("Autumn")
    elif month in winter:
        if (month == "December") and (day < 21):
            print_szn("Autumn")
        elif (month == "March") and (day > 19):
            print_szn("Spring")
        else:
            print_szn("Winter")


# Determines suffix for day numbers
def suffix(day):
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

    return suffix


# Input validation for date (MMMM/DD)
def valiDate(date):

    # Check length of input
    if len(date) != 2:
        return False

    # Check day type
    try:
        # Parse date
        month = date[0].title()
        day = int(date[1])
    except:
        return False

    # Check for month and list
    if month not in months:
        return False

    # Check for day in range
    if int(day) < 1 or int(day > months[month]):
        return False

    # All checks passed
    else:
        return True


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
clear()
date = input("Enter a date (ex. 'May 27'):\n> ").split()

# Input validation for date
while valiDate(date) == False:
    clear()
    date = input("Invalid date.\nEnter a date (ex. 'May 27'):\n> ").split()

# Parse date
month = date[0].title()
day = int(date[1])

# Determine which season the date is in
calc_season()
