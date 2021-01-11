import random

print("Welcome to Employee Wage Computation Program")

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
employee_wage = 0
days = 1
total_wage = 0
while days <= 20:
    attendance = random.randint(0, 2)
    if attendance == 0:
        print("Absent")
        employee_wage = 0
    elif attendance == 1:
        print("Present")
        employee_wage = WAGE_PER_HOUR * FULL_DAY_HOUR
    elif attendance == 2:
        print("Part Time")
        employee_wage = WAGE_PER_HOUR * PART_TIME_HOUR
    print("Employee Wage for day {} is equal to {}".format(days, employee_wage))
    days += 1
    total_wage += employee_wage
print("Total Wage of the employee {}".format(total_wage))

