class BusTicketAccount:
    # Class-level state (equivalent to static initialization block)
    MIN_PENALTY_RATE = 0.01  # 1% minimum penalty floor

    def __init__(self, booking_id: str, ticket_fare: float = 0.0):
        """
        Full constructor with chaining support for provisional bookings (default ticket_fare = 0.0).
        """
        if ticket_fare < 0:
            raise ValueError("Ticket fare cannot be negative.")
            
        self.booking_id = booking_id
        self.ticket_fare = float(ticket_fare)

    @classmethod
    def provisional(cls, booking_id: str):
        """Chained constructor for provisional account creation."""
        return cls(booking_id, ticket_fare=0.0)

    def calculate_penalty(self, minutes_late: int) -> float:
        """
        Calculates boarding penalty using Problem 4's tiered rate model + floor rule.
        """
        if minutes_late <= 0:
            return 0.0

        # Tiered bracket rates
        m1 = min(minutes_late, 5)            # 1-5 mins @ 0.5%
        m2 = max(0, min(minutes_late - 5, 10)) # 6-15 mins @ 1.0%
        m3 = max(0, minutes_late - 15)        # 16+ mins @ 2.0%

        total_rate = (m1 * 0.005) + (m2 * 0.01) + (m3 * 0.02)
        tiered_penalty = self.ticket_fare * total_rate
        minimum_floor = self.ticket_fare * self.MIN_PENALTY_RATE

        return max(tiered_penalty, minimum_floor)


class SleeperBusTicketAccount(BusTicketAccount):
    """
    Sleeper-coach accounts settle differently (e.g., 1.5x penalty multiplier due to berth hold-ups).
    """
    SLEEPER_SURCHARGE_MULTIPLIER = 1.5

    def calculate_penalty(self, minutes_late: int) -> float:
        base_penalty = super().calculate_penalty(minutes_late)
        return base_penalty * self.SLEEPER_SURCHARGE_MULTIPLIER


class ReconciliationEngine:
    @staticmethod
    def process_batch(
        accounts: list, amounts: list[float], minutes_late_array: list[int]
    ) -> None:
        """
        Single-pass O(N) batch reconciliation processor handling mixed accounts, 
        sleeper accounts, and null placeholders safely.
        """
        # Array length mismatch check to prevent misaligned passenger data
        if not (len(accounts) == len(amounts) == len(minutes_late_array)):
            raise ValueError("Batch processing aborted: Input arrays must have matching lengths.")

        processed_count = 0
        null_skipped_count = 0
        sleeper_count = 0
        regular_count = 0
        grand_total_penalties = 0.0

        # Single pass over the batch
        for account, amount, minutes_late in zip(accounts, amounts, minutes_late_array):
            # Safe null checking
            if account is None:
                null_skipped_count += 1
                continue

            processed_count += 1

            # Type identification using isinstance (Python equivalent of instanceof)
            if isinstance(account, SleeperBusTicketAccount):
                sleeper_count += 1
            elif isinstance(account, BusTicketAccount):
                regular_count += 1

            # Calculate penalty for the account
            penalty = account.calculate_penalty(minutes_late)
            grand_total_penalties += penalty

        # Formatted Output Summary
        print(
            f"{processed_count} processed | "
            f"{null_skipped_count} null skipped | "
            f"{sleeper_count} sleeper | "
            f"{regular_count} regular | "
            f"grand total penalties = Rs {grand_total_penalties:.2f}"
        )


# --- Verification ---
if __name__ == "__main__":
    # Test batch matching the example in image
    accounts_batch = [
        SleeperBusTicketAccount("BK001", 2000.0),
        None,  # Null entry left by buggy upstream process
        BusTicketAccount("BK002", 1200.0),
    ]

    amounts_batch = [1200.0, 900.0, 700.0]
    minutes_late_batch = [10, 5, 0]

    ReconciliationEngine.process_batch(
        accounts_batch, amounts_batch, minutes_late_batch
    )
