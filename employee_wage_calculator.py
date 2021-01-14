import random
from employee_wage_interface import EmployeeWageInterface


class EmployeeWageComputation:

    print("Welcome to Employee Wage Computation Program")

    def __init__(self, company_name, wage_per_hour, full_day_hour, part_time_hour, max_work_hours, max_working_days):
        self.COMPANY_NAME = company_name
        self.WAGE_PER_HOUR = wage_per_hour
        self.FULL_DAY_HOUR = full_day_hour
        self.PART_TIME_HOUR = part_time_hour
        self.MAX_WORK_HOURS = max_work_hours
        self.MAX_WORKING_DAYS = max_working_days
        self.total_wage = 0

    @staticmethod
    def generate_random_attendance():
        return random.randint(0, 2)

    def check_employee_attendance(self):
        attendance = self.generate_random_attendance()
        switcher = {
            0: 0,
            1: self.FULL_DAY_HOUR,
            2: self.PART_TIME_HOUR
        }
        return switcher.get(attendance)

    def calculate_employee_wage(self):
        days = 1
        employee_wage = 0
        total_hours = 0
        while days <= self.MAX_WORKING_DAYS and total_hours <= self.MAX_WORK_HOURS:
            hours = self.check_employee_attendance()
            employee_wage = self.WAGE_PER_HOUR * hours
            print("Employee Wage for day {} is equal to {}".format(days, employee_wage))
            self.total_wage += employee_wage
            days += 1
            total_hours += hours
        print("Total Wage of the employee {} from the company {} and he worked for total {} hours".format(self.total_wage, self.COMPANY_NAME, total_hours))

    def __str__(self):
        return f"{self.COMPANY_NAME, self.total_wage}"
