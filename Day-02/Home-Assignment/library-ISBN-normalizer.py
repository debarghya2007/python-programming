def normalize_code(raw: str) -> str:
    """
    Trims leading/trailing spaces and converts the first 3 characters 
    (publisher code) to uppercase while preserving the rest of the string.
    """
    trimmed = raw.strip()
    if len(trimmed) < 3:
        return trimmed.upper()
    
    # Uppercase first 3 characters + concatenate remainder
    return trimmed[:3].upper() + trimmed[3:]


def validate_and_format(code: str) -> str:
    """
    Validates the normalized code:
    - Exactly 13 characters long
    - First 3 characters are letters
    - Remaining 10 characters are digits
    
    Returns formatted display line if valid, or specific error reason if invalid.
    """
    # 1. Check total length
    if len(code) != 13:
        return f"Invalid: code must be exactly 13 characters (got {len(code)})"

    # 2. Check first 3 characters are letters (without regex)
    pub_code = code[:3]
    for char in pub_code:
        if not char.isalpha():
            return "Invalid: publisher code must be 3 letters"

    # 3. Check remaining 10 characters are digits (without regex)
    body = code[3:]
    for char in body:
        if not char.isdigit():
            return "Invalid: body after publisher code must contain 10 digits"

    # Parse year (4 digits) and catalog number (6 digits)
    year = body[:4]
    catalog = body[4:]

    # Construct formatted output string
    return f"[{pub_code}] YEAR: {year} | CATALOG: {catalog}"


def main():
    print("=== Library ISBN Normalizer & Validator ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter raw code (e.g., ' pen2026004251 '): ")

        if user_input.strip().lower() in ["exit", "quit"]:
            print("Exiting validator session. Goodbye!")
            break

        if not user_input.strip():
            print("Input cannot be empty. Please try again.\n")
            continue

        # Step 1: Normalize input
        normalized = normalize_code(user_input)

        # Step 2: Validate and format
        result = validate_and_format(normalized)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
