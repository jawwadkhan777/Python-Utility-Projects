def is_leap(year):
    leap = False
    if year%400==0:
        leap = True
    elif year%4==0 and year%100!=0:
        leap = True
 
    
    return leap

year = int(input("Enter the year: "))
#is_leap(year)
if is_leap(year) == True:
    print(year,"is a leap year")
elif is_leap(year) == False:
    print(year,"is not a leap year")