from typing import List


class Canteen:
    def __init__(self, canteen_code: str, canteen_name: str, trust_score: int = 3):
        """
        Primary Constructor with default trust_score = 3.
        Provides constructor chaining without code duplication.
        """
        self.canteen_code = canteen_code
        self.canteen_name = canteen_name
        self.trust_score = trust_score

    @classmethod
    def default_score(cls, canteen_code: str, canteen_name: str):
        """Chained constructor for 2-argument instantiation."""
        return cls(canteen_code, canteen_name, trust_score=3)

    def compare_to(self, other: "Canteen") -> int:
        """
        Compares two canteens for ranking order:
        1. Higher trust_score comes first.
        2. Case-insensitive canteen_code order.
        3. Case-sensitive canteen_code tie-breaker.
        4. Canteen name lexicographical order.

        Returns:
            < 0 if self precedes other
            > 0 if self succeeds other
            0 if both are identical
        """
        # 1. Higher trust score comes first
        if self.trust_score != other.trust_score:
            return other.trust_score - self.trust_score

        # 2. Case-insensitive code comparison
        code_self_lower = self.canteen_code.lower()
        code_other_lower = other.canteen_code.lower()

        if code_self_lower < code_other_lower:
            return -1
        elif code_self_lower > code_other_lower:
            return 1

        # 3. Case-sensitive code comparison (preserves original case)
        if self.canteen_code < other.canteen_code:
            return -1
        elif self.canteen_code > other.canteen_code:
            return 1

        # 4. Canteen name comparison
        if self.canteen_name < other.canteen_name:
            return -1
        elif self.canteen_name > other.canteen_name:
            return 1

        return 0

    @staticmethod
    def rank_canteens(canteens: List["Canteen"]) -> List[str]:
        """
        Sorts canteens using a custom O(n^2) Insertion Sort algorithm
        and returns a list of canteen codes.
        """
        arr = list(canteens)
        n = len(arr)

        # Insertion sort using compare_to
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j].compare_to(key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return [canteen.canteen_code for canteen in arr]


# --- Verification ---
if __name__ == "__main__":
    # Test batch matching the image example
    test_canteens = [
        Canteen("HB3-C", "Spice Junction", 3),
        Canteen("hb1-c", "Grand Mess", 5),
        Canteen("HB2-C", "Southern Treats"),  # Defaults trustScore to 3
    ]

    ranked_codes = Canteen.rank_canteens(test_canteens)
    print("Ranked Canteen Codes:", ranked_codes)
