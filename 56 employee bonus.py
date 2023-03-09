employee_grade = input("Enter the grade of the employee: ")
employee_salary = float(input("Enter the employee salary: "))

if employee_salary < 10000:
    bonus_percent = 12
else:
    if employee_grade == 'A':
        bonus_percent = 5
    elif employee_grade == 'B':
        bonus_percent = 10
    else:
        print("Invalid grade entered.")
        exit()

bonus_amount = employee_salary * bonus_percent / 100
total_amount = employee_salary + bonus_amount

print("Salary =", employee_salary)
print("Bonus =", bonus_amount)
print("Total to be paid:", total_amount)
