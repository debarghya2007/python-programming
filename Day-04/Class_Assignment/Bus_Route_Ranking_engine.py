from typing import List

class BusRoute:
    def __init__(self, route_code: str, route_name: str, priority: int = 0):
        """
        Primary Constructor with optional priority parameter (defaults to 0).
        """
        self.route_code = route_code
        self.route_name = route_name
        self.priority = priority

    @classmethod
    def default_priority(cls, route_code: str, route_name: str):
        """
        Chained constructor for 2-argument instantiation using default priority 0.
        """
        return cls(route_code, route_name, priority=0)

    def compare_to(self, other: 'BusRoute') -> int:
        """
        Compares two routes for ranking order:
        1. Priority (Higher priority first)
        2. Route Code (Case-insensitive lexicographical order)
        3. Route Code (Case-sensitive tie-breaker)
        4. Route Name (Lexicographical order)
        
        Returns:
            < 0 if self precedes other
            > 0 if self succeeds other
            0 if both are equivalent
        """
        # 1. Higher priority comes first
        if self.priority != other.priority:
            return other.priority - self.priority

        # 2. Case-insensitive route code comparison
        code_self_lower = self.route_code.lower()
        code_other_lower = other.route_code.lower()

        if code_self_lower < code_other_lower:
            return -1
        elif code_self_lower > code_other_lower:
            return 1

        # 3. Case-sensitive route code tie-breaker without modifying original code
        if self.route_code < other.route_code:
            return -1
        elif self.route_code > other.route_code:
            return 1

        # 4. Route name comparison
        if self.route_name < other.route_name:
            return -1
        elif self.route_name > other.route_name:
            return 1

        return 0

    @staticmethod
    def rank_routes(routes: List['BusRoute']) -> List[str]:
        """
        Sorts routes using a custom O(n^2) algorithm (Insertion Sort) 
        and returns a list of route codes.
        """
        n = len(routes)
        # Create a copy to avoid mutating input array directly
        arr = list(routes)

        # Insertion Sort using custom compare_to method
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j].compare_to(key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return [route.route_code for route in arr]


# --- Verification ---
if __name__ == "__main__":
    test_routes = [
        BusRoute("RT205L", "Airport Express", 3),
        BusRoute("rt201j", "City Central", 4),
        BusRoute("RT299T", "Night Service")  # Defaults priority to 0
    ]

    ranked_codes = BusRoute.rank_routes(test_routes)
    print("Ranked Route Codes:", ranked_codes)
