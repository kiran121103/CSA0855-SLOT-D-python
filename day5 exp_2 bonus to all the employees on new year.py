grade = input("Enter the grade of the employee: ")
salary = float(input("Enter the employee salary: "))

if salary < 10000:
    bonus = 0.07 * salary
elif grade == 'A':
    bonus = 0.05 * salary
elif grade == 'B':
    bonus = 0.1 * salary
else:
    bonus = 0

totalsalary = salary + bonus
print("Salary: ",salary)
print("Bonus: ",bonus)
print("Total to be paid: ",totalsalary)
