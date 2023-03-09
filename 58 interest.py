principal = float(input("Enter the principal amount: "))
years = int(input("Enter the no of years: "))
senior_citizen = input("Is customer senior citizen (y/n): ")
if senior_citizen == 'y':
    rate_of_interest = 0.12
else:
    rate_of_interest = 0.10
interest = rate_of_interest*years*principal
print("Interest: ", int(interest))
