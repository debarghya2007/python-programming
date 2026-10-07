class Employee:
    def __init__(self, emp_id: str, emp_name: str, salary: float):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._salary = salary

    def get_salary(self) -> float:
        return self._salary


class ManagerEmployee(Employee):
    def __init__(self, emp_id: str, emp_name: str, salary: float, team_bonus: float):
        super().__init__(emp_id, emp_name, salary)
        self._team_bonus = team_bonus

    def effective_salary(self) -> float:
        return self.get_salary() + self._team_bonus


class InternEmployee(Employee):
    def __init__(self, emp_id: str, emp_name: str, salary: float, stipend_cap: float):
        super().__init__(emp_id, emp_name, salary)
        self._stipend_cap = stipend_cap

    def effective_salary(self) -> float:
        return min(self.get_salary(), self._stipend_cap)


class ParkingSlot:
    def __init__(self, slot_no: str, capacity: int, occupied_count: int = 0):
        self.slot_no = slot_no
        self.capacity = capacity
        self.occupied_count = occupied_count

    def allot(self) -> bool:
        if self.occupied_count < self.capacity:
            self.occupied_count += 1
            return True
        return False

    @staticmethod
    def find_available_slot(slots: list['ParkingSlot']) -> 'ParkingSlot | None':
        for slot in slots:
            if slot.occupied_count < slot.capacity:
                return slot
        return None

    @staticmethod
    def safe_allot(slots: list['ParkingSlot']) -> 'ParkingSlot | None':
        """Null-safe parking slot allotment process"""
        slot = ParkingSlot.find_available_slot(slots)
        if slot is not None:
            slot.allot()
            return slot
        return None


class CompanyEmployeeRecord:
    total_records = 0  # Static/class counter

    def __init__(self, name: str, emp_id: str, employee: Employee, slot: ParkingSlot | None = None):
        self.name = name
        self.emp_id = emp_id
        self.employee = employee  # Object reference as field
        self.slot = slot          # Object reference as field (or None)
        CompanyEmployeeRecord.total_records += 1

    def full_profile(self) -> str:
        # Determine pay dynamically based on employee type
        if hasattr(self.employee, 'effective_salary'):
            pay = self.employee.effective_salary()
        else:
            pay = self.employee.get_salary()

        slot_str = self.slot.slot_no if self.slot is not None else "no parking assigned"
        return f"{self.name} | Pay: Rs {pay} | Slot: {slot_str}"


if __name__ == "__main__":
    # Setup available parking slots (Only 2 slots available)[cite: 10]
    parking_slots = [
        ParkingSlot("A1", 1, 0),
        ParkingSlot("A2", 1, 0)
    ]

    # Employee 1: Manager with bonus + Allotted Parking A1[cite: 10]
    divya_emp = ManagerEmployee("EMP001", "Divya", 70000.0, 8000.0)
    divya_slot = ParkingSlot.safe_allot(parking_slots)
    rec1 = CompanyEmployeeRecord("Divya", "EMP001", divya_emp, divya_slot)

    # Employee 2: Plain Employee + Allotted Parking A2[cite: 10]
    karan_emp = Employee("EMP002", "Karan", 40000.0)
    karan_slot = ParkingSlot.safe_allot(parking_slots)
    rec2 = CompanyEmployeeRecord("Karan", "EMP002", karan_emp, karan_slot)

    # Employee 3: Intern with cap + Parking unallotted (no slots left)[cite: 10]
    meera_emp = InternEmployee("EMP003", "Meera", 12000.0, 10000.0)
    meera_slot = ParkingSlot.safe_allot(parking_slots)  # Returns None as all slots are full
    rec3 = CompanyEmployeeRecord("Meera", "EMP003", meera_emp, meera_slot)

    # Print employee profiles and total records count[cite: 10]
    print(rec1.full_profile())
    print(rec2.full_profile())
    print(rec3.full_profile())
    print(f"Total records: {CompanyEmployeeRecord.total_records}")
