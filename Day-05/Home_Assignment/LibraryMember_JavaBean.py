import hashlib


class LibraryMember:
    def __init__(self, *args):
        # Chained constructor routing (simulating Java's this(...))
        if len(args) == 0:
            # 1. No-arg constructor: LibraryMember() -> calls this(None, None)
            self._this(None, None)
        elif len(args) == 1:
            # 2. Name-only constructor: LibraryMember(name) -> calls this(None, name)
            self._this(None, args[0])
        elif len(args) == 2:
            # 3. ID + Name constructor: LibraryMember(membership_id, name)
            self._this(args[0], args[1])
        else:
            raise TypeError("Invalid number of constructor arguments")

    def _this(self, membership_id: str | None, name: str | None) -> None:
        """Central initialization logic linked via constructor chaining."""
        self._membership_id = None
        if membership_id is not None:
            self.set_membership_id(membership_id)

        self._name = name
        self._premium_member = False
        self._security_answer_hash = None  # Write-only field

    # --- JavaBean-compliant Getters & Setters ---

    def get_membership_id(self) -> str | None:
        return self._membership_id

    def set_membership_id(self, membership_id: str) -> None:
        """Write-once property: takes effect only once, ever."""
        if self._membership_id is None and membership_id is not None:
            self._membership_id = membership_id

    def get_name(self) -> str | None:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def is_premium_member(self) -> bool:
        return self._premium_member

    def set_premium_member(self, premium: bool) -> None:
        self._premium_member = premium

    def set_security_answer(self, answer: str) -> None:
        """
        Write-only property: stores a deterministic one-way transformation (SHA-256 hash)
        without providing any getter method.
        """
        if answer is not None:
            self._security_answer_hash = hashlib.sha256(answer.encode('utf-8')).hexdigest()

    # Java-style camelCase alias methods for test-case compatibility
    getMembershipId = get_membership_id
    setMembershipId = set_membership_id
    getName = get_name
    setName = set_name
    isPremiumMember = is_premium_member
    setPremiumMember = set_premium_member
    setSecurityAnswer = set_security_answer


if __name__ == "__main__":
    # --- Example 1: Name-only constructor (ID remains None / null) ---
    m1 = LibraryMember("Priya Nair")
    print(f"Membership ID: {m1.getMembershipId()}")

    # --- Example 2: ID + Name constructor ---
    m2 = LibraryMember("LIB-8841", "Priya Nair")
    print(f"Membership ID: {m2.getMembershipId()}")

    # --- Example 3: Write-once membershipId test ---
    m3 = LibraryMember()
    m3.setMembershipId("LIB-8841")
    m3.setMembershipId("FAKE-0000")  # Silently ignored!
    print(f"Membership ID after overwrite attempt: {m3.getMembershipId()}")

    # --- Example 4: Write-only Security Answer ---
    m3.setSecurityAnswer("Secret123")
