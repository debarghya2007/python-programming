class Employee:
    def __init__(self, emp_id: str, emp_name: str, salary: float):
        self._emp_id = emp_id          # Encapsulated (private prefix)
        self._emp_name = emp_name
        self._salary = salary

    def get_salary(self) -> float:
        return self._salary


class ManagerEmployee(Employee):
    def __init__(self, emp_id: str, emp_name: str, salary: float, team_bonus: float):
        super().__init__(emp_id, emp_name, salary)
        self._team_bonus = team_bonus  # Private double teamBonus

    def effective_salary(self) -> float:
        """Returns get_salary() + team_bonus"""
        return self.get_salary() + self._team_bonus


class InternEmployee(Employee):
    def __init__(self, emp_id: str, emp_name: str, salary: float, stipend_cap: float):
        super().__init__(emp_id, emp_name, salary)
        self._stipend_cap = stipend_cap  # Private double stipendCap

    def effective_salary(self) -> float:
        """Returns whichever is smaller: get_salary() or stipend_cap"""
        return min(self.get_salary(), self._stipend_cap)


if __name__ == "__main__":
    # Create one of each of the three employee types based on sample input
    plain_emp = Employee("EMP101", "Plain Employee", 40000.0)
    manager_emp = ManagerEmployee("EMP102", "Manager Employee", 70000.0, 8000.0)
    intern_emp = InternEmployee("EMP103", "Intern Employee", 12000.0, 10000.0)

    employees = [plain_emp, manager_emp, intern_emp]

    # Process each employee using isinstance() to decide which extra behaviour to invoke
    for emp in employees:
        if isinstance(emp, ManagerEmployee):
            print(f"Manager effective pay: Rs {emp.effective_salary()}")
        elif isinstance(emp, InternEmployee):
            print(f"Intern effective pay: Rs {emp.effective_salary()}")
        elif isinstance(emp, Employee):
            print(f"Plain employee pay: Rs {emp.get_salary()}")
