def normalize_reference(raw: str) -> str:
    """
    Trims leading/trailing spaces and converts only the first 3 characters 
    (bank code) to uppercase while preserving the rest of the string.
    """
    trimmed = raw.strip()
    if len(trimmed) < 3:
        return trimmed.upper()
    
    # Uppercase first 3 chars + concatenate remainder
    return trimmed[:3].upper() + trimmed[3:]


def validate_and_format(reference: str) -> str:
    """
    Validates the normalized reference:
    - Exactly 14 characters long
    - First 3 characters are letters
    - Remaining 11 characters are digits
    
    Returns formatted display line if valid, or specific error reason if invalid.
    """
    # 1. Check total length
    if len(reference) != 14:
        return f"Invalid: reference code must be exactly 14 characters (got {len(reference)})"

    # 2. Check first 3 characters are letters (without regex)
    bank_code = reference[:3]
    for char in bank_code:
        if not char.isalpha():
            return "Invalid: bank code must be 3 letters"

    # 3. Check remaining 11 characters are digits (without regex)
    body = reference[3:]
    for char in body:
        if not char.isdigit():
            return "Invalid: body after bank code must contain 11 digits"

    # Parse date components (ddMMyy -> dd/MM/yy) and sequence
    day = body[0:2]
    month = body[2:4]
    year = body[4:6]
    seq = body[6:]

    # Construct formatted output string
    return f"[{bank_code}] DATE: {day}/{month}/{year} | SEQ: {seq}"


def main():
    print("=== Bank Transaction Reference Generator & Validator ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter raw reference code (e.g., ' hdf03022600042 '): ")

        if user_input.strip().lower() in ["exit", "quit"]:
            print("Exiting validator session. Goodbye!")
            break

        if not user_input.strip():
            print("Input cannot be empty. Please try again.\n")
            continue

        # Step 1: Normalize input
        normalized = normalize_reference(user_input)

        # Step 2: Validate and format
        result = validate_and_format(normalized)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
