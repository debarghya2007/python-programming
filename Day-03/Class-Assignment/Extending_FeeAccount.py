class FeeAccount:
    def __init__(self, reg_no: str, total_fee: float, amount_paid: float = 0.0):
        self._reg_no = reg_no            # Encapsulated attribute (private prefix)
        self._total_fee = total_fee
        self._amount_paid = amount_paid

    def pay(self, amount: float) -> None:
        """Rejects non-positive payments"""
        if amount <= 0:
            print("Payment amount must be positive.")
            return
        self._amount_paid += amount

    def get_due(self) -> float:
        return self._total_fee - self._amount_paid


class HostelFeeAccount(FeeAccount):
    def __init__(self, reg_no: str, total_fee: float, amount_paid: float = 0.0):
        super().__init__(reg_no, total_fee, amount_paid)

    def pay_in_two_installments(self, amount: float) -> None:
        """Pays the total amount across two equal installments"""
        installment = amount / 2.0
        self.pay(installment)
        self.pay(installment)


class ScholarshipFeeAccount(FeeAccount):
    def __init__(self, reg_no: str, total_fee: float, amount_paid: float, scholarship_percent: float):
        super().__init__(reg_no, total_fee, amount_paid)
        self._scholarship_percent = scholarship_percent  # 0 to 100

    def effective_due(self) -> float:
        """Returns getDue() reduced by the scholarship percentage"""
        due = self.get_due()
        discount = (self._scholarship_percent / 100.0) * due
        return due - discount


if __name__ == "__main__":
    # Create one of each account type matching the sample input
    plain_acc = FeeAccount("REG101", 150000.0)
    plain_acc.pay(150000.0)

    hostel_acc = HostelFeeAccount("REG102", 200000.0)
    hostel_acc.pay_in_two_installments(60000.0)

    scholarship_acc = ScholarshipFeeAccount("REG103", 180000.0, 0.0, 20.0)

    accounts = [plain_acc, hostel_acc, scholarship_acc]

    # Process and print account details using isinstance() checks
    for acc in accounts:
        if isinstance(acc, ScholarshipFeeAccount):
            print(f"Scholarship account effective due: Rs {acc.effective_due()}")
        elif isinstance(acc, HostelFeeAccount):
            print(f"Hostel account due: Rs {acc.get_due()}")
        elif isinstance(acc, FeeAccount):
            print(f"Plain account due: Rs {acc.get_due()}")
