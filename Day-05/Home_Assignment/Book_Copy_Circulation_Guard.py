class BookInventory:
    def __init__(self, copies_total: int):
        # Reject 0 or negative total copies outright at construction time
        if copies_total <= 0:
            raise ValueError("construction rejected")

        self.__copies_total: int = copies_total
        self.__copies_available: int = copies_total

    def check_out(self) -> None:
        """Silently rejects checkout if no available copies remain."""
        if self.__copies_available > 0:
            self.__copies_available -= 1

    def check_in(self) -> None:
        """Silently rejects check-in if inventory is already full."""
        if self.__copies_available < self.__copies_total:
            self.__copies_available += 1

    def get_copies_available(self) -> int:
        """Returns the current number of available copies."""
        return self.__copies_available

    # Java-style camelCase alias methods for test compatibility
    checkOut = check_out
    checkIn = check_in
    getCopiesAvailable = get_copies_available


if __name__ == "__main__":
    # --- Example 1: Constructor rejection on zero or negative starting count ---
    try:
        b_invalid = BookInventory(0)
    except ValueError as e:
        print(f"new BookInventory(0): {e}")
    # Output: construction rejected[cite: 18]

    # --- Example 2: Out-of-bounds checkOut (Boundary protection) ---
    b = BookInventory(3)
    b.checkOut()
    b.checkOut()
    b.checkOut()
    b.checkOut()  # 4th checkout - silently ignored
    print(f"Copies available after 4 checkouts: {b.getCopiesAvailable()}")
    # Output: 0[cite: 18]

    # --- Example 3: Out-of-bounds checkIn (Inventory overflow protection) ---
    b.checkIn()
    b.checkIn()
    b.checkIn()
    b.checkIn()  # 4th check-in - silently ignored
    print(f"Copies available after 4 check-ins: {b.getCopiesAvailable()}")
    # Output: 3[cite: 19]
