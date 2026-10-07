class SrmStudent:
    def __init__(self, name: str, reg_no: str, attendance: int):
        self.name = name
        self.reg_no = reg_no
        self.attendance = attendance

    # Instance method to update attendance after a re-check
    def add_attendance_update(self, new_attendance: int) -> None:
        self.attendance = new_attendance

    # Instance method checking eligibility (75% or above)
    def is_eligible(self) -> bool:
        return self.attendance >= 75

    # Static utility method to compute average attendance across a list of students
    @staticmethod
    def class_average(students: list['SrmStudent']) -> float:
        if not students:
            return 0.0
        
        total_attendance = sum(student.attendance for student in students)
        return total_attendance / len(students)


if __name__ == "__main__":
    # Build a list of five SrmStudent objects matching sample data
    students = [
        SrmStudent("Kavya", "REG001", 98),
        SrmStudent("Anitha", "REG002", 68),
        SrmStudent("Karthik", "REG003", 91),
        SrmStudent("Meera", "REG004", 74),
        SrmStudent("Suresh", "REG005", 60)
    ]

    # Print each student's details and eligibility status
    for student in students:
        status = "Eligible" if student.is_eligible() else "Detained"
        print(f"{student.name} - {student.attendance}% - {status}")

    # Calculate and print class average using the class name
    avg = SrmStudent.class_average(students)
    print(f"Class average: {avg:.1f}%")

'''
JUSTIFICATION FOR STATIC VS INSTANCE METHOD:

1. is_eligible() is an instance method because it operates on a specific student's 
   instance data (self.attendance). Every student object has its own attendance 
   and eligibility state.

2. class_average() is decorated with @staticmethod because calculating the average 
   is a general utility task that acts on a collection of students as a whole, 
   rather than relying on state from any single student instance.
'''
