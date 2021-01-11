from employee_wage_calculator import EmployeeWageComputation

if __name__ == '__main__':
    tata = EmployeeWageComputation("Tata", 20, 8, 4)
    tata.calculate_employee_wage()
    print(tata)
    reliance = EmployeeWageComputation("Reliance", 30, 10, 5)
    reliance.calculate_employee_wage()
    print(reliance)
