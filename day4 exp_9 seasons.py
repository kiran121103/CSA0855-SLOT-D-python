month=input("input the month:")
day=int(input("input the day:"))

if month in ('january'or'jan','february'or'feb','march'or'mar'):
    season='winter'
elif month in ('april'or'apr','may','june'or'jun'):
    season='summer'
elif month in ('july'or'jul','august'or'aug','september'or'sep'):
    season='spring'
else:
    season='fall'

if (month=='march'or'mar')and (day>=20):
    season='summer'
elif (month=='june'or'jun')and (day>=21):
    season='spring'
elif (month=='september'or'sep')and(day>=22):
    season='fall'
elif (month=='december'or'dec')and(day>=21):
    season='winter'

print("season is",season)
