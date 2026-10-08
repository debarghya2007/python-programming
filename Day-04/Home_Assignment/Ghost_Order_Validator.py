class FoodOrder:
    def __init__(self, student_name: str, dish_name: str):
        """
        Constructor validates student_name and dish_name at initialization time.
        Raises ValueError for blank, None, or whitespace-only inputs.
        """
        if not self._is_valid_field(student_name):
            raise ValueError(f"Invalid student name: {student_name!r}")
            
        if not self._is_valid_field(dish_name):
            raise ValueError(f"Invalid dish name: {dish_name!r}")

        self.student_name = student_name.strip()
        self.dish_name = dish_name.strip()
        self.is_delivered = False

    @staticmethod
    def _is_valid_field(val: str) -> bool:
        """Helper to ensure a field is non-None, non-empty, and not purely whitespace."""
        if val is None or not isinstance(val, str):
            return False
        return len(val.strip()) > 0

    def mark_delivered(self) -> None:
        """
        Marks order as delivered. 
        Prints a warning message if it has already been delivered previously.
        """
        if self.is_delivered:
            print(f"WARNING: Order for '{self.student_name}' ({self.dish_name}) was already delivered! Possible double-serve.")
        else:
            self.is_delivered = True
            print(f"Order for '{self.student_name}' ({self.dish_name}) marked as delivered.")

    @staticmethod
    def process_batch(raw_orders: list[list[str]]) -> None:
        """
        Processes a batch of raw [studentName, dishName] entries,
        counting valid vs rejected orders.
        """
        valid_count = 0
        rejected_count = 0
        accepted_orders = []

        for attempt in raw_orders:
            if not attempt or len(attempt) < 2:
                rejected_count += 1
                continue

            student_name, dish_name = attempt[0], attempt[1]

            try:
                # Construct order (fails at construction time for invalid inputs)
                order = FoodOrder(student_name, dish_name)
                accepted_orders.append(order)
                valid_count += 1
            except ValueError:
                rejected_count += 1

        print(f"Valid: {valid_count} | Rejected: {rejected_count}")


# --- Verification ---
if __name__ == "__main__":
    # Test batch from the image example
    test_batch = [
        ["Ravi", "Paneer Butter Masala"],
        ["", "Chole Bhature"],
        ["Meera", " "],
        ["Divya", "Veg Biryani"]
    ]

    # Batch output: Valid: 2 | Rejected: 2
    FoodOrder.process_batch(test_batch)

    print("\n--- Testing Double Delivery ---")
    order = FoodOrder("Divya", "Veg Biryani")
    order.mark_delivered()  # First attempt
    order.mark_delivered()  # Second attempt triggers alert
