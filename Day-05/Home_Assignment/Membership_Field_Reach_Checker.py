class AccessRuleEngine:
    @staticmethod
    def classify_access(field_modifier: str, accessor_context: str) -> str:
        """
        Classifies access attempts using Java's visibility rules:
        - public: ALLOWED in SAME_CLASS, SAME_PACKAGE, DIFFERENT_PACKAGE
        - protected / default: ALLOWED in SAME_CLASS, SAME_PACKAGE; DENIED in DIFFERENT_PACKAGE
        - private: ALLOWED only in SAME_CLASS
        """
        modifier = field_modifier.lower()
        context = accessor_context.upper()

        if modifier == "public":
            return "ALLOWED"
        elif modifier in ("protected", "default"):
            if context in ("SAME_CLASS", "SAME_PACKAGE"):
                return "ALLOWED"
            return "DENIED"
        elif modifier == "private":
            if context == "SAME_CLASS":
                return "ALLOWED"
            return "DENIED"

        return "DENIED"

    @staticmethod
    def summarize_by_modifier(attempts: list[list[str]]) -> str:
        """Groups access results per modifier (private, default, protected, public)."""
        counts = {
            "private": {"allowed": 0, "denied": 0},
            "default": {"allowed": 0, "denied": 0},
            "protected": {"allowed": 0, "denied": 0},
            "public": {"allowed": 0, "denied": 0}
        }

        for modifier, context in attempts:
            mod_key = modifier.lower()
            result = AccessRuleEngine.classify_access(mod_key, context)
            if mod_key in counts:
                if result == "ALLOWED":
                    counts[mod_key]["allowed"] += 1
                else:
                    counts[mod_key]["denied"] += 1

        parts = [
            f"{mod}: {counts[mod]['allowed']} allowed / {counts[mod]['denied']} denied"
            for mod in ["private", "default", "protected", "public"]
        ]
        return " | ".join(parts)

    # Java-style camelCase aliases
    classifyAccess = classify_access
    summarizeByModifier = summarize_by_modifier


class LibraryMember:
    def __init__(self, membership_id: str, branch_code: str, fines_owed: float, display_name: str):
        # Trim whitespace first, then reject blank, whitespace-only, or IDs shorter than 4 characters
        trimmed_id = membership_id.strip() if membership_id else ""
        if not trimmed_id or len(trimmed_id) < 4:
            raise ValueError("construction rejected")

        # Field Access Levels:
        self.__membership_id = trimmed_id  # Private: Sensitive member ID
        self._branch_code = branch_code     # Default / Protected: Library branch routing
        self.__fines_owed = fines_owed      # Private: Financial balance
        self.display_name = display_name    # Public: Publicly viewable name


if __name__ == "__main__":
    # --- Example 1: classifyAccess("private", "SAME_CLASS") ---
    print(AccessRuleEngine.classify_access("private", "SAME_CLASS"))
    # Output: ALLOWED[cite: 19]

    # --- Example 2: classifyAccess("protected", "DIFFERENT_PACKAGE") ---
    print(AccessRuleEngine.classify_access("protected", "DIFFERENT_PACKAGE"))
    # Output: DENIED[cite: 19]

    # --- Example 3: summarizeByModifier(...) ---
    attempts = [
        ["private", "SAME_CLASS"],
        ["private", "SAME_PACKAGE"],
        ["default", "SAME_PACKAGE"],
        ["default", "DIFFERENT_PACKAGE"],
        ["protected", "SAME_PACKAGE"],
        ["protected", "SAME_CLASS"],
        ["public", "DIFFERENT_PACKAGE"]
    ]
    print(AccessRuleEngine.summarize_by_modifier(attempts))
    # Output: "private: 1 allowed / 1 denied | default: 1 allowed / 1 denied | protected: 2 allowed / 0 denied | public: 1 allowed / 0 denied"[cite: 20]

    # --- Example 4: Invalid LibraryMember ID (< 4 chars) ---
    try:
        member = LibraryMember("LB9", "BR1", 0, "Priya Nair")
    except ValueError as e:
        print(f"new LibraryMember(\"LB9\", ...): {e}")
    # Output: construction rejected[cite: 20]

    # --- Example 5: Valid LibraryMember ID (>= 4 chars) ---
    try:
        valid_member = LibraryMember("LB94", "BR1", 0, "Priya Nair")
        print(f"Successfully created member with ID: {valid_member._LibraryMember__membership_id}")
    except ValueError as e:
        print(e)
