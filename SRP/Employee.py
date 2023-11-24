class Employee:

    def __init__(self, name, dob, base_salary) -> None:
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"Имя - {self.name} , Дата рождения - {self.dob}, Базовая ставка-{self.base_salary}"
