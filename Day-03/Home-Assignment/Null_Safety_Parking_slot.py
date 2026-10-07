class ParkingSlot:
    def __init__(self, slot_no: str, capacity: int, occupied_count: int):
        self.slot_no = slot_no
        self.capacity = capacity
        self.occupied_count = occupied_count

    # Method to fill a spot if one is free[cite: 8]
    def allot(self, vehicle_no: str) -> None:
        if self.occupied_count < self.capacity:
            self.occupied_count += 1
            print(f"{vehicle_no} allotted to slot {self.slot_no}")

    # Static method returning the first slot with available space, or None if full[cite: 8]
    @staticmethod
    def find_available_slot(slots: list['ParkingSlot']) -> 'ParkingSlot | None':
        for slot in slots:
            if slot.occupied_count < slot.capacity:
                return slot
        return None  # Equivalent to null in Java[cite: 8]

    # Static method that checks for None before touching the object[cite: 8]
    @staticmethod
    def safe_allot(slots: list['ParkingSlot'], vehicle_no: str) -> None:
        available_slot = ParkingSlot.find_available_slot(slots)
        
        # Null-safe check to eliminate NPE risk[cite: 8]
        if available_slot is not None:
            available_slot.allot(vehicle_no)
        else:
            print(f"No slots available for {vehicle_no}")


if __name__ == "__main__":
    # Test Case 1: Array containing an available slot (A1: 3/4)[cite: 8]
    slots1 = [
        ParkingSlot("A1", 4, 3),
        ParkingSlot("A2", 5, 5)
    ]
    ParkingSlot.safe_allot(slots1, "TN09AB1234")

    # Test Case 2: Array where every slot is full (A1: 4/4, A2: 5/5)[cite: 8]
    slots2 = [
        ParkingSlot("A1", 4, 4),
        ParkingSlot("A2", 5, 5)
    ]
    ParkingSlot.safe_allot(slots2, "TN09AB1234")

'''
WHY PASSING THE PARKINGSLOT ARRAY DOES NOT COPY THE SLOTS:

In Python (as in Java), argument passing operates on object references[cite: 8]. The list 
stores reference pointers pointing to the actual `ParkingSlot` instances in memory, 
rather than duplicating the objects[cite: 8].

When `safe_allot` or `find_available_slot` receives the list, it operates directly on 
those exact memory instances[cite: 8]. Any modification (such as incrementing `occupied_count` 
inside `allot()`) updates the original `ParkingSlot` object directly[cite: 8].
'''
