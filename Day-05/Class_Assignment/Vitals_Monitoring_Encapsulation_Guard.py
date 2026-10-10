class PatientVitals:
    def __init__(self, initial_readings: list[float] = None):
        # Private field to encapsulate readings history
        self.__readings: list[float] = []

        # Seed initial readings by reusing record_reading to avoid duplicating range checks
        if initial_readings:
            for reading in initial_readings:
                self.record_reading(reading)

    def record_reading(self, reading: float) -> None:
        """Silently rejects readings <= 0 or > 45°C without throwing an exception."""
        if 0 < reading <= 45.0:
            self.__readings.append(reading)

    def get_average(self) -> float:
        """Returns the average of valid recorded readings."""
        if not self.__readings:
            return 0.0
        return sum(self.__readings) / len(self.__readings)

    def get_all_readings(self) -> list[float]:
        """Returns a defensive copy of the readings to prevent external mutation."""
        return self.__readings.copy()


if __name__ == "__main__":
    # --- Example 1: Constructor filters invalid readings (-2 is rejected) ---
    v = PatientVitals([36.5, -2, 37.1])
    print(v.get_all_readings())
    # Output: [36.5, 37.1]

    # --- Example 2: Defensive Copy Verification ---
    copy_list = v.get_all_readings()
    copy_list[0] = 999  # Mutating the returned array/list

    print(f"Original after modifying copy: {v.get_all_readings()[0]}")
    # Output: 36.5 (internal state remains untouched)

    # --- Example 3: Average Calculation ---
    print(f"Average: {v.get_average():.2f}")
    # Output: Average: 36.80
