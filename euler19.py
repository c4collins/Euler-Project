monthStartDays = []
sundays = []
finalDays = []

def numOfDays(startYear, endYear):
    monthStartDays.append(1)
    
    for year in range(startYear, endYear+1 ):
        for month in range(12):
            addDays = 0
            
            if month == 0:
                addDays = 31
            if month == 1:
                addDays = 29 if isLeapYear(year) else 28
            if month == 2:
                addDays = 31
            if month == 3:
                addDays = 30
            if month == 4:
                addDays = 31
            if month == 5:
                addDays = 30
            if month == 6:
                addDays = 31
            if month == 7:
                addDays = 31
            if month == 8:
                addDays = 30
            if month == 9:
                addDays = 31
            if month == 10:
                addDays = 30
            if month == 11:
                addDays = 31
            elif month >= 12 or month < 0:
                print "error, month is ", month
            monthStartDays.append(monthStartDays[-1] + addDays)
            print "Adding Month %d, %d" % (month, year)
            
def numOfSundays(startYear, endYear):
    for day in range(1,int((endYear-startYear) * (366*.25 + 365*.75))):
        if day % 7 == 0:
            for possibleMatch in monthStartDays:
                if possibleMatch == day:
                    finalDays.append(day)
                    print "Match! ", day
            sundays.append(day)
    
def isLeapYear(year):
    leapYear = True if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)) else False
    return leapYear
 
startYear = 1901
endYear = 2000
numOfDays(startYear, endYear)
numOfSundays(startYear, endYear)

# finalDays = set(monthStartDays).intersection(sundays)
print "There are %d months that start with a Sunday between %d and %d" % (len(finalDays), startYear, endYear)

