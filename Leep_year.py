def is_leap(year):
    # year=int(input("enter the year:"))
    if year%400==0 or year%4==0 and year%100!=0:
        leap = True
    else:
        leap = False
    return leap


year = int(input())
print(is_leap(year))