denominations = [2000, 500, 200, 100]
values = {}
for i in range(len(denominations)):
    denomination = int(input(f"Enter the {i+1} Denomination: "))
    notes = int(input(f"Enter the {i+1} Denomination number of notes: "))
    values[denomination] = notes
total_balance = 0
for denomination in denominations:
    if denomination in values:
        total_balance += denomination * values[denomination]
print("Total Available Balance in ATM:",total_balance)
