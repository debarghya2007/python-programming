class DeliverySlot:
    PEAK_HOURS = {
        "12:00-13:00",
        "13:00-14:00",
        "19:00-20:00",
        "20:00-21:00"
    }

    def __init__(self, order_id: str, time_slot: str = "ASAP"):
        """
        Primary constructor. Defaults time_slot to 'ASAP' if not explicitly provided,
        achieving constructor chaining without duplicating setup logic.
        """
        self.order_id = order_id
        self.time_slot = time_slot

    @classmethod
    def asap_booking(cls, order_id: str):
        """
        Explicit chained constructor for ASAP bookings.
        """
        return cls(order_id, time_slot="ASAP")

    def is_peak_hour(self) -> bool:
        """
        Returns True if the time slot corresponds to one of the four peak-hour slots.
        """
        return self.time_slot in self.PEAK_HOURS


# --- Verification ---
if __name__ == "__main__":
    # Example 1: Scheduled order in peak hour -> True
    slot1 = DeliverySlot("ORD101", "13:00-14:00")
    print("ORD101 isPeakHour():", slot1.is_peak_hour())  # Output: True

    # Example 2: ASAP order -> False
    slot2 = DeliverySlot("ORD102")
    print("ORD102 time_slot:", slot2.time_slot)         # Output: ASAP
    print("ORD102 isPeakHour():", slot2.is_peak_hour())  # Output: False
