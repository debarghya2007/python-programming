class SurgeFeeCalculator:
    def __init__(self, minimum_surge_percent: float):
        """
        Initializes the calculator with a minimum surge percentage floor.
        Converts percentage (e.g., 1.0 for 1%) to decimal rate (0.01).
        """
        if minimum_surge_percent < 0:
            raise ValueError("Minimum surge percent cannot be negative.")
            
        self._minimum_surge_rate = (
            minimum_surge_percent / 100.0 if minimum_surge_percent >= 1.0 else minimum_surge_percent
        )

    def calculate_surge_fee(self, order_value: float, delay_minutes: int) -> float:
        """
        Closed-form O(1) calculation for escalating surge fees with floor enforcement.
        Rejects negative order values or negative delay minutes at calculation time.
        """
        if order_value < 0:
            raise ValueError("Order value cannot be negative.")
        if delay_minutes < 0:
            raise ValueError("Delay minutes cannot be negative.")

        # On-time orders never incur surge fees or trigger minimum floor
        if delay_minutes == 0:
            return 0.0

        # Closed-form O(1) bracket calculation
        # Minutes 1–5 @ 0.5% per minute
        m1 = min(delay_minutes, 5)
        
        # Minutes 6–15 @ 1.0% per minute
        m2 = max(0, min(delay_minutes - 5, 10))
        
        # Minutes 16+ @ 2.0% per minute
        m3 = max(0, delay_minutes - 15)

        total_rate = (m1 * 0.005) + (m2 * 0.01) + (m3 * 0.02)
        tiered_surge = order_value * total_rate

        # Apply minimum floor only when genuinely delayed
        minimum_floor = order_value * self._minimum_surge_rate

        return max(tiered_surge, minimum_floor)


# --- Example Verification ---
if __name__ == "__main__":
    # Configured with 1% minimum surge floor (0.01)
    calc = SurgeFeeCalculator(0.01)

    # Example 1: orderValue = 500, delayMinutes = 0 -> Rs 0.0
    print("Example 1:", calc.calculate_surge_fee(500, 0))

    # Example 2: orderValue = 500, delayMinutes = 1 -> Rs 5.0 (Floor applied)
    print("Example 2:", calc.calculate_surge_fee(500, 1))

    # Example 3: orderValue = 500, delayMinutes = 16 -> Rs 72.5
    print("Example 3:", calc.calculate_surge_fee(500, 16))
