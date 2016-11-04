# This is a simple Python program that takes in a user's date of
# birth as an input and calculates how long the user has lived on
# earth either in Seconds, Minutes, Hours, Days, Weeks, Months or Years.

# Import Python Time packages
import time
from datetime import tzinfo, timedelta, datetime

# This function calculates the users age in seconds
def age_in_secs():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff = (current_date - date_of_birth).total_seconds()
    print("You have lived for {} seconds.".format(diff))

# This function calculates the users age in minutes
def age_in_mins():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_sec = (current_date - date_of_birth).total_seconds()
    diff_min = round((diff_sec / 60), 3)
    print("You have lived for {} minutes.".format(diff_min))

# This function calculates the users age in hours
def age_in_hrs():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_sec = (current_date - date_of_birth).total_seconds()
    diff_hrs = round((diff_sec / 60 / 60), 3)
    print("You have lived for {} hours.".format(diff_hrs))

# This function calculates the users age in days
def age_in_days():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_sec = (current_date - date_of_birth).total_seconds()
    diff_days = round((diff_sec / 60 / 60 / 24), 3)
    print("You have lived for {} days.".format(diff_days))

# This function calculates the users age in weeks
def age_in_weeks():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_sec = (current_date - date_of_birth).total_seconds()
    diff_weeks = round((diff_sec / 60 / 60 / 24 / 7), 3)
    print("You have lived for {} weeks.".format(diff_weeks))

# This function calculates the users age in months
def age_in_months():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_sec = (current_date - date_of_birth).total_seconds()
    diff_months = round(( diff_sec / 60 / 60 / 24 / 30.43), 3)
    print("You have lived for {} months.".format(diff_months))

# This function calculates the users age in years
def age_in_years():
    user_input = raw_input("Enter a date in YYYY-MM-DD format: ")
    date_of_birth = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    diff_secs = (current_date - date_of_birth).total_seconds()
    diff_years = round((diff_secs / 60 / 60 / 24 / 365.25), 3)
    print("You have lived for {} years.".format(diff_years))

# Menu function
def menu():
    print ("Welcome to Python Age Calculator.")
    print ("Select an option to begin: ")
    print ("Input 1 to for age in seconds, 2 for age in minutes, 3 for age in hours, 4 for age in days, 5 for age in weeks , 6 for age in months or 7 for age in years ")
    option = int(input("Enter your option here: "))
    # Conditional operations based on the user selected option
    if option == 1:
        age_in_secs()
    elif option == 2:
        age_in_mins()
    elif option == 3:
        age_in_hrs()
    elif option == 4:
        age_in_days()
    elif option == 5:
        age_in_weeks()
    elif option == 6:
        age_in_months()
    elif option == 7:
        age_in_years()
    else:
        print("You option is invalid...")
        menu()

# Calls up the menu function when the program runs
menu()