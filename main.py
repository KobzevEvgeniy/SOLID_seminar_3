from OCP.Bus import Bus
from OCP.Car import Car
from SRP.Employee import Employee
from SRP.Salary import Salary


if __name__ == '__main__':
    # Задание №1 Переписать код в соответствии с Single Responsibility Principle:
    worker = Employee("Кобзев Евгений", "02/12/1984", 150000)
    print(worker.get_emp_info())
    print(Salary.calculate_net_salary(worker, 13))

    # Задание №2 Переписать код SpeedCalculation в соответствии с Open-Closed Principle:
    bus1 = Bus(50, "Нефаз")
    print(f"Тип-{bus1.get_type()},скорость-{bus1.get_speed()}")
    print(bus1.get_max_speed())

    car1 = Car(100, "BMW")
    print(f"Тип-{car1.get_type()},скорость-{car1.get_speed()}")
    print(car1.get_max_speed())

