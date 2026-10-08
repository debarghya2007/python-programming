class BoardingPenaltyCalculator:
    def __init__(self, minimum_penalty_percent: float):
        """
        Initializes the calculator with a minimum penalty percentage floor.
        Converts percentage (e.g., 1.0) to decimal rate (e.g., 0.01) if passed as percentage,
        or accepts direct decimal representation.
        """
        if minimum_penalty_percent < 0:
            raise ValueError("Minimum penalty percent cannot be negative.")
            
        # Standardize representation (e.g., 1% floor = 0.01 rate)
        self._minimum_penalty_rate = (
            minimum_penalty_percent / 100.0 if minimum_penalty_percent >= 1.0 else minimum_penalty_percent
        )

    def calculate_penalty(self, ticket_fare: float, minutes_late: int) -> float:
        """
        Closed-form O(1) penalty calculation with tiered escalation rates 
        and minimum flat-fee floor enforcement.
        """
        # Input Validation at calculation time
        if ticket_fare < 0:
            raise ValueError("Ticket fare cannot be negative.")
        if minutes_late < 0:
            raise ValueError("Minutes late cannot be negative.")

        # On-time passengers never trigger penalties or minimum floor
        if minutes_late == 0:
            return 0.0

        # Closed-form O(1) bracket calculation
        # Tier 1: Minutes 1–5 @ 0.5% per minute
        m1 = min(minutes_late, 5)
        
        # Tier 2: Minutes 6–15 @ 1.0% per minute
        m2 = max(0, min(minutes_late - 5, 10))
        
        # Tier 3: Minutes 16+ @ 2.0% per minute
        m3 = max(0, minutes_late - 15)

        total_rate = (m1 * 0.005) + (m2 * 0.01) + (m3 * 0.02)
        tiered_penalty = ticket_fare * total_rate

        # Apply minimum flat-fee floor only when genuinely late
        minimum_floor = ticket_fare * self._minimum_penalty_rate

        return max(tiered_penalty, minimum_floor)


# --- Example Verification ---
if __name__ == "__main__":
    # Configured with 1% minimum penalty floor (0.01)
    calc = BoardingPenaltyCalculator(0.01)

    # Example 1: ticketFare = 1000, minutesLate = 0 -> Rs 0.0
    print("Example 1:", calc.calculate_penalty(1000, 0))

    # Example 2: ticketFare = 1000, minutesLate = 1 -> Rs 10.0 (Floor applied)
    print("Example 2:", calc.calculate_penalty(1000, 1))

    # Example 3: ticketFare = 1000, minutesLate = 16 -> Rs 145.0
    # Tier 1: 5 * 0.005 * 1000 = 25
    # Tier 2: 10 * 0.01 * 1000 = 100
    # Tier 3: 1 * 0.02 * 1000  = 20
    # Total = 25 + 100 + 20    = 145.0
    print("Example 3:", calc.calculate_penalty(1000, 16))
