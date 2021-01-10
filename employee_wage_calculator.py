import random

print("Welcome to Employee Wage Computation Program")
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
attendance = random.randint(0, 1)
if attendance == 0:
    print("Absent")
elif attendance == 1:
    print("Present")
employee_wage = attendance * WAGE_PER_HOUR * FULL_DAY_HOUR
print("Employee Wage  is equal to {}".format(employee_wage))
