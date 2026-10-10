class AccessChecker:
    @staticmethod
    def classify_access(field_modifier: str, accessor_context: str) -> str:
        """
        Classifies access attempts across 5 contexts based on Java visibility rules:
        - public: ALLOWED across all contexts.
        - protected: ALLOWED in SAME_CLASS, SAME_PACKAGE, and in cross-package 
                     subclasses when accessed via OWN_TYPE reference.
        - default: ALLOWED only in SAME_CLASS and SAME_PACKAGE.
        - private: ALLOWED only in SAME_CLASS.
        """
        modifier = field_modifier.lower()
        context = accessor_context.upper()

        if modifier == "public":
            return "ALLOWED"

        elif modifier == "protected":
            if context in ("SAME_CLASS", "SAME_PACKAGE", "SUBCLASS_DIFFERENT_PACKAGE_OWN_TYPE"):
                return "ALLOWED"
            return "DENIED"

        elif modifier == "default":
            if context in ("SAME_CLASS", "SAME_PACKAGE"):
                return "ALLOWED"
            return "DENIED"

        elif modifier == "private":
            if context == "SAME_CLASS":
                return "ALLOWED"
            return "DENIED"

        return "DENIED"

    @staticmethod
    def describe_context(accessor_context: str) -> str:
        """Turns an underscore-separated code into a Title-Cased readable sentence."""
        words = accessor_context.split('_')
        return " ".join(word.capitalize() for word in words)

    # Java-style camelCase aliases for test-case compatibility
    classifyAccess = classify_access
    describeContext = describe_context


if __name__ == "__main__":
    # --- Example 1: protected + SUBCLASS_DIFFERENT_PACKAGE_OWN_TYPE ---
    print(AccessChecker.classify_access("protected", "SUBCLASS_DIFFERENT_PACKAGE_OWN_TYPE"))
    # Output: ALLOWED[cite: 21]

    # --- Example 2: protected + SUBCLASS_DIFFERENT_PACKAGE_PARENT_TYPE ---
    print(AccessChecker.classify_access("protected", "SUBCLASS_DIFFERENT_PACKAGE_PARENT_TYPE"))
    # Output: DENIED[cite: 21]

    # --- Example 3: describeContext(...) ---
    print(AccessChecker.describe_context("SUBCLASS_DIFFERENT_PACKAGE_OWN_TYPE"))
    # Output: "Subclass Different Package Own Type"[cite: 21]
