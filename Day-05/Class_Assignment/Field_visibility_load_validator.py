class AccessRuleEngine:
    @staticmethod
    def classify_access(field_modifier: str, accessor_context: str) -> str:
        """
        Classifies access attempts using Java's visibility rules:
        - public: ALLOWED in SAME_CLASS, SAME_PACKAGE, DIFFERENT_PACKAGE
        - protected: ALLOWED in SAME_CLASS, SAME_PACKAGE
        - default: ALLOWED in SAME_CLASS, SAME_PACKAGE
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
    def summarize_batch(attempts: list[list[str]]) -> str:
        """Summarizes a batch of access attempts into total Allowed and Denied counts."""
        allowed_count = 0
        denied_count = 0

        for modifier, context in attempts:
            result = AccessRuleEngine.classify_access(modifier, context)
            if result == "ALLOWED":
                allowed_count += 1
            else:
                denied_count += 1

        return f"Allowed: {allowed_count} | Denied: {denied_count}"


class PatientRecord:
    def __init__(self, patient_id: str, ward_code: str, vitals_score: float, facility_name: str):
        # Trim whitespace first, then check for blankness and minimum length (< 4)
        trimmed_id = patient_id.strip() if patient_id else ""
        if not trimmed_id or len(trimmed_id) < 4:
            raise ValueError("construction rejected")

        # Field Access Levels:
        self.__patient_id = trimmed_id       # Private: Sensitive identifier
        self._ward_code = ward_code          # Package-private / Default: Internal routing
        self._vitals_score = vitals_score    # Private: Medical vital metric
        self.facility_name = facility_name   # Public: General facility info


if __name__ == "__main__":
    # --- Example 1: classifyAccess("private", "SAME_CLASS") ---
    print(AccessRuleEngine.classify_access("private", "SAME_CLASS"))
    # Output: ALLOWED

    # --- Example 2: classifyAccess("default", "DIFFERENT_PACKAGE") ---
    print(AccessRuleEngine.classify_access("default", "DIFFERENT_PACKAGE"))
    # Output: DENIED

    # --- Example 3: summarizeBatch(...) ---
    attempts = [
        ["protected", "SAME_PACKAGE"],
        ["protected", "DIFFERENT_PACKAGE"],
        ["public", "DIFFERENT_PACKAGE"]
    ]
    print(AccessRuleEngine.summarize_batch(attempts))
    # Output: Allowed: 2 | Denied: 1

    # --- Example 4: Invalid PatientRecord (< 4 chars) ---
    try:
        record = PatientRecord("MT9", "W3", 98.2, "MediTrack Central")
    except ValueError as e:
        print(f"new PatientRecord(\"MT9\", ...): {e}")
    # Output: construction rejected

    # --- Example 5: Valid PatientRecord (>= 4 chars) ---
    try:
        valid_record = PatientRecord("MT94", "W3", 98.2, "MediTrack Central")
        print(f"Successfully constructed PatientRecord with ID: {valid_record._PatientRecord__patient_id}")
    except ValueError as e:
        print(e)
