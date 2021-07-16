# Given your birthday and the current date, calculate your age in days. 
# To put simply, if you're born on Jan 1, 2021 and today is Jan 2, 2021, then you're 1 day old

def isLeapYear(year):
    """Checks if a year is Leap year or not"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    """Returns number of days in a month"""
    if month in(1,3,5,7,8,10,12):
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30
    return 30

def nextDay(year, month, day):
    """Returns next day of a date"""
    if day < daysInMonth(year, month):
        return year, month, day+1
    else:
        if month == 12:
            return year+1, 1, 1
        else:
            return year, month+1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    
    # Add an if statement if the inputs are not valid!
    if dateIsBefore(year2, month2, day2, year1, month1, day1):
        return("Dates are in wrong order")
        
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

        
def tests():
    assert daysInMonth(2012,2) == 29
    assert daysInMonth(2012,3) == 31
    assert daysInMonth(2012,6) == 30
    assert nextDay(2012,3,31) == (2012,4,1)
    assert nextDay(2013,2,28) == (2013,3,1)
    print(daysBetweenDates(2014,1,2,2015,1,1))
    
tests()
