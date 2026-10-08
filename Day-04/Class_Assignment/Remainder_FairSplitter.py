from typing import List

class FareSplitter:
    def __init__(self, trip_id: str, total_fare: float = 0.0, passenger_count: int = 2):
        """
        Primary Constructor with default values for optional parameters.
        Rejects invalid inputs at initialization time.
        """
        if total_fare < 0:
            raise ValueError("Total fare cannot be negative.")
        if passenger_count <= 0:
            raise ValueError("Passenger count must be greater than zero.")

        self.trip_id = trip_id
        self.total_fare = float(total_fare)
        self.passenger_count = int(passenger_count)

    # Class methods providing chained constructor alternatives
    @classmethod
    def from_fare(cls, trip_id: str, total_fare: float):
        """Creates a split using trip_id and total_fare (defaults passenger_count to 2)."""
        return cls(trip_id, total_fare, passenger_count=2)

    @classmethod
    def provisional(cls, trip_id: str):
        """Creates a provisional split using only trip_id."""
        return cls(trip_id, total_fare=0.0, passenger_count=2)

    def fare_breakdown(self) -> List[float]:
        """
        Splits fare fairly across passengers, allocating any remainder to the last share
        so no money is lost to rounding errors.
        """
        total_cents = int(round(self.total_fare * 100))
        base_cents = total_cents // self.passenger_count
        remainder_cents = total_cents % self.passenger_count

        shares = [base_cents] * self.passenger_count
        shares[-1] += remainder_cents  # Assign extra paisa/cents to final share

        return [round(share / 100.0, 2) for share in shares]

    def is_confirmation_overdue(self, confirmed: int, expected: int) -> bool:
        """Returns True if confirmed bookings are strictly less than expected bookings."""
        return confirmed < expected


# --- Verification ---
if __name__ == "__main__":
    # Example 1: Uneven breakdown
    fs1 = FareSplitter("TRIP001", 100000.0, 3)
    print("TRIP001 Breakdown:", fs1.fare_breakdown())
    # Output: [33333.33, 33333.33, 33333.34]

    # Example 2: Provisional split
    fs2 = FareSplitter("TRIP003")
    print("TRIP003 Breakdown:", fs2.fare_breakdown())
    # Output: [0.0, 0.0]

    # Example 3: Check confirmation status
    print("Is Overdue (1 confirmed vs 3 expected):", fs1.is_confirmation_overdue(1, 3))
    # Output: True
