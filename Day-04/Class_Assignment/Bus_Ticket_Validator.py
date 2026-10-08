class BusTicket:
    def __init__(self, passenger_name: str, destination: str):
        """
        Validates input at construction time.
        Raises ValueError for invalid inputs.
        """
        # Validate passenger_name
        if not self._is_valid_string(passenger_name):
            raise ValueError(f"Invalid passenger name: '{passenger_name}'")
            
        # Validate destination
        if not self._is_valid_string(destination):
            raise ValueError(f"Invalid destination: '{destination}'")
            
        self.passenger_name = passenger_name.strip()
        self.destination = destination.strip()
        self.is_checked_in = False

    @staticmethod
    def _is_valid_string(val: str) -> bool:
        """
        Checks if string is non-null, non-whitespace-only, 
        and consists only of letters/spaces.
        """
        if val is None or not isinstance(val, str):
            return False
        
        trimmed = val.strip()
        if len(trimmed) == 0:
            return False
        
        # Ensures names/destinations only contain alphabetic characters and spaces
        return all(char.isalpha() or char.isspace() for char in trimmed)

    def mark_checked_in(self):
        """Marks ticket as checked in; raises error if already checked in."""
        if self.is_checked_in:
            raise ValueError("Ticket is already checked in.")
        self.is_checked_in = True

    @staticmethod
    def process_batch(raw_bookings: list[list[str]]) -> None:
        """
        Processes a list of raw [passengerName, destination] attempts and prints the summary.
        """
        accepted_tickets = []
        accepted_pairs = set()
        
        valid_count = 0
        rejected_count = 0
        duplicate_count = 0

        for attempt in raw_bookings:
            if not attempt or len(attempt) < 2:
                rejected_count += 1
                continue

            name, dest = attempt[0], attempt[1]

            # Try constructing ticket (fails at construction time for invalid inputs)
            try:
                ticket = BusTicket(name, dest)
            except ValueError:
                rejected_count += 1
                continue

            # Check for duplicates among valid bookings
            pair_key = (ticket.passenger_name, ticket.destination)
            if pair_key in accepted_pairs:
                duplicate_count += 1
            else:
                accepted_pairs.add(pair_key)
                accepted_tickets.append(ticket)
                valid_count += 1

        print(f"Valid: {valid_count} | Rejected: {rejected_count} | Duplicates skipped: {duplicate_count}")


# --- Example Run ---
if __name__ == "__main__":
    raw_attempts = [
        ["Divya", "Chennai"],
        ["", "Bangalore"],
        ["Ravi123", "Pune"],
        ["Divya", "Chennai"],
        [" ", " "]
    ]

    BusTicket.process_batch(raw_attempts)
