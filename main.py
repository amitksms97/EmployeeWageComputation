from employee_wage_calculator import EmployeeWageComputation

company_list = []

if __name__ == '__main__':
    tata = EmployeeWageComputation("Tata", 20, 8, 4, 100, 20)
    tata.calculate_employee_wage()
    company_list.append(tata.__str__())

    reliance = EmployeeWageComputation("Reliance", 30, 10, 5, 150, 25)
    reliance.calculate_employee_wage()
    company_list.append(reliance.__str__())

    print(company_list)
