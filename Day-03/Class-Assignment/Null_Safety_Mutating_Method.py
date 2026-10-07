class HostelRoom:
    def __init__(self, room_no: str, beds: int, occupied: int):
        self.room_no = room_no
        self.beds = beds
        self.occupied = occupied

    # Allots a bed if one is free
    def allot(self, student_name: str) -> None:
        if self.occupied < self.beds:
            self.occupied += 1
            print(f"{student_name} allotted to room {self.room_no}")

    # Static method to find the first room with an available bed
    @staticmethod
    def find_available_room(rooms: list['HostelRoom']) -> 'HostelRoom | None':
        for room in rooms:
            if room.occupied < room.beds:
                return room
        return None  # Equivalent to null in Java

    # Static method to safely allot a room without risk of None/Null errors
    @staticmethod
    def safe_allot(rooms: list['HostelRoom'], student_name: str) -> None:
        available_room = HostelRoom.find_available_room(rooms)
        
        # Check for None before invoking any methods
        if available_room is not None:
            available_room.allot(student_name)
        else:
            print(f"No rooms available for {student_name}")


if __name__ == "__main__":
    # Test Case 1: Array containing an available room (C-214: 2/3)[cite: 3]
    rooms1 = [
        HostelRoom("C-214", 3, 2),
        HostelRoom("C-507", 2, 2)
    ]
    HostelRoom.safe_allot(rooms1, "Divya")

    # Test Case 2: Array where every room is already full (C-214: 3/3, C-507: 2/2)[cite: 3]
    rooms2 = [
        HostelRoom("C-214", 3, 3),
        HostelRoom("C-507", 2, 2)
    ]
    HostelRoom.safe_allot(rooms2, "Divya")

'''
WHY PASSING THE ROOMS ARRAY DOES NOT COPY THE ROOMS THEMSELVES:

In Python (as in Java), arguments are passed by object reference[cite: 3]. The list containing 
the `HostelRoom` objects holds reference pointers to the actual objects in memory, 
rather than duplicate copies of the object data[cite: 3]. 

When `safe_allot` or `find_available_room` receives the list, it accesses the exact same 
`HostelRoom` instances in memory[cite: 3]. Any mutation (such as incrementing `self.occupied` 
inside `allot()`) modifies the original room object directly[cite: 3].
'''
