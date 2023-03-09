year = int(input("Enter a year: "))
if (year % 4 == 0):
    print(year, "is a leap year")
    for i in range(year+1, year+4):
        if (i % 4 == 0):
            print("Next leap year:", i)
            break
else:
    print(year, "is not a leap year")
    for i in range(year-1, year-4, -1):
        if (i % 4 == 0 ):
            print("Previous leap year:", i)
            break
