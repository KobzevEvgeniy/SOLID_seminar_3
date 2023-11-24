class Salary:
    def __init__(self, employee):
        self.base_salary = None
        self.employee = employee

    def calculate_net_salary(self, tax):

        return self.base_salary - self.base_salary * tax/100
