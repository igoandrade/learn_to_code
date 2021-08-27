"""
A formula for computing Easter in the years 1982-2048, inclusive, is as
follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30,
e = (2b + 4c + 6d + 5)%7. The date of Easter is March 22 + d + e (which
could be in April). Write a program that inputs a year, verifies that it is in
the proper range, and then prints out the date of Easter that year.
"""

from datetime import datetime

def easter_date(year):
    if (year >= 1982 and year <= 2048):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        easter_day = 22 + d + e
        if easter_day < 32:
            month = 'March'
        else:
            month = 'April'
            easter_day -= 31
        str_easter_dt = f"{month:s} {easter_day:0>2} {year}"
        return str_easter_dt

    else:
        print("Year must be between 1982 and 2048 (inclusive).")
        return None

def easter_date2(year):
    if (year >= 1900 and year <= 2099):
        D = 225 - 11* (year % 19)
        while D > 50:
            D -= 30
        if D > 48:
            D -= 1
        E = (year + year//4 + D + 1) % 7
        Q = D + 7 - E
        if Q < 32:
            m = "March"
        else:
            m = "April"
            Q -= 31
        str_easter_dt = f"{m:s} {Q:0>2} {year}"
        return str_easter_dt
    else:
        print("Year must be between 1900 and 2099 (inclusive).")
        return None


for i in range(2095, 2100):
    print(easter_date(i))
    print("------------")
    print(easter_date2(i))
    print("\n============\n")