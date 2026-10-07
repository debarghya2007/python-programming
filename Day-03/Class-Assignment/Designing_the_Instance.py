# ==========================================
# 1. BROKEN VERSION (Static Misuse)
# ==========================================
class BrokenSrmStudent:
    # Class attributes (static fields shared by ALL instances)
    name = ""
    reg_no = ""
    attendance = 0

    def __init__(self, name: str, attendance: int):
        # Incorrectly setting static fields on every instantiation
        BrokenSrmStudent.name = name
        BrokenSrmStudent.attendance = attendance

'''
EXPLANATION: WHY MARKING EACH FIELD AS STATIC IS WRONG

1. name:
   Making `name` static means every student object shares the exact same name variable in memory. 
   Creating a new student overwrites the name of all previously created students.

2. reg_no:
   A registration number is a unique identity for an individual student. Marking it static 
   means all students share one registration number rather than having unique instance identifiers.

3. attendance:
   Attendance belongs to an individual student. Making it static causes every student's 
   attendance tracking to collapse into a single shared value across the entire school.
'''


# ==========================================
# 2. FIXED VERSION (Correct Class Design)
# ==========================================
class SrmStudent:
    # Static / Class variables shared across all students
    university = "SRM"
    admission_count = 0

    def __init__(self, name: str, attendance: int):
        SrmStudent.admission_count += 1
        
        # Instance variables unique to each student
        self.name = name
        self.attendance = attendance
        
        # Automatically derive regNo using admission_count (base: RA231100301010)
        self.reg_no = f"RA2311003010{10 + SrmStudent.admission_count}"

    # Instance method to display student details
    def print_id_card(self) -> None:
        print(f"{self.name} | {self.reg_no}")

    # Static method operating on class-level data
    @staticmethod
    def print_total_admissions() -> None:
        print(f"Students admitted so far: {SrmStudent.admission_count}")


# ==========================================
# DEMONSTRATION & TEST
# ==========================================
if __name__ == "__main__":
    # --- Testing Broken Version ---
    print("--- Broken Version ---")
    s1_broken = BrokenSrmStudent("Ravi", 82)
    s2_broken = BrokenSrmStudent("Meera", 74)

    print(s1_broken.name)
    print(s2_broken.name)
    print("(Ravi's data was overwritten — both students now show \"Meera\")\n")

    # --- Testing Fixed Version ---
    print("--- Fixed Version ---")
    s1 = SrmStudent("Ravi", 82)
    s2 = SrmStudent("Meera", 74)

    s1.print_id_card()
    s2.print_id_card()
    SrmStudent.print_total_admissions()
