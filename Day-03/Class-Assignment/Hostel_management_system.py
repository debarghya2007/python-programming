class FeeAccount:
    def __init__(self, reg_no: str, total_fee: float, amount_paid: float = 0.0):
        self._reg_no = reg_no
        self._total_fee = total_fee
        self._amount_paid = amount_paid

    def pay(self, amount: float) -> None:
        """Rejects non-positive payments"""
        if amount <= 0:
            return  # Rejected payment
        self._amount_paid += amount

    def get_due(self) -> float:
        return self._total_fee - self._amount_paid


class HostelFeeAccount(FeeAccount):
    def __init__(self, reg_no: str, total_fee: float, amount_paid: float = 0.0):
        super().__init__(reg_no, total_fee, amount_paid)

    def pay_in_two_installments(self, amount: float) -> None:
        installment = amount / 2.0
        self.pay(installment)
        self.pay(installment)


class HostelRoom:
    def __init__(self, room_no: str, beds: int, occupied: int = 0):
        self.room_no = room_no
        self.beds = beds
        self.occupied = occupied

    def allot(self) -> bool:
        if self.occupied < self.beds:
            self.occupied += 1
            return True
        return False

    @staticmethod
    def find_available_room(rooms: list['HostelRoom']) -> 'HostelRoom | None':
        for room in rooms:
            if room.occupied < room.beds:
                return room
        return None

    @staticmethod
    def safe_allot(rooms: list['HostelRoom']) -> 'HostelRoom | None':
        """Null-safe room allotment process"""
        room = HostelRoom.find_available_room(rooms)
        if room is not None:
            room.allot()
            return room
        return None


class SrmStudent:
    total_students = 0  # Static/class counter

    def __init__(self, name: str, reg_no: str, fee_account: HostelFeeAccount, room: HostelRoom | None = None):
        self.name = name
        self.reg_no = reg_no
        self.fee_account = fee_account  # Field as an object
        self.room = room                # Field as an object (or None)
        SrmStudent.total_students += 1

    def full_status(self) -> str:
        room_str = self.room.room_no if self.room is not None else "unallotted"
        return f"{self.name} | Due: Rs {self.fee_account.get_due()} | Room: {room_str}"


if __name__ == "__main__":
    # Create available rooms with limited beds
    rooms = [
        HostelRoom("C-214", 3, 2),  # 1 bed available
        HostelRoom("C-507", 2, 1)   # 1 bed available
    ]

    # Student 1: Valid payment + Room allotted
    ravi_acc = HostelFeeAccount("RA001", 200000.0)
    ravi_acc.pay_in_two_installments(60000.0)
    ravi_room = HostelRoom.safe_allot(rooms)
    s1 = SrmStudent("Ravi", "RA001", ravi_acc, ravi_room)

    # Student 2: Rejected negative payment + Room allotted
    anitha_acc = HostelFeeAccount("RA002", 180000.0)
    anitha_acc.pay(-5000.0)  # Rejected payment
    anitha_room = HostelRoom.safe_allot(rooms)
    s2 = SrmStudent("Anitha", "RA002", anitha_acc, anitha_room)

    # Student 3: Valid payment + Left unallotted (no free rooms remaining)
    karthik_acc = HostelFeeAccount("RA003", 200000.0)
    karthik_room = HostelRoom.safe_allot(rooms)  # Returns None as rooms are full
    s3 = SrmStudent("Karthik", "RA003", karthik_acc, karthik_room)

    # Display student statuses
    print(s1.full_status())
    print(s2.full_status())
    print(s3.full_status())
    print(f"Total students: {SrmStudent.total_students}")
