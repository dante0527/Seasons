month = input("Enter a month:\n")
day = int(input("Enter a day:\n"))

spring = ("March", "April", "May", "June")
summer = ("June", "July", "August", "September")
autumn = ("September", "October", "November", "December")
winter = ("December", "January", "February", "March")

months = {"January" : 31,
    "February": 28,
    "March": 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October": 31,
    "November" : 30,
    "December": 31}
    
def szn(season):
  print(f"{month} {day} is in {season}")

if month in months:
    if 1 <= day < months[month]:
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
        else:
            print("Invalid")
    else:
        print(f"{month} does not have a {day}{suffix} day.")
else:
    print(f"{month} is not a valid month.")
