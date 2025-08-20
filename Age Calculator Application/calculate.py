# -*- coding: utf-8 -*-
import time
from calendar import isleap

def judge_leap_year(year):
    """Check if a year is a leap year."""
    return isleap(year)

def month_days(month, leap_year):
    """Returns the number of days in a given month."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28
    return 0  # For invalid months

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    try:
        age_years = int(age)
        if age_years < 0:
            print("Age cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number for age.")
        return
    
    localtime = time.localtime(time.time())
    current_year = localtime.tm_year
    birth_year = current_year - age_years
    
    # Calculate total months
    total_months = age_years * 12 + localtime.tm_mon
    
    # Calculate total days
    total_days = 0
    
    # Add days for each year from birth year to current year - 1
    for year in range(birth_year, current_year):
        total_days += 366 if judge_leap_year(year) else 365
    
    # Add days for the current year
    current_leap = judge_leap_year(current_year)
    for month in range(1, localtime.tm_mon):
        total_days += month_days(month, current_leap)
    
    total_days += localtime.tm_mday
    
    print(f"{name}'s age is {age_years} years or {total_months} months or {total_days} days")

if __name__ == "__main__":
    main()
