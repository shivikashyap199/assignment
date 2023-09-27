day = int(input("enter the day"))
month = int(input("enter the month"))
year = int(input("enter the year"))
refDay = 1 
refYear = 2004
refMonth = 1
def check_leap_year(year):
    if year % 400==0 or (year%4==0 and year % 100!=0) :
        return True
    else:
        return False

def days_in_months(months):
    days = 0
    for x in range(1,months+1):
        if x == 1:
            days+=31
        elif x == 2:
            days+=28
        elif x == 3:
             days+=31
        elif x == 4:
            days+=30
        elif x == 5:
             days+=31
        elif x == 6:
            days+=30
        elif x == 7:
            days+=31
        elif x == 8:
            days+=31
        elif x == 9:
            days+=30
        elif x == 10:
            days+=31
        elif x == 11:
            days+=30

    return days

numDays = (year - refYear) * 365
for x in range(refYear, year+1):

    if(check_leap_year(x)):

        numDays+=1
numDays += days_in_months(month - refMonth)

numDays += day
remaining = numDays%7
if(remaining == 1):

    print('Sunday')

elif(remaining == 2):

    print('Monday')

elif(remaining == 3):

    print('Tuesday')

elif(remaining == 4):

    print('Wednesday')

elif(remaining == 5):

    print('Thursday')

elif(remaining == 6):

    print('Friday')

elif(remaining == 7):

    print('Saturday')

 

