class DeliveryAccount:
    # Class-level state (equivalent to static block configuration)
    MIN_SURGE_RATE = 0.01  # 1% minimum surge floor

    def __init__(self, student_id: str, order_value: float = 0.0):
        """
        Full constructor with chaining support for provisional accounts (default order_value = 0.0).
        """
        if order_value < 0:
            raise ValueError("Order value cannot be negative.")

        self.student_id = student_id
        self.order_value = float(order_value)

    @classmethod
    def provisional(cls, student_id: str):
        """Chained constructor for provisional account creation."""
        return cls(student_id, order_value=0.0)

    def calculate_surge_fee(self, delay_minutes: int) -> float:
        """
        Calculates surge fee using Problem 4's tiered rate model + floor rule.
        """
        if delay_minutes <= 0:
            return 0.0

        # Tiered bracket rates:
        # Minutes 1-5 @ 0.5% per min
        m1 = min(delay_minutes, 5)
        # Minutes 6-15 @ 1.0% per min
        m2 = max(0, min(delay_minutes - 5, 10))
        # Minutes 16+ @ 2.0% per min
        m3 = max(0, delay_minutes - 15)

        total_rate = (m1 * 0.005) + (m2 * 0.01) + (m3 * 0.02)
        tiered_surge = self.order_value * total_rate
        minimum_floor = self.order_value * self.MIN_SURGE_RATE

        return max(tiered_surge, minimum_floor)


class PremiumDeliveryAccount(DeliveryAccount):
    """
    Premium account holders receive settled discounts on surge fees (e.g., 50% waiver).
    """
    PREMIUM_DISCOUNT_FACTOR = 0.5

    def calculate_surge_fee(self, delay_minutes: int) -> float:
        base_surge = super().calculate_surge_fee(delay_minutes)
        return base_surge * self.PREMIUM_DISCOUNT_FACTOR


class ReconciliationEngine:
    @staticmethod
    def process_batch(
        accounts: list, amounts: list[float], delay_minutes_array: list[int]
    ) -> None:
        """
        Single-pass O(N) batch processor for multi-kitchen reconciliation.
        Safely handles regular accounts, premium accounts, and null entries.
        """
        # Guard clause against array length mismatch
        if not (len(accounts) == len(amounts) == len(delay_minutes_array)):
            raise ValueError("Batch processing error: Parallel input arrays must have equal lengths.")

        processed_count = 0
        null_skipped_count = 0
        premium_count = 0
        regular_count = 0
        grand_total_surge_fees = 0.0

        # Single-pass iteration
        for account, amount, delay_minutes in zip(accounts, amounts, delay_minutes_array):
            # Null check safeguard
            if account is None:
                null_skipped_count += 1
                continue

            processed_count += 1

            # Instance type checking using isinstance (equivalent to instanceof)
            if isinstance(account, PremiumDeliveryAccount):
                premium_count += 1
            elif isinstance(account, DeliveryAccount):
                regular_count += 1

            # Calculate surge fee
            surge_fee = account.calculate_surge_fee(delay_minutes)
            grand_total_surge_fees += surge_fee

        # Printed Summary
        print(
            f"{processed_count} processed | "
            f"{null_skipped_count} null skipped | "
            f"{premium_count} premium | "
            f"{regular_count} regular | "
            f"grand total surge fees = {grand_total_surge_fees:.1f}"
        )


# --- Verification ---
if __name__ == "__main__":
    # Test batch matching the image example
    accounts_batch = [
        PremiumDeliveryAccount("STU001", 500.0),
        None,  # Null entry
        DeliveryAccount("STU002", 300.0)
    ]

    amounts_batch = [500.0, 400.0, 300.0]
    delay_minutes_batch = [10, 5, 0]

    ReconciliationEngine.process_batch(
        accounts_batch, amounts_batch, delay_minutes_batch
    )
