import re


class LoanReceipt:
    def __init__(self, member_id: str, book_ids: list[str]):
        if book_ids is None:
            raise ValueError("construction rejected")
        
        # Validate each book ID format: "BK-" followed by exactly 3 digits[cite: 19]
        validated_ids = []
        for bid in book_ids:
            if not isinstance(bid, str) or not re.match(r"^BK-\d{3}$", bid):
                raise ValueError("construction rejected")
            validated_ids.append(bid)

        self.__member_id: str = member_id
        self.__book_ids: list[str] = list(validated_ids)  # Defensive copy on entry[cite: 19]

    def get_member_id(self) -> str:
        return self.__member_id

    def get_book_ids(self) -> list[str]:
        return list(self.__book_ids)  # Defensive copy on exit[cite: 19]

    def with_corrected_book_id(self, index: int, new_id: str) -> "LoanReceipt":
        """Wither pattern: returns a brand-new immutable receipt with a corrected book ID[cite: 19]."""
        if not isinstance(new_id, str) or not re.match(r"^BK-\d{3}$", new_id):
            raise ValueError("Invalid book ID format")
        new_ids = list(self.__book_ids)
        new_ids[index] = new_id
        return LoanReceipt(self.__member_id, new_ids)

    # Java-style camelCase alias methods for test compatibility
    getMemberId = get_member_id
    getBookIds = get_book_ids
    withCorrectedBookId = with_corrected_book_id


class ReferenceOnlyLoanReceipt(LoanReceipt):
    def __init__(self, member_id: str, book_ids: list[str], room_number: str):
        super().__init__(member_id, book_ids)
        self.__room_number: str = room_number

    def get_room_number(self) -> str:
        return self.__room_number

    getRoomNumber = get_room_number


class LoanCirculationLedger:
    @staticmethod
    def process_nightly_circulation(receipts) -> str:
        """
        Null-safe nightly processor that settles ReferenceOnlyLoanReceipt 
        differently from regular receipts using type inspection[cite: 20].
        """
        processed_count = 0
        null_skipped = 0
        ref_only_count = 0
        regular_count = 0

        if receipts is not None:
            for receipt in receipts:
                if receipt is None:
                    null_skipped += 1
                else:
                    processed_count += 1
                    if isinstance(receipt, ReferenceOnlyLoanReceipt):
                        ref_only_count += 1
                    else:
                        regular_count += 1

        return f"{processed_count} processed | {null_skipped} null skipped | {ref_only_count} reference-only | {regular_count} regular"

    # Java-style camelCase alias for static method
    processNightlyCirculation = process_nightly_circulation


if __name__ == "__main__":
    # --- Example 1: Constructor validation rejection ---
    try:
        LoanReceipt("LIB-8841", ["BK-100", "bad"])
    except ValueError as e:
        print(f"new LoanReceipt construction test: {e}")
    # Output: construction rejected[cite: 19]

    # --- Example 2: Defensive copying and immutability test ---
    r = LoanReceipt("LIB-8841", ["BK-100", "BK-101"])
    ids = r.getBookIds()
    ids[0] = "HACKED"  # External mutation attempt
    print(f"Original book ID after external mutation attempt: {r.getBookIds()[0]}")
    # Output: "BK-100"[cite: 19]

    # --- Example 3: Wither pattern test ---
    r_corrected = r.withCorrectedBookId(0, "BK-999")
    print(f"Original ID: {r.getBookIds()[0]} | Corrected New Receipt ID: {r_corrected.getBookIds()[0]}")

    # --- Example 4: Nightly Circulation Batch Processing ---
    batch = [
        ReferenceOnlyLoanReceipt("LIB-001", ["BK-200"], "Reading Room 3"),
        None,
        LoanReceipt("LIB-002", ["BK-201"])
    ]
    summary = LoanCirculationLedger.processNightlyCirculation(batch)
    print(summary)
    # Output: 2 processed | 1 null skipped | 1 reference-only | 1 regular[cite: 20]
