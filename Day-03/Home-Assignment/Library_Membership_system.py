# ==========================================
# 1. BROKEN VERSION (Static Misuse)
# ==========================================
class BrokenLibraryMember:
    # Class attributes (static fields shared by ALL instances)
    name = ""
    member_id = ""
    books_issued = 0

    def __init__(self, name: str, books_issued: int):
        # Incorrectly updating static fields on every instantiation
        BrokenLibraryMember.name = name
        BrokenLibraryMember.books_issued = books_issued


'''
EXPLANATION: WHY MARKING EACH FIELD AS STATIC IS WRONG

1. name:
   A member's name belongs to an individual person. Making it static causes every 
   `LibraryMember` object to share one name field in memory, so creating a new member 
   overwrites the name of all existing members.

2. memberId:
   A member ID is a unique personal identifier for a specific account. Making it static 
   assigns the exact same ID value to every single member in the system.

3. booksIssued:
   The count of borrowed books is unique to an individual member's borrowing history. 
   Making it static combines every member's borrowed books into a single shared number.
'''


# ==========================================
# 2. FIXED VERSION (Correct Class Design)
# ==========================================
class LibraryMember:
    # Static / Class variables shared across all members
    library_name = "Central Library"
    member_count = 0

    def __init__(self, name: str, books_issued: int):
        LibraryMember.member_count += 1
        
        # Instance variables unique to each library member
        self.name = name
        self.books_issued = books_issued
        
        # Automatically derive member_id using member_count (base: LM-1000)
        self.member_id = f"LM-{1000 + LibraryMember.member_count}"

    # Instance method to display member card details
    def print_member_card(self) -> None:
        print(f"{self.name} | {self.member_id}")

    # Static method operating on class-level data
    @staticmethod
    def print_total_members() -> None:
        print(f"Total members: {LibraryMember.member_count}")


# ==========================================
# DEMONSTRATION & TEST
# ==========================================
if __name__ == "__main__":
    # --- Testing Broken Version ---
    m1_broken = BrokenLibraryMember("Aditi", 2)
    m2_broken = BrokenLibraryMember("Rohan", 1)

    print(m1_broken.name)
    print(m2_broken.name)
    print("(Aditi's data was overwritten — both members now show \"Rohan\")\n")

    # --- Testing Fixed Version ---
    m1 = LibraryMember("Aditi", 2)
    m2 = LibraryMember("Rohan", 1)

    m1.print_member_card()
    m2.print_member_card()
    LibraryMember.print_total_members()
