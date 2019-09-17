def isYearLeap(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False

def daysInMonth(year, month):
    if month < 1 or month > 12:
        return 0
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    if isYearLeap(year):
        days = [31,29,31,30,31,30,31,31, 30, 31, 30, 31]
    else:
        days = [31,28,31,30,31,30,31,31, 30, 31, 30, 31]
    
    for i in range(len(months)):
        if month == months[i]:
            return days[i]


def dayOfYear(year, month, day):
    #day of the year
    # validate date
    if day > daysInMonth(year, month):
        return None
    # number of days before
    days = 0
    for mo in range(month):
        days += daysInMonth(year, mo)
    return days + day


print("2000-12-31 ", dayOfYear(2000, 12, 31))
print("1900-2-29 ", dayOfYear(1900, 2, 29))
        
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
