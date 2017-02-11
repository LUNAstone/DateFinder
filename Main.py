import datetime
import sys


def get_date():
    while True:
        date_year = int(input("Year? "))
        print("Please type a year between 1 and 9999.", end="\n\n")
        if date_year <= 1 or date_year >= 9999:
            break
        else:
            print("Please type a year between 1 and 9999.", end="\n\n")
    while True:
        date_month = int(input("Month? "))
        print("Please type a month between 1 and 12.", end="\n\n")
        if date_month <= 1 or date_month >= 12:
            break
        else:
            print("Please type a month between 1 and 12.", end="\n\n")
    while True:
        date_day = int(input("Day? "))
        print("Please type a day between 1 and 31.", end="\n\n")
        if date_day <= 1 or date_day >= 31:
            break
        else:
            print("Please type a day between 1 and 31.", end="\n\n")
    print(date_day, "/", date_month, "/", date_year, sep="")
    answer = input("Is this correct? (Y/N) ").lower()
    if answer == "y":
        print(" ")
        return date_day, date_month, date_year
    else:
        get_date()

if __name__ == "__main__":
    print("First date:")
    date1 = get_date()
    print("Second date:")
    date2 = get_date()
    if date1 == date2:
        raise ValueError("Dates are the same.")
